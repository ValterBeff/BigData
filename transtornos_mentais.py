import kagglehub
import pandas as pd
import os

# Download the latest version of the dataset
path = kagglehub.dataset_download("cid007/mental-disorder-classification")

# Verificar o caminho para garantir que o arquivo CSV correto seja usado
print("Path to dataset files:", path)

# Definir o caminho completo para o arquivo CSV
inputfile = os.path.join(path, 'Dataset-Mental-Disorders.csv')  # Certifique-se de que a extensão seja .csv e não .CVS

# Carregar o arquivo CSV no DataFrame
data = pd.read_csv(inputfile)

# Exibir as primeiras 7 linhas do DataFrame
print(data.head(7))
