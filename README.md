# Sobre
Pacote de replicação para minha dissertação de mestrado em Ciência da Computação pela Universidade de São Paulo.

# Estrutura do repositório
Este repositório está dividido em pastas da seguinte maneira:
- [**data**](https://github.com/fronchetti/dissertacao/tree/master/data): Os dados utilizados para elaboração do modelo de classificação se encontram nesta pasta, incluindo as planilhas analisadas qualitativamente, os projetos preditos e os parágrafos avaliados pelos desenvolvedores no questionário. 
- [**results**](https://github.com/fronchetti/dissertacao/tree/master/results): Os resultados apresentados na dissertação se encontram nesta pasta, incluindo a análise da performance dos diferentes algoritmos de classificação, os dados obtidos na análise qualitativa, a importância das características e demais imagens geradas. 
- [**scripts**](https://github.com/fronchetti/dissertacao/tree/master/scripts): Nesta pasta se encontram os códigos implementados durante a execução deste estudo, da extração dos arquivos via GitHub API ao treinamento de um modelo de classificação capaz de identificar categorias de informação relevantes a novatos.
- [**app**](https://github.com/fronchetti/dissertacao/tree/master/app): Esta pasta contém códigos relacionados a implementação de uma ferramenta de análise de arquivos de contribuição de projetos em software livre. Ela representa uma possível aplicação prática do modelo de classificação gerado por este estudo, e sua versão experimental pode ser acessada em: https://contributing.streamlit.app/. 
- [**qualification**](https://github.com/fronchetti/dissertacao/tree/master/qualification): Esta pasta contém dados apresentados na qualificação deste mestrado, não mais utilizados na versão final do estudo.
- [**overleaf**](https://github.com/fronchetti/dissertacao/tree/master/overleaf): Contém cópias de segurança da apresentação e da dissertação em formato LaTeX.
- [**misc**](https://github.com/fronchetti/dissertacao/tree/master/misc): Esta pasta contém arquivos diversos, sem categoria definida. Inclui basicamente as licenças dos icones utilizados na dissertação, e uma captura de tela do GitHub Octoverse.

# Utilizando o modelo final
We are glad you are interested in our classification model. The final model is available as a [`classification_model.sav`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier) file inside the [`app`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier) folder that you can load using Pickle. If you are not familiar with Pickle or don't know how to load a model, we recommend you to take a look at our code implementation inside the [`app`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier) folder (`classify_content.py` is a good starting point).

# Contato
If you have any questions or are interested in contributing to this project, please don't hesitate to contact us:

* Aluno, Felipe Fronchetti (fronchettl@vcu.edu)
* Orientador, Marco Gerosa (marco.gerosa@nau.edu)
* Co-orientador, Igor Steinmacher (igorfs@utfpr.edu.br)
* Co-orientador, Igor Wiese (igor@utfpr.edu.br)
