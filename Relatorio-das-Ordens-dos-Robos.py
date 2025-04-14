from datetime import datetime, timedelta
from pyexcel_ods import get_data
import matplotlib.pyplot as plt
from fpdf import FPDF
import pandas as pd
import os

# Constantes
TEMPO_TRABALHO_DIARIO = 528  # Já está incluso o tempo descontado de almoço (60 minutos)
data_hoje = datetime.now().strftime('%Y-%m-%d')

# Define o caminho para o arquivo na área de trabalho
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "peças_robô.csv")

# Utilize o caminho para ler o arquivo
CAMINHO_CSV = desktop_path

# Dados dos robôs
ROBOS_NOMES = [
    'Rob8', 'Rob159', 'Rob160', 'Rob79', 'Rob41', 'Rob137', 'Rob138', 'Rob21', 'Rob180'
]

# São as peças específicas feitas nos robôs específicos
ordens_ESPECIFICOS = {

    # Faz acionamento indireto (tesoura)
    '326014708': 'Rob8', '326014703': 'Rob8', '326014710': 'Rob8',

    # Faz tampa pantográfica
    '377279405': 'Rob137',

    # Faz de fixação do pé mecânico e outras peças.
    '0376072301': 'Rob41', '0376072302': 'Rob41', '0376072303': 'Rob41', '0376072306': 'Rob41',
    '0376072309': 'Rob41', '0359043430': 'Rob41', '0359043453': 'Rob41', '0359043413': 'Rob41',
    '0359043422': 'Rob41', '0359043408': 'Rob41', '0359043474': 'Rob41', '0359064101': 'Rob41',
    '0376075306': 'Rob41', '0376075302': 'Rob41', '0376075206': 'Rob41', '0376075202': 'Rob41',
    '0376075204': 'Rob41',

   # Faz painel e tampa
    '357225302': 'Rob21', '357225307': 'Rob21', '357225310': 'Rob21', '357228001': 'Rob21',
    '357228003': 'Rob21', '357228103': 'Rob21', '357228206': 'Rob21', '357228207': 'Rob21',
    '357228211': 'Rob21', '357230601': 'Rob21', '357230602': 'Rob21', '357230603': 'Rob21',
    '357230610': 'Rob21', '357230611': 'Rob21', '355121101': 'Rob21', '355121105': 'Rob21',
    '355197601': 'Rob21', '357225301': 'Rob21', '357225317': 'Rob21', '357225304': 'Rob21',
    '357172910': 'Rob21', '357345001': 'Rob21', '377307423': 'Rob21', '377307422': 'Rob21',
    '357366105': 'Rob21', '357366106': 'Rob21', '357366113': 'Rob21', '377307427': 'Rob21',
    '357225315': 'Rob21', '357079113': 'Rob21', '357172933': 'Rob21', '355140601': 'Rob21',
    '377276902': 'Rob21', '377277732': 'Rob21', '377283818': 'Rob21', '331097708': 'Rob21',
    '331097707': 'Rob21', '331097702': 'Rob21', '357225312': 'Rob21', '355121107': 'Rob21',
    '357252606': 'Rob21', '377279405': 'Rob21', '377283719': 'Rob21', '355121108': 'Rob21',
    '377323602': 'Rob21', '357225405': 'Rob21', '357225321': 'Rob21', '357228209': 'Rob21',
    '357228103': 'Rob21', '357230601': 'Rob21', '357230602': 'Rob21', '357228001': 'Rob21',
    '357172918': 'Rob21', '357225414': 'Rob21', '357345005': 'Rob21', '377275302': 'Rob21',
    '357225311': 'Rob21', '357225323': 'Rob21', '357225324': 'Rob21', '357225327': 'Rob21',
    '357225328': 'Rob21', '357225329': 'Rob21', '357225330': 'Rob21', '357225401': 'Rob21',
    '357225402': 'Rob21', '357225423': 'Rob21', '357225424': 'Rob21', '357225426': 'Rob21',
    '357233501': 'Rob21', '357252601': 'Rob21', '357252602': 'Rob21', '357252609': 'Rob21',
    '357228004': 'Rob21', '357228102': 'Rob21', '357228105': 'Rob21', '357228107': 'Rob21',
    '357228109': 'Rob21', '357228110': 'Rob21', '357228202': 'Rob21', '357228203': 'Rob21',
    '357228205': 'Rob21', '357228217': 'Rob21', '357228301': 'Rob21', '357228303': 'Rob21',
    '357228307': 'Rob21', '357228311': 'Rob21', '357340402': 'Rob21', '357368202': 'Rob21',
    '357368211': 'Rob21', '357413105': 'Rob21', '357172901': 'Rob21', '357172902': 'Rob21',
    '357172903': 'Rob21', '357172904': 'Rob21', '357172905': 'Rob21', '357172907': 'Rob21',
    '357172909': 'Rob21', '357172911': 'Rob21', '357172912': 'Rob21', '357172913': 'Rob21',
    '357172915': 'Rob21', '357172916': 'Rob21', '357172919': 'Rob21', '357172920': 'Rob21',
    '357172922': 'Rob21', '357172923': 'Rob21', '357172924': 'Rob21', '357172925': 'Rob21',
    '357172926': 'Rob21', '357172927': 'Rob21', '357172928': 'Rob21', '357172929': 'Rob21',
    '357172930': 'Rob21', '357172931': 'Rob21', '357172932': 'Rob21', '357225303': 'Rob21',
    '357225305': 'Rob21', '357225308': 'Rob21', '357225313': 'Rob21', '357225314': 'Rob21',
    '357225316': 'Rob21', '357225318': 'Rob21', '357225319': 'Rob21', '357225320': 'Rob21',
    '357225322': 'Rob21', '357225325': 'Rob21', '357225326': 'Rob21', '357225403': 'Rob21',
    '357225404': 'Rob21', '357225417': 'Rob21', '357225418': 'Rob21', '357225425': 'Rob21',
    '357225427': 'Rob21', '357228214': 'Rob21', '357228216': 'Rob21', '357252603': 'Rob21',
    '357252604': 'Rob21', '357252607': 'Rob21', '357252611': 'Rob21', '357252612': 'Rob21',
    '357252626': 'Rob21', '357252628': 'Rob21', '357252629': 'Rob21', '357252631': 'Rob21',
    '357335508': 'Rob21', '357368204': 'Rob21', '357368205': 'Rob21', '357368210': 'Rob21',
    '357368212': 'Rob21', '357402903': 'Rob21', '357454801': 'Rob21', '357454802': 'Rob21',
    '357454803': 'Rob21', '357454804': 'Rob21', '357454805': 'Rob21', '357454806': 'Rob21',
    '364061506': 'Rob21', '364091106': 'Rob21', '364109901': 'Rob21', '364109902': 'Rob21',
    '377179202': 'Rob21', '377222639': 'Rob21', '377231302': 'Rob21', '377274804': 'Rob21',
    '377277715': 'Rob21', '377277721': 'Rob21', '377277745': 'Rob21', '377278607': 'Rob21',
    '377283802': 'Rob21', '377283806': 'Rob21', '377283821': 'Rob21', '377283824': 'Rob21',
    '377283827': 'Rob21', '377283830': 'Rob21', '377283834': 'Rob21', '377285402': 'Rob21',
    '377285407': 'Rob21', '377288007': 'Rob21', '377296502': 'Rob21', '377302563': 'Rob21',
    '377302567': 'Rob21', '377303315': 'Rob21', '377305014': 'Rob21', '377305021': 'Rob21',
    '377305025': 'Rob21', '377305029': 'Rob21', '377308602': 'Rob21', '377313424': 'Rob21',
    '377314902': 'Rob21', '357411805': 'Rob21', '357413105': 'Rob21', '357172027': 'Rob21',
    '357172027': 'Rob21', '319138609': 'Rob21', '377285202': 'Rob21', '357242839': 'Rob21',
    '355121111': 'Rob21', '357252632': 'Rob21', '377307412': 'Rob21', '357228106': 'Rob21',
    '355173709': 'Rob21', '357225331': 'Rob21', '377307423': 'Rob21', '357366111': 'Rob21',
    '377310505': 'Rob21', '355121103': 'Rob21', '355197602': 'Rob21', '377283735': 'Rob21',
    '377283846': 'Rob21', '355213102': 'Rob21', '355213102': 'Rob21', '355199002': 'Rob21',
    '355199003': 'Rob21',

    # Não faz painel, apenas tampa
    '357225302': 'Rob180', '357225307': 'Rob180', '357225310': 'Rob180', '357228001': 'Rob180',
    '357228003': 'Rob180', '357228103': 'Rob180', '357228206': 'Rob180', '357228207': 'Rob180',
    '357228211': 'Rob180', '357230601': 'Rob180', '357230602': 'Rob180', '357230603': 'Rob180',
    '357230610': 'Rob180', '357230611': 'Rob180', '357225301': 'Rob180', '357225317': 'Rob180',
    '357225304': 'Rob180', '357172910': 'Rob180', '357345001': 'Rob180', '357366113': 'Rob180',
    '357366105': 'Rob180', '357366106': 'Rob180', '357228209': 'Rob180', '357225315': 'Rob180',
    '357079113': 'Rob180', '357172933': 'Rob180', '377276902': 'Rob180', '377277732': 'Rob180',
    '377283818': 'Rob180', '331097708': 'Rob180', '331097707': 'Rob180', '331097702': 'Rob180',
    '357225312': 'Rob180', '357252606': 'Rob180', '377279405': 'Rob180', '377283719': 'Rob180',
    '377323602': 'Rob180', '357225405': 'Rob180', '377307427': 'Rob180', '377307423': 'Rob180',
    '357225321': 'Rob180', '377307422': 'Rob180', '357252630': 'Rob180', '355197608': 'Rob180',
    '357172918': 'Rob180', '357225414': 'Rob180', '357345005': 'Rob180', '357225311': 'Rob180',
    '357225323': 'Rob180', '357225324': 'Rob180', '357225327': 'Rob180', '357225328': 'Rob180',
    '357225329': 'Rob180', '357225330': 'Rob180', '357225401': 'Rob180', '357225402': 'Rob180',
    '357225423': 'Rob180', '357225424': 'Rob180', '357225426': 'Rob180', '357233501': 'Rob180',
    '357252601': 'Rob180', '357252602': 'Rob180', '357252609': 'Rob180', '377275302': 'Rob180',
    '357368202': 'Rob180', '357368211': 'Rob180', '357340402': 'Rob180', '357228004': 'Rob180',
    '357228102': 'Rob180', '357228105': 'Rob180', '357228107': 'Rob180', '357228109': 'Rob180',
    '357228110': 'Rob180', '357228202': 'Rob180', '357228203': 'Rob180', '357228205': 'Rob180',
    '357228217': 'Rob180', '357228301': 'Rob180', '357228303': 'Rob180', '357228307': 'Rob180',
    '357228311': 'Rob180', '357172027': 'Rob180', '357172027': 'Rob180', '319138609': 'Rob180',
    '357242839': 'Rob180', '357252632': 'Rob180', '377307412': 'Rob180', '357228106': 'Rob180',
    '357225331': 'Rob180', '377307423': 'Rob180', '357366111': 'Rob180', '377283846': 'Rob180',

}

# Lista de robôs inativos
# Ex: {'Rob159', 'Rob180'}
ROBO_INATIVO = {}

def minutos_para_hms(minutos):
    """Converte minutos para o formato HH:MM:SS."""
    horas = minutos // 60
    minutos_restantes = minutos % 60
    segundos = 0  # Como estamos lidando apenas com minutos, os segundos serão 0
    return f"{horas:02}:{minutos_restantes:02}:{segundos:02}"

def carregar_pecas_robo(caminho_csv):
    """Carrega e processa o arquivo CSV com as peças do robô."""
    df = pd.read_csv(caminho_csv, delimiter=';')
    df['id'] = df['id'].astype(str)
    df['tempo'] = df['tempo'].astype(int)
    return df.to_dict(orient='records')

def obter_nome_arquivo_ods():
    """Gera o nome do arquivo ODS com base na data de hoje mais 4 dias úteis e retorna o caminho completo."""
    hoje = datetime.now()
    dias_uteis = 0
    data_futura = hoje
    # O número 5 representa os dias úteis da semana: SEG(0)/TER(1)/QUA(2)/QUI(3)/SEX(4)
    # Precisa ser mudada a parte "dias_uteis < 4:"
    while dias_uteis < 3:
        data_futura += timedelta(days=1)
        if data_futura.weekday() < 5:  # Segunda a sexta-feira
            dias_uteis += 1

    nome_arquivo = f'ORDENS REFERENTE A {data_futura.strftime("%d.%m.%Y")}.ods'
    caminho_arquivo = os.path.join('C:\\Users\\pcicilini.CORP\\Desktop', nome_arquivo)

    # Imprimir a data futura
    print(f"Data Futura: {data_futura.strftime('%d/%m/%Y')}")
    return caminho_arquivo, data_futura

def ler_ordens_do_ods(caminho_ods):
    """Lê os ordens do arquivo ODS e retorna uma lista de ordens com base nas colunas item, Descrição, Qt. Ordem e Início."""
    ordens = []
    try:
        # Lê o arquivo ODS
        data = get_data(caminho_ods)
        planilha = list(data.values())[0]  # Assume que os dados estão na primeira planilha

        # Cria um DataFrame a partir dos dados da planilha
        df = pd.DataFrame(planilha[1:], columns=planilha[0])

        # Remove espaços extras nos nomes das colunas
        df.columns = df.columns.str.strip()

        # Verifica se as colunas esperadas estão presentes
        colunas_esperadas = ['item', 'Descrição', 'Qt. Ordem', 'Início']
        for coluna in colunas_esperadas:
            if coluna not in df.columns:
                raise ValueError(f"Coluna esperada '{coluna}' não encontrada no arquivo.")

        # Seleciona as colunas 'item', 'Descrição', 'Qt. Ordem' e 'Início'
        df = df[['item', 'Descrição', 'Qt. Ordem', 'Início']]
        df.columns = ['A', 'B', 'C', 'D']

        # Converte e limpa os dados
        df['A'] = df['A'].astype(str).str.replace('.0', '')
        df['B'] = df['B'].astype(str)
        
        # Tratar valores ausentes antes da conversão
        df['C'] = pd.to_numeric(df['C'], errors='coerce').fillna(0).astype(int)
        df['D'] = pd.to_datetime(df['D'], errors='coerce', dayfirst=True)

        ordens = df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Arquivo '{caminho_ods}' não encontrado.")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{caminho_ods}': {e}")
    return ordens, len(ordens)  # Retorna o comprimento ajustado

def verificar_ordens(pecas_robo, ordens):
    """Verifica quais ordens são válidas com base nas peças disponíveis."""
    ordens_validas_robo = {peca['id'] for peca in pecas_robo}
    ordens_validas = [ordem for ordem in ordens if ordem['A'] in ordens_validas_robo]
    return ordens_validas

def distribuir_ordens(ordens, pecas_robo):
    hoje = datetime.now()
    ordens_nao_alocados = []

    # Agrupa ordens semelhantes pelo prefixo de 8 dígitos do ID
    grupos_semejantes = {}
    for ordem in ordens:
        chave_grupo = ordem['A'][:7]  # Considera os 7 primeiros dígitos do ID
        if chave_grupo not in grupos_semejantes:
            grupos_semejantes[chave_grupo] = []
        grupos_semejantes[chave_grupo].append(ordem)

    # Ordena grupos de ordens por prioridade
    grupos_ordenados = sorted(
        grupos_semejantes.values(),
        key=lambda g: (g[0]['A'] not in ordens_ESPECIFICOS, g[0]['D'] > hoje),
        reverse=False
    )

    # Define robôs disponíveis
    robos_dedicados = {'Rob8', 'Rob180', 'Rob21', 'Rob137'}
    robos_gerais = [nome for nome in ROBOS_NOMES if nome not in robos_dedicados and nome not in ROBO_INATIVO]

    robos = {nome: [] for nome in ROBOS_NOMES}
    tempos_robos = {nome: 0 for nome in ROBOS_NOMES}

    # Mapeia qual grupo de ordens já foi alocado em qual robô
    grupo_para_robo = {}

    def alocar_ordem(ordem, robo):
        quantidade_restante = ordem['C']
        tempo_por_unidade = next((p['tempo'] for p in pecas_robo if p['id'] == ordem['A']), None)

        if quantidade_restante == 0 or tempo_por_unidade is None:
            ordens_nao_alocados.append(ordem)
            return False

        tempo_disponivel = TEMPO_TRABALHO_DIARIO - tempos_robos[robo]
        unidades_possiveis = min(quantidade_restante, tempo_disponivel // tempo_por_unidade)
        tempo_parcial = unidades_possiveis * tempo_por_unidade

        if unidades_possiveis > 0:
            robos[robo].append({
                'id': ordem['A'],
                'quantidade': unidades_possiveis,
                'data': ordem['D'],
                'descricao': ordem['B'],
                'tempo_total': tempo_parcial
            })
            tempos_robos[robo] += tempo_parcial
            quantidade_restante -= unidades_possiveis

        if quantidade_restante > 0:
            ordens_nao_alocados.append({'A': ordem['A'], 'C': quantidade_restante, 'D': ordem['D'], 'B': ordem['B']})

        return True

    # Alocar ordens grupo por grupo
    for grupo in grupos_ordenados:
        chave_grupo = grupo[0]['A'][:8]

        # Verifica se esse grupo já foi alocado em um robô específico
        if chave_grupo in grupo_para_robo:
            robo_alocado = grupo_para_robo[chave_grupo]
        else:
            # Define um robô adequado para o grupo
            if grupo[0]['A'] in ordens_ESPECIFICOS:
                robo_alocado = ordens_ESPECIFICOS[grupo[0]['A']]
                if robo_alocado in ROBO_INATIVO:
                    ordens_nao_alocados.extend(grupo)
                    continue
            else:
                robo_alocado = min(robos_gerais, key=lambda r: tempos_robos[r])

            grupo_para_robo[chave_grupo] = robo_alocado  # Salva o robô escolhido para este grupo

        # Alocar todas as ordens do grupo no mesmo robô
        for ordem in grupo:
            alocar_ordem(ordem, robo_alocado)

    tempos_ociosos = {nome: TEMPO_TRABALHO_DIARIO - tempo for nome, tempo in tempos_robos.items()}
    return robos, ordens_nao_alocados, tempos_robos, tempos_ociosos

def gerar_grafico(tempos_robos, tempos_ociosos, caminho_arquivo):
    """Gera um gráfico único mostrando o tempo trabalhado e ocioso dos robôs em colunas empilhadas."""
    nomes_robos = list(tempos_robos.keys())
    tempos_robos_values = [tempos_robos[nome] for nome in nomes_robos]
    tempos_ociosos_values = [tempos_ociosos[nome] for nome in nomes_robos]

    fig, ax = plt.subplots(figsize=(14, 7))

    bar_width = 0.6
    index = range(len(nomes_robos))

    # Empilhar os tempos trabalhado e ocioso com cores mais visíveis
    bars1 = ax.bar(index, tempos_robos_values, bar_width, label='Tempo Trabalhado', color='#1f77b4')  # Azul escuro
    bars2 = ax.bar(index, tempos_ociosos_values, bar_width, bottom=tempos_robos_values, label='Tempo Ocioso', color='#ff7f0e')  # Laranja

    ax.set_xlabel('Robôs', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tempo (min)', fontsize=12, fontweight='bold')
    ax.set_title('Tempo Trabalhado e Ocioso dos Robôs', fontsize=14, fontweight='bold')
    ax.set_xticks(index)
    ax.set_xticklabels(nomes_robos, rotation=45, ha='right', fontsize=10)
    ax.legend()

    plt.tight_layout()
    plt.savefig(caminho_arquivo)
    plt.close()

def is_atrasado(data_ordem, data_futura):
    """Verifica se a data da ordem é considerada atrasada em relação à data futura."""
    if isinstance(data_ordem, datetime):
        data_ordem = data_ordem.date()
    if isinstance(data_futura, datetime):
        data_futura = data_futura.date()
    
    return data_ordem < data_futura

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        
        data_hoje = datetime.now().strftime("%d/%m/%Y")
        texto = f"Distribuição de Ordens para Robôs ({data_hoje})"
        self.cell(0, 10, texto, 0, 1, 'C')
        
        self.set_draw_color(0, 0, 0)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def criar_relatorio_pdf(robos, ordens_nao_alocados, pecas_robo, ordens_validos, comprimento_ordens, data_futura, caminho_arquivo):
    """Cria um relatório em PDF com os detalhes dos robôs e ordens não alocados, incluindo o gráfico gerado e uma tabela de resultados."""
    pdf = PDF()
    pdf.set_font("Arial", size=12)

    hoje = datetime.now().date()

    for robo, ordens in robos.items():
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 10, txt=f"Ordens Alocadas:", ln=True)
        pdf.set_font("Arial", size=12)
        
        pdf.set_font("Arial", 'B', size=14)
        pdf.set_text_color(0, 0, 255)
        pdf.cell(0, 10, txt=f"{robo}:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(0, 10, txt=f"Tempo Total de Fabricação: {minutos_para_hms(sum(ordem['tempo_total'] for ordem in ordens if ordem['quantidade'] > 0))}", ln=True, fill=True)
        
        for ordem in ordens:
            if ordem['quantidade'] > 0:
                if is_atrasado(ordem['data'].date(), data_futura):
                    pdf.set_font("Arial", 'I', 12)
                    pdf.set_text_color(255, 0, 0)
                else:
                    pdf.set_font("Arial", size=12)
                    pdf.set_text_color(0, 0, 0)
                
                pdf.cell(0, 10, txt=f"{ordem['id']} - ({ordem['descricao']}) - {ordem['quantidade']} unidades ({minutos_para_hms(ordem['tempo_total'])})", ln=True)
                pdf.cell(0, 10, txt=f"Data Planejada: {ordem['data'].strftime('%d/%m/%Y')}", ln=True)
                pdf.set_text_color(0, 0, 0)
    
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 10, txt="Ordens não Alocadas:", ln=True)

    for ordem in ordens_nao_alocados:
        tempo_total_ordem = ordem['C'] * next(p['tempo'] for p in pecas_robo if p['id'] == ordem['A'])
        if is_atrasado(ordem['D'].date(), data_futura):
            pdf.set_font("Arial", 'I', 12)
            pdf.set_text_color(255, 0, 0)
        else:
            pdf.set_font("Arial", size=12)
            pdf.set_text_color(0, 0, 0)
        
        pdf.cell(0, 10, txt=f"{ordem['A']} - ({ordem['B']}) - {ordem['C']} unidades ({minutos_para_hms(tempo_total_ordem)})", ln=True)
        pdf.cell(0, 10, txt=f"Data Planejada: {ordem['D'].strftime('%d/%m/%Y')}", ln=True)
        pdf.set_text_color(0, 0, 0)

    pdf.add_page()

    pdf.set_font("Arial", size=12)
    total_robos = len(ROBOS_NOMES)
    total_ordens_robo = len(ordens_validos)
    total_unidades = sum(ordem['C'] for ordem in ordens_validos)
    unidades_alocadas = sum(ordem['quantidade'] for ordens in robos.values() for ordem in ordens if ordem['quantidade'] > 0)
    total_ordens_nao_alocadas = len(ordens_nao_alocados)
    total_unidades_nao_alocadas = sum(ordem['C'] for ordem in ordens_nao_alocados)
    ordens_atrasadas = sum(1 for ordem in ordens_validos if is_atrasado(ordem['D'].date(), data_futura))
    porcentagem_ordens_robo = (total_ordens_robo / (comprimento_ordens - 2)) * 100
    porcentagem_formatada = "{:.2f}".format(porcentagem_ordens_robo)
    
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(0, 10, txt="Resumo dos Resultados:", ln=True)
    pdf.set_font("Arial", size=12)
    
    pdf.cell(0, 10, txt=f"Total de Ordens do Peças e Componentes: {comprimento_ordens - 1}", ln=True)
    pdf.cell(0, 10, txt=f"Total de Ordens do Robô: {total_ordens_robo} ({porcentagem_formatada}%)", ln=True)
    pdf.cell(0, 10, txt=f"Ordens não Alocadas no Robô: {total_ordens_nao_alocadas}", ln=True)
    pdf.cell(0, 10, txt=f"Total de Unidades do Robô: {total_unidades}", ln=True)
    pdf.cell(0, 10, txt=f"Unidades Alocadas no Robô: {unidades_alocadas}", ln=True)
    pdf.cell(0, 10, txt=f"Unidades não Alocadas no Robô: {total_unidades_nao_alocadas}", ln=True)
    pdf.cell(0, 10, txt=f"Ordens Atrasadas: {ordens_atrasadas}", ln=True)
    pdf.cell(0, 10, txt=f"Robôs Disponíveis: {total_robos - len(ROBO_INATIVO)}", ln=True)
    pdf.cell(0, 10, txt=f"Robôs Quebrados: {len(ROBO_INATIVO)}", ln=True)
    
    if os.path.exists(caminho_arquivo):
        pdf.ln(10)
        pdf.image(caminho_arquivo, x=10, y=None, w=180)

    data_hoje = datetime.now().strftime('%d_%m_%Y')
    pdf_path = f'C:\\Users\\pcicilini.CORP\\Desktop\\Peças_e_Componentes_Relatório_Ordens_{data_hoje}.pdf'
    pdf.output(pdf_path)
    print(f"Relatório gerado com sucesso em: {pdf_path}")
    input("Pressione Enter para sair...")

def main():
    pecas_robo = carregar_pecas_robo(CAMINHO_CSV)
    caminho_ods, data_futura = obter_nome_arquivo_ods()
    ordens, comprimento_ordens = ler_ordens_do_ods(caminho_ods)
    ordens_validos = verificar_ordens(pecas_robo, ordens)
    robos, ordens_nao_alocados, tempos_robos, tempos_ociosos = distribuir_ordens(ordens_validos, pecas_robo)
    
    # Definir data de hoje e caminho do arquivo gráfico
    data_hoje = datetime.now().strftime('%d_%m_%Y')
    
    caminho_arquivo = f'C:\\Users\\pcicilini.CORP\\Desktop\\Tempo_Robôs_{data_hoje}.png'
    gerar_grafico(tempos_robos, tempos_ociosos, caminho_arquivo)
    criar_relatorio_pdf(robos, ordens_nao_alocados, pecas_robo, ordens_validos, comprimento_ordens, data_futura, caminho_arquivo)

if __name__ == "__main__":
    main()
