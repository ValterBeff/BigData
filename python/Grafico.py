# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Obtém o diretório do arquivo atual
base_dir = os.path.dirname(__file__)
img_dir = os.path.join(base_dir, "img")  # Pasta para salvar as imagens
csv_file_path = os.path.join(base_dir, "Data.csv")

# Lê o arquivo CSV
df = pd.read_csv(csv_file_path)

# Limpa espaços em branco e normaliza os valores
df.columns = df.columns.str.strip().str.lower().str.title()  # Primeiras letras maiúsculas

# Gera gráficos para cada coluna categórica
for column in df.columns[1:]:  # Ignora a primeira coluna 'Número Do Paciente'
    if column in ['Concentração', 'Otimismo', 'Atividade Sexual', 'Diagnóstico']:
        # Verifica se a coluna contém dados válidos
        if df[column].isnull().all():
            print(f'A coluna {column} não contém dados válidos.')
            continue  # Pula para a próxima coluna se não houver dados

        # Contagem dos valores 'SIM' e 'NÃO'
        counts = df[column].value_counts()

        # Limita o número de segmentos para o gráfico de pizza
        if len(counts) > 10:  # Limite de 10 valores
            counts = counts.head(10)

        # Criando o gráfico de pizza
        plt.figure(figsize=(8, 6))  # Dimensões adequadas
        wedges, texts, autotexts = plt.pie(
            counts, labels=None, startangle=90,
            autopct='%1.1f%%', pctdistance=0.85,  # Ajusta a distância das porcentagens
            colors=plt.cm.viridis(np.linspace(0, 1, len(counts)))
        )
        plt.title(f'Distribuição de {column}', fontsize=14)
        plt.axis('equal')  # Para manter a forma circular

        # Aumenta a visibilidade dos textos da legenda
        for text in texts:
            text.set_fontsize(12)
        for autotext in autotexts:
            autotext.set_fontsize(12)

        # Adiciona uma legenda ao lado do gráfico com os valores e cores
        legend_labels = [f'{label}: {count}' for label, count in zip(counts.index, counts)]
        legend_colors = [color for color in plt.cm.viridis(np.linspace(0, 1, len(counts)))]

        plt.legend(
            handles=[
                plt.Line2D([0], [0], marker='o', color='w', label=label,
                           markerfacecolor=color, markersize=10)
                for label, color in zip(legend_labels, legend_colors)
            ],
            title="Valores", loc="center left", bbox_to_anchor=(0.8, 0.5), fontsize=10
        )

        # Salva o gráfico como uma imagem na pasta 'img'
        plt.savefig(os.path.join(img_dir, f'grafico_pizza_{column}.png'), bbox_inches='tight')

        # Mostra o gráfico
        plt.show()

    # Gráficos de barra para outras colunas
    else:
        counts = df[column].value_counts()

        plt.figure(figsize=(8, 5))
        bars = plt.bar(
            counts.index, counts.values,
            color=plt.cm.viridis(np.linspace(0, 1, len(counts))), alpha=0.8
        )
        plt.title(f'Contagem de {column}', fontsize=14)
        plt.xlabel(column)
        plt.ylabel('Contagem')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        max_value = counts.max()
        max_index = counts.idxmax()
        min_value = counts.min()
        min_index = counts.idxmin()

        plt.legend(
            [f'Maior: {max_index} ({max_value})', f'Menor: {min_index} ({min_value})'],
            loc='upper right', fontsize=10
        )

        plt.savefig(os.path.join(img_dir, f'grafico_{column}.png'))
        plt.show()
