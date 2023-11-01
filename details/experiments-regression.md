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

## **1 : single_lstm_regression1**

  Rodei 200 cenários, com uma arquitetura de LSTM com 1 camada

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **30 dias**
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3067 dias, 
  - Uso de Seed aleatória: 190011106
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 200
      - Épocas: 30
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
    - Função de Loss: mean_squared_error
    - Função de Ativação: **relu**, padrão do LSTM
    - Épocas e earlystop: 500, patience 100
    - Melhor Modelo:
      - Trial XXX summary
      -  Hyperparameters:
      -  num_lstm_layers: X
      -  num_lstm_units: X
      -  dropout_rate: 
      -  learning_rate: 
      -  Score (val_loss): 
  - Loss e Loss/Épocas: Gráfico criado
    ![Alt text](./images/regression/single_lstm_regression1.png)
  - Resultados e Métricas Validação:
    - Mean Absolute Error (MAE): 0.09495217779143617
    - Mean Squared Error (MSE): 0.016113716357197976
    - Root Mean Squared Error (RMSE): 0.12693981391666673
    - Coefficient of Determination (R-squared): 0.7932416042694121
  - ROI: Não fiz ainda
  - Acurácia e Acurácia/Épocas: Não se Aplica
  - Threshold: Não se aplica

  
## **2 : regressao_2_lstm**


## **1 : classificação_1_lstm**
  - Técnica de ML: Classificação
  - Window Size (Time Step): 30 dias
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Threshold = 5%
  - Número de Amostras: 3067 dias, 
  - Uso de Seed aleatória: 190011106
  - Modelo de ML usado: LSTM
    - Random Search
      - Épocas: 100 
      - Camadas de LSTM: 1 2, 3 ou 4;
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout entre as camadas: entre 0,2 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
    - Função de Loss: categorical_crossentropy
    - Função de Ativação: softmax
    - Épocas e earlystop: 500, patience 100
    - Melhor Modelo:
      - 
      -  Hyperparameters:
      -  num_lstm_layers: 
      -  num_lstm_units: 
      -  dropout_rate: 
      -  learning_rate: 0
      -  Score (val_loss): 
  - Loss e Loss/Épocas: Gráfico criado
    <!-- ![Alt text](./imagens/regressao_tunnint_2_valLoss.png) -->
  - Resultados e Métricas: XXXXXX
  - ROI: Não fiz ainda
  - Acurácia e Acurácia/Épocas: Não se Aplica
  - Threshold: Não se aplica
