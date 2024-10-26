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

# Limpa espaços em branco e normaliza os valores
df['Suicidal thoughts'] = df['Suicidal thoughts'].str.strip().str.upper()  # Normaliza para maiúsculas

# Verifica se há duplicatas na coluna 'Suicidal thoughts'
duplicates = df[df.duplicated(subset=['Suicidal thoughts'], keep=False)]
if not duplicates.empty:
    print("Duplicatas encontradas na coluna 'Suicidal thoughts':")
    print(duplicates)

# Dicionário para traduções
translations = {
    'Sadness': 'Tristeza',
    'Euphoric': 'Eufórico',
    'Exhausted': 'Exausto',
    'Sleep dissorder': 'Distúrbio do Sono',
    'Mood Swing': 'Mudança de Humor',
    'Suicidal thoughts': 'Pensamentos Suicidas',
    'Anorxia': 'Anorexia',
    'Authority Respect': 'Respeito à Autoridade',
    'Try-Explanation': 'Tentativa de Explicação',
    'Aggressive Response': 'Resposta Agressiva',
    'Ignore & Move-On': 'Ignorar e Seguir em Frente',
    'Nervous Break-down': 'Colapso Nervoso',
    'Admit Mistakes': 'Admitir Erros',
    'Overthinking': 'Pensar Demais',
    'Sexual Activity': 'Atividade Sexual',
    'Concentration': 'Concentração',
    'Optimisim': 'Otimismo',
    'Expert Diagnose': 'Diagnóstico Especializado'
}

# Gera gráficos para cada coluna categórica
for column in df.columns[1:]:  # Ignora a primeira coluna 'Patient Number'
    print(f'Processando coluna: {column}')
    print(df[column].head())  # Exibe os primeiros valores da coluna

    # Gráficos de pizza para 'Concentration', 'Optimisim', 'Sexual Activity'
    if column in ['Concentration', 'Optimisim', 'Sexual Activity']:
        # Verifica se a coluna contém dados válidos
        if df[column].isnull().all():
            print(f'A coluna {column} não contém dados válidos.')
            continue  # Pula para a próxima coluna se não houver dados

        # Extrai o primeiro número antes do " From 10"
        try:
            first_value = df[column].str.extract(r'(\d+)').astype(int)  # Extrai e converte para inteiro
        except ValueError as e:
            print(f'Erro ao converter valores na coluna {column}: {e}')
            continue  # Pula para a próxima coluna em caso de erro

        counts = first_value[0].value_counts().sort_index()  # Ordena os índices

        # Criando o gráfico de pizza
        plt.figure(figsize=(10, 6))
        wedges, texts, autotexts = plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, 
                                            colors=plt.cm.viridis(np.linspace(0, 1, len(counts))))
        plt.title(f'Distribuição de {translations[column]}', fontsize=14)
        plt.axis('equal')  # Para manter a forma circular

        # Aumenta a visibilidade dos textos da legenda
        for text in texts:
            text.set_fontsize(12)
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(12)

        # Adiciona uma legenda ao lado do gráfico com os valores e cores
        legend_labels = []
        for index, count in counts.items():
            label = translations.get(str(index), "Desconhecido")
            legend_labels.append(f'{label}: {count}')

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

    # Gráfico de pizza para 'Expert Diagnose'
    elif column == 'Expert Diagnose':
        # Contagem dos diagnósticos
        counts = df[column].value_counts()
        
        # Criando o gráfico de pizza
        plt.figure(figsize=(10, 6))
        wedges, texts, autotexts = plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, 
                                            colors=plt.cm.viridis(np.linspace(0, 1, len(counts))))
        plt.title('Distribuição de Diagnósticos', fontsize=14)
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
        plt.savefig(os.path.join(img_dir, 'grafico_diagnosticos_pizza.png'), bbox_inches='tight')
        
        # Mostra o gráfico
        plt.show()

    # Gráficos de barra para outras colunas
    elif column in translations.keys():
        # Contagem das ocorrências
        counts = df[column].value_counts()
        
        # Criando o gráfico
        plt.figure(figsize=(8, 5))
        bars = plt.bar(counts.index, counts.values, color=plt.cm.viridis(np.linspace(0, 1, len(counts))), alpha=0.8)
        
        # Título em português
        plt.title(f'Contagem de {translations[column]}', fontsize=14)
        plt.xlabel(translations[column])
        plt.ylabel('Contagem')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Determina o maior e menor valores
        max_value = counts.max()
        max_index = counts.idxmax()
        min_value = counts.min()
        min_index = counts.idxmin()

        # Adiciona informações à legenda
        plt.legend([f'Maior: {translations.get(max_index, max_index)} ({max_value})', 
                     f'Menor: {translations.get(min_index, min_index)} ({min_value})'], 
                   loc='upper right', fontsize=10)

        # Salva o gráfico como uma imagem na pasta 'img'
        plt.savefig(os.path.join(img_dir, f'grafico_{column}.png'))
        
        # Exibir a legenda de traduções abaixo do gráfico
        plt.figtext(0.5, 0.1, 
                    'Legenda: ' + ', '.join([f'{translations[key]} = {key}' for key in translations.keys()]),
                    horizontalalignment='center', fontsize=10)

        # Mostra o gráfico
        plt.show()
