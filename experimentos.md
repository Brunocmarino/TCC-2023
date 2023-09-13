# Experimentos do Projeto

 - Regressão e Classificação
 - Dados do preço
 - Dados de análise técnica - indicadores
 - Dados da rede Bitcoin
 - Dados Macroeconômicos
 - Feature Selection (Filter, Wrapper, Embedded, outra)
 - Variar Threshold
 - GridSearch RandomSearch
 - Variar otimizadores
 - Utilizar EarlyStop
 - Variar função de ativação
 - Utilizar acurácia x época
 - Ver Train Test Split - Estratificado em classificação com LSTM
--------
> Para cada teste é bom anotar:\
> Modelo de ML usado \
> Técnica de ML: Classificação ou regressão\
> Quais foram as features\
> Threshold\
> Window Size\
> Quantidade de amostras\
> Balanceamento de classes, se tiver\
> Função de Ativação\
> Otimizadores\
> Épocas e earlystop\
> Loss e Loss/Épocas\
> Acurácia e Acurácia/Épocas\
> Resultados - Métricas\
> ROI
# Experimentos:

## **1 : regressao_1_lstm**

        - Modelo de ML usado: LSTM
        - Construção do Modelo: 1 camada de 64 units
        - Técnica de ML: Regressão
        - Features: Open, High, Low, Close, Volume
        - Valor Predito: Ver Tabela
        - Número de Amostras: 3067 dias, 
        - Threshold: Não se aplica
        - Window Size: Ver tabela
        - Função de Ativação: relu
        - Fução de Loss: mean_squared_error
        - Otimizador: adam
        - Épocas e earlystop: 500
          - patience: 50
        - Loss e Loss/Épocas: Gráfico criado
        - Acurácia e Acurácia/Épocas: Não se Aplica
        - MAE e MAE/Épocas: Gráfico criado
        - Resultados e Métricas: Ver tabela
        - ROI: Não fiz ainda
  
