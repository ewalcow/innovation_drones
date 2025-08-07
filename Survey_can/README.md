Descrição do Projeto
Título: Análise de Dados de Survey de Drones com Random Forest

Objetivo: O objetivo do projeto é analisar os dados de um survey sobre o uso de drones, utilizando técnicas de aprendizado de máquina para prever a eficiência do uso de drones com base em diferentes características.

Ferramentas Utilizadas:

Pandas: Para manipulação e análise de dados.
NumPy: Para operações matemáticas e manipulação de arrays.
Scikit-learn: Para aprendizado de máquina.
Matplotlib e Seaborn: Para visualização de dados.
WordCloud: Para criação de nuvens de palavras.
Openpyxl: Para trabalhar com arquivos Excel.

Passos do Projeto

Instalação das Bibliotecas:
Instalei as bibliotecas necessárias: pandas, numpy, scikit-learn, matplotlib, seaborn e wordcloud.

Carregamento dos Dados:
Carreguei os dados de um arquivo Excel usando pandas, pulando as primeiras linhas que contêm metadados.

Limpeza dos Dados:
Removi linhas completamente vazias e limpei espaços e quebras de linha nos nomes das colunas.

Seleção de Colunas Numéricas:
Selecionei apenas as colunas numéricas para a modelagem preditiva.

Divisão dos Dados:
Dividi os dados em conjuntos de treino e teste usando train_test_split.

Treinamento do Modelo:
Utilizei um modelo de Random Forest Regressor para treinar com os dados de treino.
Previsões e Avaliação:

Fiz previsões com os dados de teste e avaliei o modelo usando a métrica Mean Squared Error.
Visualização dos Resultados:

Criei gráficos de barras para comparar os valores reais e preditos, e gráficos de radar para visualizar a média das características.
Criei uma nuvem de palavras para visualizar os objetivos do site survey.

Conclusão
Este projeto demonstra como podemos usar Python e suas bibliotecas para analisar dados de surveys sobre o uso de drones, utilizando técnicas de aprendizado de máquina para fazer previsões e visualizações para entender melhor os dados. É uma introdução prática ao mundo da ciência de dados e aprendizado de máquina.
