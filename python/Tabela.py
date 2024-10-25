#bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtém o diretório do arquivo atual
base_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(base_dir, "Dataset-Mental-Disorders.csv")

# Lê o arquivo CSV
df = pd.read_csv(csv_file_path)

# Remove espaços em branco e converte para minúsculas
df.columns = df.columns.str.strip().str.lower()

# Seleciona algumas linhas e colunas para exibir na tabela
table_data = df[['patient number', 'sadness', 'euphoric', 'exhausted', 'mood swing', 'expert diagnose']].head(10)

# Configurando o gráfico
plt.figure(figsize=(8, 6))  # Tamanho da figura

# Criação da tabela
plt.axis('tight')
plt.axis('off')
table = plt.table(cellText=table_data.values,
                  colLabels=table_data.columns,
                  cellLoc='center',
                  loc='center')

# Ajusta o tamanho da fonte da tabela
table.auto_set_font_size(False)
table.set_fontsize(10)  # Tamanho da fonte ajustado
table.scale(1.2, 1.2)  # Escala para aumentar um pouco o tamanho das células

# Ajusta a largura das colunas de acordo com o conteúdo
table.auto_set_column_width([0, 1, 2, 3, 4, 5])

# Adiciona título
plt.title('Tabela dos Pacientes', fontsize=14)

# Adiciona legendas para as traduções na parte inferior
translations = {
    'patient number': 'Número do Paciente',
    'sadness': 'Tristeza',
    'euphoric': 'Eufórico',
    'exhausted': 'Exausto',
    'mood swing': 'Mudança de Humor',
    'expert diagnose': 'Diagnóstico de Especialista'
}

# Cria uma string para exibir as traduções
translation_line = ' ; '.join([f"{pt} - {eng}" for eng, pt in translations.items()])

# Adiciona a linha de traduções abaixo da tabela
plt.text(0.5, -0.1, translation_line, ha='center', fontsize=10, transform=plt.gca().transAxes)

# Mostra o gráfico
plt.show()