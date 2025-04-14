import os
import re
import logging
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import pandas as pd

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,  # Define o nível mínimo para capturar mensagens
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        # logging.FileHandler("processamento.log"),  # Salva mensagens em um arquivo
        logging.StreamHandler()  # Exibe mensagens no console
    ]
)

def extract_percentage_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        # Regex para encontrar "Total de Ordens do Robô: <número> (<porcentagem>)"
        match = re.search(r"Total de Ordens do Robô:\s*\d+\s*\(([\d.,]+%)\)", text)
        if match:
            return match.group(1)  # Retorna a porcentagem encontrada
        else:
            return None
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo {file_path}: {e}")
        return None

def extract_date_from_filename(file_name):
    # Regex para encontrar datas no formato DD_MM_YYYY no nome do arquivo
    match = re.search(r"(\d{2})_(\d{2})_(\d{4})", file_name)
    if match:
        day, month, year = match.groups()
        return datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y")
    return None

def process_pdfs_in_folder(folder_path):
    data_points = []
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            date = extract_date_from_filename(file_name)
            percentage = extract_percentage_from_pdf(file_path)
            
            if date and percentage:
                percentage_value = float(percentage.replace(",", ".").replace("%", ""))
                data_points.append((date, percentage_value))
                logging.info(f"Porcentagem encontrada em {file_name}: {percentage}")
            else:
                logging.warning(f"Nenhuma porcentagem encontrada em {file_name}")
    
    # Ordenar por data
    data_points.sort(key=lambda x: x[0])
    return data_points

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import logging

def plot_percentages(data_points):
    # Converter para DataFrame para facilitar os cálculos
    df = pd.DataFrame(data_points, columns=["data", "porcentagem"])
    df.set_index("data", inplace=True)
    
    # Cálculo da média móvel de 7 dias
    df["media_movel"] = df["porcentagem"].rolling(window=7).mean()
    
    # Linha de tendência linear
    x = np.arange(len(df))
    coef = np.polyfit(x, df["porcentagem"], 1)  # Ajuste linear
    poly = np.poly1d(coef)
    df["tendencia"] = poly(x)
    
    # Identificar picos e vales
    pico = df["porcentagem"].idxmax()
    vale = df["porcentagem"].idxmin()
    
    # Ajustar limites do eixo Y
    y_min = max(0, df["porcentagem"].min() - 10)  # Margem inferior de 10%
    y_max = min(100, df["porcentagem"].max() + 10)  # Margem superior de 10%
    
    # Criar o gráfico com fundo cinza e aumento das dimensões
    plt.figure(figsize=(18, 12), dpi=600, facecolor='lightgray')  # Aumento das dimensões e DPI
    ax = plt.gca()
    ax.set_facecolor('lightgray')  # Fundo cinza para o gráfico
    
    # Plotando as linhas
    plt.plot(df.index, df["porcentagem"], marker="o", label="Porcentagem de Utilização", color="b")
    plt.plot(df.index, df["media_movel"], linestyle="--", label="Média Móvel (7 dias)", color="g")
    plt.plot(df.index, df["tendencia"], linestyle=":", label="Tendência Linear", color="r")
    
    # Destacar picos e vales
    plt.scatter(pico, df.loc[pico, "porcentagem"], color="purple", label=f"Pico ({df.loc[pico, 'porcentagem']:.2f}%)")
    plt.scatter(vale, df.loc[vale, "porcentagem"], color="brown", label=f"Vale ({df.loc[vale, 'porcentagem']:.2f}%)")
    
    # Anotações no gráfico
    plt.annotate(f"Pico: {df.loc[pico, 'porcentagem']:.2f}%", 
                 xy=(pico, df.loc[pico, "porcentagem"]), 
                 xytext=(10, 20), textcoords="offset points", 
                 arrowprops=dict(arrowstyle="->"), color="purple")
    
    plt.annotate(f"Vale: {df.loc[vale, 'porcentagem']:.2f}%", 
                 xy=(vale, df.loc[vale, "porcentagem"]), 
                 xytext=(-50, -30), textcoords="offset points",
                 arrowprops=dict(arrowstyle="->"), color="brown")
    
    # Ajustar limites do eixo Y
    plt.ylim(y_min, y_max)
    
    # Adicionar título, rótulos e legenda
    plt.title("Evolução da Utilização dos Robôs", fontsize=18, fontweight='bold')
    plt.xlabel("Data", fontsize=14)
    plt.ylabel("Porcentagem (%)", fontsize=14)
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(which="both", linestyle="--", linewidth=0.6, color="gray")
    
    # Adicionar texto informativo (tópico 5) no centro superior
    # Texto informativo no topo direito
    informativo = (
        "Este gráfico representa a evolução da utilização dos robôs em termos percentuais.\n"
        "A média móvel é calculada com base nos últimos 7 dias para suavizar as flutuações.\n"
        "A linha de tendência linear indica a direção geral do desempenho."
    )
    plt.text(
        0.98, 0.98, informativo, ha='right', va='top', transform=ax.transAxes,
        fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.4')
    )

    
    # Ajustar a rotação da legenda do eixo X para diagonal
    plt.xticks(rotation=45, ha="right")  # Rotacionar os rótulos do eixo X
    
    # Caminho para salvar o gráfico na área de trabalho
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    save_path = os.path.join(desktop_path, "Gráfico da Utilização dos Robôs.png")
    plt.savefig(save_path, dpi=300, bbox_inches="tight", facecolor='lightgray')  # Salvar com fundo cinza e 300 DPI
    logging.info(f"Gráfico salvo em: {save_path}")
    
    # plt.show()

# Caminho para a pasta com os PDFs
folder_path = r"C:\Users\pcicilini.CORP\Desktop\Relatorios-Robo"

# Processar os PDFs e obter as porcentagens ordenadas por data
data_points = process_pdfs_in_folder(folder_path)

# Verificar se há dados para plotar
if data_points:
    plot_percentages(data_points)
else:
    logging.warning("Nenhuma porcentagem foi encontrada nos PDFs.")
