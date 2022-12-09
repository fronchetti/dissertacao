#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Felipe Fronchetti'
__contact__ = 'fronchetti@usp.br'

import pandas
import math
import csv

if __name__ == '__main__':
    dataframe = pandas.read_csv('predictions.csv')
    spreadsheets = dataframe.groupby('spreadsheet')

    with open('cluster_features.csv', 'w', encoding='utf-8', newline='') as features_file:
        fields = ['n_CF', 'n_CT', 'n_TC', 'n_BW', 'n_DC', 'n_SC', 'n_NC', 'n_paragraphs', 'paragraph_0p', 'paragraph_25p', 'paragraph_75p', 'paragraph_100p']
        writer = csv.DictWriter(features_file, fieldnames=fields)
        writer.writeheader()

        for filename, content in spreadsheets:
            categories_count = content['prediction'].value_counts()
            n_paragraphs = content['row_index'].max()
            paragraph_0p = content['prediction'].iloc[0]
            paragraph_25p = content['prediction'].iloc[math.ceil(n_paragraphs * 0.25)]
            paragraph_75p = content['prediction'].iloc[math.ceil(n_paragraphs * 0.75)]
            paragraph_100p = content['prediction'].iloc[n_paragraphs]

            csv_row = {'n_paragraphs': n_paragraphs, 'paragraph_0p': paragraph_0p, 'paragraph_25p': paragraph_25p, 'paragraph_75p': paragraph_75p, 'paragraph_100p': paragraph_100p}
            csv_row['n_CF'] = categories_count['CF - Contribution flow'] if 'CF - Contribution flow' in categories_count else 0
            csv_row['n_CT'] = categories_count['CT - Choose a task'] if 'CT - Choose a task' in categories_count else 0
            csv_row['n_TC'] = categories_count['TC - Talk to the community'] if 'TC - Talk to the community' in categories_count else 0 
            csv_row['n_BW'] = categories_count['BW - Build local workspace'] if 'BW - Build local workspace' in categories_count else 0
            csv_row['n_DC'] = categories_count['DC - Deal with the code'] if 'DC - Deal with the code' in categories_count else 0
            csv_row['n_SC'] = categories_count['SC - Submit the changes'] if 'SC - Submit the changes' in categories_count else 0
            csv_row['n_NC'] = categories_count['No categories identified.'] if 'No categories identified.' in categories_count else 0

            writer.writerow(csv_row)
