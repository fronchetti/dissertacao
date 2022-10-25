# Sobre
Pacote de replicação para minha dissertação de mestrado em Ciência da Computação pela Universidade de São Paulo.

# Estrutura do repositório
Este repositório está dividido em pastas da seguinte maneira:
- [**app**](https://github.com/fronchetti/dissertacao/tree/master/app): This folder contains the implementation of our streamlit application, used to demonstrate the capabilities of our classification model. 
- [**data**](https://github.com/fronchetti/dissertacao/tree/master/data): If you are looking for the data we have used for classification, this is the folder where it is located. This folder also contains the raw contributing files of each project analyzed, and the spreadsheets qualitatively analyzed by the authors. 
- [**results**](https://github.com/fronchetti/dissertacao/tree/master/results): This folder contains all the files related to our results section. From the analysis of our classification model to the results of our online questionnaire.
- [**scripts**](https://github.com/fronchetti/dissertacao/tree/master/scripts): If you want to see the code we wrote during the whole classification process, including but not limited to the classification process, this is the folder you are looking for.
- [**qualification**](https://github.com/fronchetti/dissertacao/tree/master/qualification): This folder contains the first set of data we tried to use to train our classifier. This data, analyzed by undegraduate students, was part of my masters qualification and wans't used or discussed in this paper. I just keep it here for recording purposes. 
- [**misc**](https://github.com/fronchetti/dissertacao/tree/master/misc): This folder contains miscellaneous files that were not used in this paper, but support the statements of it (e.g. a screenshot of the top ten languages used on GitHub from the Octoverse website).

# Utilizando o modelo final
We are glad you are interested in our classification model. The final model is available as a [`classification_model.sav`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier) file inside the [`app`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier) folder that you can load using Pickle. If you are not familiar with Pickle or don't know how to load a model, we recommend you to take a look at our code implementation inside the [`app`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier) folder (`classify_content.py` is a good starting point).

# Contato
If you have any questions or are interested in contributing to this project, please don't hesitate to contact us:

* Aluno, Felipe Fronchetti (fronchettl@vcu.edu)
* Orientador, Marco Gerosa (marco.gerosa@nau.edu)
* Co-orientador, Igor Steinmacher (igorfs@utfpr.edu.br)
* Co-orientador, Igor Wiese (igor@utfpr.edu.br)
