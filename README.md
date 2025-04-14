# 🤖 Distribuição de Ordens para Robôs

Este projeto em Python automatiza a **distribuição de ordens de produção** entre robôs industriais com base nos tempos de execução e regras específicas de alocação. O sistema gera um relatório em **PDF**, incluindo gráficos, estatísticas e os detalhes de cada ordem processada.

---

## ⚙️ Como Funciona?

1. 📂 **Leitura dos arquivos**
   - Lê uma planilha `.ods` com as ordens de produção, referenciando códigos de itens montados e soldados manualmente e em robôs (arquivo gerado automaticamente pelo sistema APS Drummer com data futura de 3 dias úteis — ou seja, a data do arquivo será a data atual + 3 dias úteis).
   - Lê um `.csv` com todas as peças catalogadas que são feitas **apenas nos robôs de solda** e seus respectivos tempos de fabricação, incluindo pré-montagem e solda (arquivo `peças_robô.csv`).

2. 🧠 **Processamento**
   - Filtra ordens válidas conforme as peças cadastradas. Se a ordem no `.ods` possuir um código presente no `.csv`, ela é reconhecida como feita no robô e será processada.
   - Agrupa ordens semelhantes para otimizar a distribuição da produção.
   - Distribui as ordens entre os robôs considerando:
     - Robôs específicos para determinadas peças
     - Robôs genéricos com balanceamento de carga
     - Tempo total de trabalho diário (528 minutos)

3. 📊 **Relatório**
   - Geração de um gráfico de tempo trabalhado e ocioso por robô.
   - Criação de um PDF com:
     - Ordens alocadas por robô
     - Ordens não alocadas
     - Resumo estatístico completo

---

## 🚀 Passo a Passo da Execução

### 📁 Preparar os Arquivos

⚠️ Ambos os arquivos devem estar na **área de trabalho**:

- `peças_robô.csv`  
  → Deve conter duas colunas:
  - `id` → código da peça
  - `tempo` → tempo por peça em minutos

- `ORDENS REFERENTE A XX.XX.XXXX.ods`  
  → Gerado automaticamente pelo APS Drummer com base em **3 dias úteis à frente**.

---

### ▶️ Rodar o Programa

Para rodar o programa, siga os passos abaixo:

1. **Certifique-se de que os arquivos necessários estão na área de trabalho:**
   - O arquivo `peças_robô.csv` contendo as peças e seus tempos de fabricação.
   - O arquivo `ORDENS REFERENTE A XX.XX.XXXX.ods` gerado pelo APS Drummer com as ordens de produção (com data futura de 3 dias úteis).

2. **Instale as dependências do projeto** (caso ainda não tenha feito):
   Abra o terminal (ou o prompt de comando) e execute o seguinte comando para instalar as bibliotecas necessárias:

   ```bash
   pip install pandas matplotlib fpdf pyexcel-ods
