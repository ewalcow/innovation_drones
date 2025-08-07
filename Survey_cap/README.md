# Análise Exploratória de Dados - Survey de Drones

## Descrição do Projeto

Este projeto realiza uma análise exploratória de dados (EDA) com base no levantamento de informações sobre o uso de drones pela Polícia Militar do Estado de São Paulo. O objetivo é entender melhor os dados coletados e gerar visualizações que possam ser utilizadas para insights e tomadas de decisão.

## Arquivo de Dados

- **Nome do Arquivo:** Survey_ DRONES - 13_01_25 _cap-hog 2.xlsx
- **Descrição:** O arquivo contém respostas a várias perguntas relacionadas ao uso de drones, incluindo finalidades, dados coletados, condições ambientais, regulamentações, entre outros.

## Passos da Análise Exploratória

1. **Carregamento dos Dados**
   - Utilizei a biblioteca `pandas` para carregar os dados do arquivo Excel.
   - Verifiquei as primeiras linhas do dataframe para garantir que os dados foram carregados corretamente.

2. **Tratamento de Valores Faltantes**
   - Preenchi os valores `NaN` com `N/A` para evitar problemas durante a análise.

3. **Estatísticas Resumidas**
   - Gerei estatísticas descritivas para entender a distribuição dos dados, incluindo contagem, média, desvio padrão, valores mínimos e máximos, etc.
   - As estatísticas foram salvas em um arquivo CSV chamado `summary_statistics.csv`.

4. **Contagem de Valores Únicos**
   - Contei os valores únicos em cada coluna para entender a diversidade dos dados.
   - Os resultados foram salvos em um arquivo CSV chamado `unique_counts.csv`.

5. **Visualização dos Dados**
   - Criei um gráfico de barras para mostrar a contagem de respostas para cada pergunta.
   - O gráfico foi salvo como `response_counts.png`.

## Código Utilizado

```python
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
file_path = r'C:\Users\Elaine\Downloads\inova_drones\Survey_cap_hog\Survey_ DRONES - 13_01_25 _cap-hog.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Exibir as primeiras linhas do dataframe
print(df.head())

# Análise Exploratória de Dados
# Estatísticas Resumidas
summary_stats = df.describe(include='all')
print(summary_stats)

# Contagem de valores únicos em cada coluna
unique_counts = df.nunique()
print(unique_counts)

# Plotagem
# Gráfico de Barras: Contagem de Respostas para Cada Pergunta
response_counts = df.count()
response_counts.plot(kind='bar', figsize=(10, 6))
plt.title('Contagem de Respostas para Cada Pergunta')
plt.xlabel('Perguntas')
plt.ylabel('Contagem de Respostas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('response_counts.png')
plt.show()

# Salvar as estatísticas resumidas em um arquivo CSV
summary_stats.to_csv('summary_statistics.csv')

# Salvar a contagem de valores únicos em um arquivo CSV
unique_counts.to_csv('unique_counts.csv')

print("Análise exploratória de dados e gráficos foram criados e salvos.")
