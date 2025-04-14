# 🤖 Distribuição de Ordens de Produção para Robôs de Solda

Este projeto em Python automatiza a **distribuição de ordens de produção** entre robôs industriais com base nos tempos de execução e regras específicas de alocação. O sistema gera um relatório de perfil de carga em **PDF**, incluindo gráficos, estatísticas e os detalhes de cada ordem processada.

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
   - Geração de um gráfico de tempo trabalhado e ocioso por robô (perfil de carga).
   - Criação de um PDF com:
     - Ordens alocadas por robô
     - Ordens não alocadas
     - Resumo estatístico completo

4. 📈 Análise Histórica dos Relatórios Diários

   Desde o mês de novembro de 2024, venho gerando esse relatório de perfil de carga diariamente a partir do script de distribuição de ordens para robôs, que permite monitorar o comportamento de alocação ao longo do tempo. Cada relatório gerado inclui gráficos e informações sobre o tempo trabalhado e ocioso de cada robô, bem como a quantidade de ordens realizadas manualmente ou com auxílio do robô.
   
   A partir desses relatórios diários, faço uma análise contínua sobre o desempenho dos robôs, identificando tendências e problemas recorrentes a partir de um gráfico que compila o resultado em porcentagem da utilização dos robôs na fabricação das peças, pois quanto mais trabalho automatizado, melhor o desempenho e eficiência da fábrica (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/distribuicao-ordens-robos/blob/main/Grafico-da-Utilizacao-dos-Robos.png)).
   
   Para executar o arquivo de atualização (realizado diariamente) do gráfico de tendência dos relatórios é necessário:

   1. **Agrupar os relatórios**:
   Crie uma pasta chamada '**Relatorios-Robo**' e coloque todos os relatórios gerados dentra dela.

   2. **Execute o programa**: No terminal (ou prompt de comando), navegue até a área de trabalho onde o arquivo `.py` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/distribuicao-ordens-robos/blob/main/Grafico-da-Utilizacao-dos-Robos.py)) deve estar localizado e execute o comando abaixo:

   Após a execução do script, os arquivos de saída serão gerados na mesma pasta onde o programa foi executado.
   
   ```bash
   python Grafico-da-utilizacao-dos-robos.py
   ```
   A seguir, explico como é feita essa análise:
   
   - Verificação das Ordens Processadas
     
     - Ordens automatizadas: São aquelas que foram atribuídas aos robôs automaticamente pelo sistema de alocação, de acordo com a programação do APS Drummer e o tempo de produção.
   
     - Ordens manuais: São aquelas que foram atribuídas ao trabalho manual pelo sistema de alocação, de acordo com a programação do APS Drummer e o tempo de produção (normalmente devido a complexidade da peça ou falta de infraestrutura para realizar a solda no robô).
   
   - Análise Comportamental dos Robôs
   
     - Comportamento diário: Verifico como as ordens são distribuídas entre os robôs e se algum robô está sendo sobrecarregado com ordens ou se está subutilizado. Essa análise é crucial para ajustar a carga de trabalho e evitar falhas ou gargalos.
   
     - Robôs subutilizados: Identifico se algum robô está frequentemente ocioso, o que pode indicar que ele não está sendo alocado corretamente ou que há capacidade excessiva para o volume de produção.
   
     - Robôs sobrecarregados: Verifico se algum robô está atingindo seu limite de tempo diário (528 minutos), o que indica que ele está sobrecarregado e pode precisar de redistribuição de tarefas para evitar falhas de produção ou atraso.
   
   - Análise de Tendências
   
     - Aumento de ordens manuais: Através dos relatórios diários, posso identificar se há um aumento no número de ordens sendo feitas manualmente, o que pode indicar a necessidade de ajustes na programação do sistema APS Drummer ou na alocação dos robôs.
   
     - Impacto de mudanças nas ordens: Quando há uma mudança significativa na programação ou um aumento da demanda, essa análise ajuda a entender como os robôs estão lidando com essas alterações, fornecendo informações valiosas para otimização futura.
   
   - Ajustes e Recomendações
   
     - Com base na análise histórica, recomendo ajustes nas regras de alocação, como reconfigurar a distribuição de tarefas entre robôs específicos e genéricos, ajustar os tempos de alocação ou mesmo redistribuir a carga de trabalho manual para evitar falhas na produção.

6. 🎯 **Análise complementar de desempenho dos robôs**

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
