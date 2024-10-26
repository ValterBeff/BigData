# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Obtém o diretório do arquivo atual
base_dir = os.path.dirname(__file__)
img_dir = os.path.join(base_dir, "img")  # Pasta para salvar as imagens
csv_file_path = os.path.join(base_dir, "Dataset-Mental-Disorders.csv")

# Lê o arquivo CSV
df = pd.read_csv(csv_file_path)

# Exibe informações do DataFrame (opcional)
print(df.info())

# Gera gráficos para cada coluna categórica
for column in df.columns[1:]:  # Ignora a primeira coluna 'Patient Number'
    if column in ['Concentration', 'Optimisim', 'Sexual Activity']:
        # Apenas o primeiro valor
        first_value = df[column].str.split(' ', n=1).str[0].astype(int)  # Converte para inteiro
        counts = first_value.value_counts().sort_index()  # Ordena os índices

        # Criando o gráfico de pizza
        plt.figure(figsize=(10, 6))
        wedges, texts, autotexts = plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, 
                                            colors=plt.cm.viridis(np.linspace(0, 1, len(counts))))
        plt.title(f'Distribuição de {column}')
        plt.axis('equal')  # Para manter a forma circular

        # Aumenta a visibilidade dos textos da legenda
        for text in texts:
            text.set_fontsize(12)
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(12)

        # Adiciona uma legenda ao lado do gráfico com os valores e cores
        legend_labels = [f'{label}: {count}' for label, count in zip(counts.index, counts.values)]
        legend_colors = [color for color in plt.cm.viridis(np.linspace(0, 1, len(counts)))]

        # Adiciona a legenda na mesma figura
        plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label=label, 
                                        markerfacecolor=color, markersize=10) 
                            for label, color in zip(legend_labels, legend_colors)], 
                   title="Valores", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

        # Salva o gráfico como uma imagem na pasta 'img'
        plt.savefig(os.path.join(img_dir, f'grafico_pizza_{column}.png'), bbox_inches='tight')
        
        # Mostra o gráfico
        plt.show()

    else:
        # Contagem das ocorrências
        counts = df[column].value_counts()
        
        # Criando o gráfico
        plt.figure(figsize=(8, 5))
        bars = plt.bar(counts.index, counts.values, color=plt.cm.viridis(np.linspace(0, 1, len(counts))), alpha=0.8)
        
        # Título em português
        plt.title(f'Contagem de {column}')
        plt.xlabel(column)
        plt.ylabel('Contagem')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Determina o maior e menor valores
        max_value = counts.max()
        max_index = counts.idxmax()
        min_value = counts.min()
        min_index = counts.idxmin()

        # Adiciona informações à legenda
        plt.legend([f'Maior: {max_index} ({max_value})', f'Menor: {min_index} ({min_value})'], 
                   loc='upper right', fontsize=10)

        # Salva o gráfico como uma imagem na pasta 'img'
        plt.savefig(os.path.join(img_dir, f'grafico_{column}.png'))
        
        # Exibir a legenda de traduções abaixo do gráfico
        plt.figtext(0.5, -0.1, 
                    'Legenda: Sadness = Tristeza, Euphoric = Eufórico, Exhausted = Exausto, '
                    'Sleep disorder = Distúrbio do sono, Mood Swing = Mudança de humor, '
                    'Suicidal thoughts = Pensamentos suicidas, Anorexia = Anorexia, '
                    'Authority Respect = Respeito à autoridade, Try-Explanation = Tentativa de explicação, '
                    'Aggressive Response = Resposta agressiva, Ignore & Move-On = Ignorar e seguir em frente, '
                    'Nervous Breakdown = Colapso nervoso, Admit Mistakes = Admitir erros, '
                    'Overthinking = Pensar demais, Sexual Activity = Atividade sexual, '
                    'Concentration = Concentração, Optimism = Otimismo, Expert Diagnose = Diagnóstico especialista',
                    horizontalalignment='center', fontsize=10)

        # Mostra o gráfico
        plt.show()
