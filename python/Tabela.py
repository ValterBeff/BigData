# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtém o diretório do arquivo atual
base_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(base_dir, "Data.csv")

# Lê o arquivo CSV
df = pd.read_csv(csv_file_path)

# Remove espaços em branco e converte para minúsculas
df.columns = df.columns.str.strip().str.lower()

# Deixa as primeiras letras de cada coluna em maiúsculas
df.columns = df.columns.str.title()

# Seleciona algumas linhas e colunas para exibir na tabela
table_data = df[['Número Do Paciente', 'Tristeza', 'Eufórico', 'Esgotado', 
                 'Mudança De Humor', 'Diagnóstico']].head(10)

# Configurando o gráfico
plt.figure(figsize=(10, 6))  # Tamanho da figura

# Criação da tabela
plt.axis('tight')
plt.axis('off')
table = plt.table(cellText=table_data.values, colLabels=table_data.columns,
                  cellLoc='center', loc='center')

# Ajusta o tamanho da fonte da tabela
table.auto_set_font_size(False)
table.set_fontsize(10)  # Tamanho da fonte ajustado
table.scale(1.2, 1.2)  # Escala para aumentar um pouco o tamanho das células

# Ajusta a largura das colunas de acordo com o conteúdo
table.auto_set_column_width([0, 1, 2, 3, 4, 5])

# Adiciona título
plt.title('Tabela dos Pacientes', fontsize=14)

# Salva a imagem na pasta 'img'
output_path = os.path.join(base_dir, 'img', 'tabela_pacientes.png')
plt.savefig(output_path, bbox_inches='tight')  # Salva a figura

# Mostra o gráfico
plt.show()
