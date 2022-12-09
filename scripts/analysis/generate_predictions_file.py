#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Felipe Fronchetti'
__contact__ = 'fronchetti@usp.br'

import os
import csv
import pickle
import pandas
from functools import partial

# Preprocessing
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
import string

# Heuristic features
from spacy.lang.en import English

def text_preprocessing(X, techniques):
    """Applies to the input text the text processing techniques used
    in our classification.

    Args:
        X (DataFrame): Set of string instances for prediction
        techniques (List): Strings defining the text-procesing techniques to be used.

    Returns:
        DataFrame: Set of string processed instances for prediction
    """
    X = X.dropna()

    def remove_punctuations(paragraph):
        # Removes all the punctuations of the text, including: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
        return paragraph.translate(str.maketrans('', '', string.punctuation))

    def remove_stopwords(paragraph):
        # Removes all the stopwords of the paragraph, such as: "the, for, but, nor"
        stop_words = set(stopwords.words('english'))
        return " ".join([word for word in paragraph.split() if word not in stop_words])

    def lemmatization(paragraph):
        # Applies a lemattizer for each word
        # Read about lemmatization at:
        # nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html
        lemmatizer = WordNetLemmatizer()
        return " ".join([lemmatizer.lemmatize(word) for word in paragraph.split()])

    if 'remove-punctuations' in techniques:        
        X = X.apply(lambda paragraph: remove_punctuations(paragraph))

    if 'remove-stopwords' in techniques:
        X = X.apply(lambda paragraph: remove_stopwords(paragraph))

    if 'lemmatization' in techniques:
        X = X.apply(lambda paragraph: lemmatization(paragraph))

    return X

def add_column_name_prefix(column_name, prefix):
    """Adds a prefix to the columns representing features.

    Args:
        column_name (DataFrame Column): Column to be renamed.
        prefix (String): Prefix to be added to the column (either stat_ or heur_).

    Returns:
        DataFrame Column: Renamed column.
    """
    return prefix + column_name

def create_statistic_features(processed_paragraphs):
    """Uses the pre-trained TF-IDF vectorizer to transform strings into TF-IDF features.

    Args:
        processed_paragraphs (DataFrame): Set of paragraphs for prediction.

    Returns:
        DataFrame: Set of TF-IDF features for prediction.
    """
    vectorizer = pickle.load(open('required_files/tf-idf.sav', 'rb'))
    statistic_features = pandas.DataFrame(vectorizer.transform(processed_paragraphs).toarray(), columns=vectorizer.get_feature_names())
    statistic_features = statistic_features.rename(mapper=partial(add_column_name_prefix, prefix="stat_"), axis="columns")

    return statistic_features

def create_heuristic_features(processed_paragraphs):
    """Uses the pre-defined heuristic patterns to transform strings into heuristic features.

    Args:
        processed_paragraphs (DataFrame): Set of paragraphs for prediction.

    Returns:
        DataFrame: Set of heuristic features for prediction.
    """

    nlp = English()
    ruler = nlp.add_pipe("entity_ruler").from_disk('required_files/patterns.jsonl')

    heuristic_features = pandas.DataFrame()
    heuristic_features['Paragraph'] = processed_paragraphs

    for heuristic in ruler.patterns:
        heuristic_features[heuristic['id']] = 0

    for index, row in heuristic_features.iterrows():
        doc = nlp(row['Paragraph'])

        for heuristic in doc.ents:
            heuristic_features.at[index, heuristic.ent_id_] = 1

    heuristic_features.drop('Paragraph', axis=1, inplace=True)
    heuristic_features = heuristic_features.rename(mapper=partial(add_column_name_prefix, prefix="heur_"), axis="columns")

    return heuristic_features


def select_features(X_predict):
    """Uses the pre-defined feature selector to select the best features for prediction.

    Args:
        X_predict (DataFrame): Set of features for prediction.

    Returns:
        DataFrame: Set of selected features for prediction.
    """
    selector = pickle.load(open('required_files/feature_selector.sav', 'rb'))
    X_selected_predict = selector.transform(X_predict)
    
    return X_selected_predict


def predict_paragraphs(paragraphs):
    print("Applying preprocessing techniques on paragraphs column.")
    preprocessing_techniques = ['remove-stopwords', 'remove-punctuations', 'lemmatization']
    processed_paragraphs = text_preprocessing(paragraphs, preprocessing_techniques)

    print("Converting paragraphs into statistic features.")
    statistic_features = create_statistic_features(processed_paragraphs)

    print("Converting paragraphs into heuristic features.")
    heuristic_features = create_heuristic_features(processed_paragraphs)

    X_predict = pandas.concat([statistic_features, heuristic_features], axis=1)

    print("Selecting features with SelectPercentile (chi2).")
    X_predict = select_features(X_predict)

    classification_model = pickle.load(open('required_files/final_estimator.sav', 'rb'))

    # Using the final estimator, predicts the classes for the unkonwn instances
    y_predict = classification_model.predict(X_predict)

    return y_predict

if __name__ == '__main__':
    # Folders used during the whole process:
    # repository/scripts/classifier/
    analysis_dir = os.getcwd()
    # repository/scripts/
    scripts_dir = os.path.dirname(analysis_dir)
    # repository/
    repository_dir = os.path.dirname(scripts_dir) 
    # repository/data/
    data_dir = os.path.join(repository_dir, 'data')
    # repository/results/
    results_dir = os.path.join(repository_dir, 'results') 
    # repository/data/documentation/spreadsheets/
    spreadsheets_dir = os.path.join(data_dir, 'documentation', 'spreadsheets')
    # repository/data/documentation/spreadsheets/survey
    analysis_spreadsheets_dir = os.path.join(spreadsheets_dir, 'for-analysis')

    if not os.path.isdir('predictions'):
        os.makedirs('predictions')

    predictions_data = []

    for filename in os.listdir(analysis_spreadsheets_dir):
        try:
            filepath = os.path.join(analysis_spreadsheets_dir, filename)
            spreadsheet = pandas.read_excel(filepath)
            paragraphs = spreadsheet.iloc[:, 0]
            predictions = predict_paragraphs(paragraphs)

            for index, prediction in enumerate(predictions):
                prediction = str(predictions[index]).replace('–', '-')
                predictions_row = {'paragraph': paragraphs[index], 'prediction': prediction, 'spreadsheet': filename, 'row_index': index}
                predictions_data.append(predictions_row)
        except Exception as e:
            with open('logs.txt', 'a') as logs_file:
                logs_file.write(filename + '\n')
                logs_file.write(str(e) + '\n')

    with open('predictions.csv', 'w', encoding='utf-8', newline='') as predictions_file:
        fields = ['paragraph', 'prediction', 'spreadsheet', 'row_index']
        writer = csv.DictWriter(predictions_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(predictions_data)