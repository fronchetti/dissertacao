# Sobre
*This dissertation is written in Portuguese. For the paper version in English, please visit our paper's [replication package](https://github.com/fronchetti/FSE-2023).*

Pacote de replicação da minha dissertação de mestrado em Ciência da Computação pela Universidade de São Paulo.

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
Agradecemos o seu interesse em nosso modelo de classificação. A versão final do modelo se encontra disponível através do arquivo serializado [`classification_model.sav`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier) em Python, disponível na pasta [`app`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier). Para utiliza-lo, recomenda-se o uso da biblioteca [`Pickle`](https://docs.python.org/3/library/pickle.html). Caso você não tenha familiaridade com a linguagem ou com aprendizado de máquina, analisar o modo como a identificação de parágrafos foi implementada em nossa ferramenta pode ser um bom começo. Veja o arquivo `classify_content.py` em  [`app`](https://github.com/fronchetti/dissertacao/tree/master/app/classifier).

# Contato
Para quaisquer dúvidas sobre este estudo, por favor entre em contato via e-amail:

* Aluno, Felipe Fronchetti (fronchettl@vcu.edu)
* Orientador, Marco Gerosa (marco.gerosa@nau.edu)
* Co-orientador, Igor Steinmacher (igorfs@utfpr.edu.br)

# Notas
* A grande maioria dos arquivos desta pesquisa estão documentados em Inglês. Caso o leitor tenha qualquer dúvida a respeito de algo, sinta-se livre para entrar em contato. É minha obrigação como pesquisador garantir a transparência deste e de demais estudos.
* Durante o desenvolvimento desta pesquisa o aluno recebeu auxílio financeiro da FAPESP (18/02596-1). Meus sinceros agradecimentos!
