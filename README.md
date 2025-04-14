# 🤖 Distribuição de Ordens para Robôs

Este projeto em Python automatiza a **distribuição de ordens de produção** entre robôs industriais com base nos tempos de execução e regras específicas de alocação. O sistema gera um relatório em **PDF**, incluindo gráficos, estatísticas e os detalhes de cada ordem processada.

---

## ⚙️ Como Funciona?

1. 📂 **Leitura dos arquivos**
   - Lê uma planilha de programação `.ods` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/distribuicao-ordens-robos/blob/main/ORDENS-REFERENTE-A-17.04.2025.ods)) com as ordens de produção, referenciando códigos de itens montados e soldados manualmente e em robôs (arquivo gerado automaticamente pelo sistema APS Drummer com data futura de 3 dias úteis — ou seja, a data do arquivo será a data atual + 3 dias úteis).
   - Lê um `.csv` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/distribuicao-ordens-robos/blob/main/pecas-robo.csv)) com todas as peças catalogadas que são feitas **apenas nos robôs de solda** e seus respectivos tempos de fabricação, incluindo pré-montagem e solda (arquivo `pecas-robo.csv`).

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

4. 🎯 **Análise complementar de desempenho dos robôs**

   Além da alocação automatizada, este projeto permite uma análise técnica aprofundada da performance de cada robô, baseada nas informações presentes no gráfico e no relatório gerado. Esses dados fornecem uma visão estratégica para tomada de decisão em engenharia de produção.

   Os principais pontos analisáveis incluem:
   
   - 🧮 Tempo médio de execução por ordem
   
   Permite identificar se há robôs enfrentando ordens mais complexas ou demoradas.
   
   Fórmula sugerida:
   tempo total trabalhado do robô / número de ordens atribuídas ao robô
   
   - ⚠️ Alocação de tarefas críticas
   
   Avalia quantos robôs operaram próximos do limite diário de tempo (528 minutos), o que pode indicar risco de sobrecarga ou necessidade de redistribuição futura.
   
   - 📊 Eficiência operacional
   
   Compara o tempo útil de trabalho com o tempo ocioso.
   
   Fórmula: eficiência (%) = (tempo trabalhado / 528) × 100
   
   Ajuda a visualizar quais robôs estão subutilizados ou operando no limite.
   
   - 🧩 Balanceamento entre os robôs
   
   Verifica se a carga está sendo bem distribuída ou se há tendência de concentração em robôs genéricos ou específicos. Esse dado pode orientar ajustes nas regras de alocação ou até mesmo na configuração do parque fabril.
   
   - 🔎 Análise dos códigos mais recorrentes
   
   A repetição de determinados códigos de peça pode sugerir uma padronização crescente ou um pico na demanda de itens específicos, orientando decisões de estoque, setup ou abastecimento.

---

## 🚀 Passo a Passo da Execução

### 📁 Preparar os Arquivos

⚠️ Ambos os arquivos devem estar na **área de trabalho**:

- `pecas-robo.csv`  
  → Deve conter duas colunas:
  - `id` → código da peça
  - `tempo` → tempo por peça em minutos

- `ORDENS-REFERENTE-A-XX.XX.XXXX.ods`  
  → Gerado automaticamente pelo APS Drummer com base em **3 dias úteis à frente**.

---

### ▶️ Rodar o Programa

Para rodar o programa, siga os passos abaixo:

1. **Certifique-se de que os arquivos necessários estão na área de trabalho:**
   - O arquivo `pecas-robo.csv` contendo as peças e seus tempos de fabricação.
   - O arquivo `ORDENS-REFERENTE-A-XX.XX.XXXX.ods` gerado pelo APS Drummer com as ordens de produção (com data futura de 3 dias úteis).

2. **Instale as dependências do projeto** (caso ainda não tenha feito):
   Abra o terminal (ou o prompt de comando) e execute o seguinte comando para instalar as bibliotecas necessárias:

   ```bash
   pip install pandas matplotlib fpdf pyexcel-ods
   ```

3. **Execute o programa**: No terminal (ou prompt de comando), navegue até a área de trabalho onde o arquivo `.py` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/distribuicao-ordens-robos/blob/main/Relatorio-das-Ordens-dos-Robos.py)) deve estar localizado e execute o comando abaixo:
   
   Após a execução do script, os arquivos de saída serão gerados na mesma pasta onde o programa foi executado.
   ```bash
   python Relatorio-das-Ordens-dos-Robos.py
   ```

## 📂 O que será gerado

Após rodar o programa, os seguintes arquivos serão gerados:

- 📄 **Relatório em PDF**  
  Relatório completo com gráficos e alocações.  
  👉 [Clique aqui para visualizar o relatório em PDF](https://github.com/azedokilmi/distribuicao-ordens-robos/raw/main/Pecas-e-Componentes-Relatorio-Ordens-11-04-2025.pdf)

- 📈 **Gráfico de Tempo dos Robôs**  
  Gráfico de barras mostrando o tempo trabalhado e o tempo ocioso por robô.  
  👉 [Clique aqui para visualizar o gráfico em PNG](https://github.com/azedokilmi/distribuicao-ordens-robos/blob/main/Tempo-Robos-11-04-2025.png)

## 💡 Ideias Futuras
Interface gráfica (GUI) para facilitar o apontamento e visualização dos dados.

Geração de arquivos via navegador (aplicação web).

Integração com banco de dados para atualização automática.

API REST para integrar o sistema com ERPs como SAP.

Envio automático diário da programação específica para os robôs.

Automação com dashboards interativos (Dash, Power BI etc.) ou sistemas integrados de monitoramento.

## ✍️ Autor
Feito com dedicação por Pedro Cicilini de Nadai 💻
GitHub: @azedokilmi
