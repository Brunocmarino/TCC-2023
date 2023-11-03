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

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **30 dias**
  - Dia predito (Future date): **1 dia** no futuro
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: relu ou tanh
    - Função de Loss: mean_squared_error
    - Épocas e earlystop: 500, patience 100
  - Threshold: 3%, 5% e 7%

  
## **2 : regressao_2_lstm**

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **30 dias**
  - Dia predito (Future date): **7 dias** no futuro
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: relu ou tanh
    - Função de Loss: mean_squared_error
    - Épocas e earlystop: 500, patience 100
  - Threshold: 3%, 5% e 7%
  - 
## **3 : regressao_3_lstm**

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **30 dias**
  - Dia predito (Future date): **30 dias** no futuro
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: relu ou tanh
    - Função de Loss: mean_squared_error
    - Épocas e earlystop: 500, patience 100
  - Threshold: 3%, 5% e 7%
  - 
## **4 : regressao_4_lstm**

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **15 dias**
  - Dia predito (Future date): **1 dias** no futuro
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: relu ou tanh
    - Função de Loss: mean_squared_error
    - Épocas e earlystop: 500, patience 100
  - Threshold: 3%, 5% e 7%
  - 
## **5 : regressao_5_lstm**

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **7 dias**
  - Dia predito (Future date): **1 dias** no futuro
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: relu ou tanh
    - Função de Loss: mean_squared_error
    - Épocas e earlystop: 500, patience 100
  - Threshold: 3%, 5% e 7%
  - 
## **6 : regressao_6_lstm**

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **15 dias**
  - Dia predito (Future date): **7 dias** no futuro
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: relu ou tanh
    - Função de Loss: mean_squared_error
    - Épocas e earlystop: 500, patience 100
  - Threshold: 3%, 5% e 7%

## **7 : regressao_7_lstm**

  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **15 dias**
  - Dia predito (Future date): **30 dias** no futuro
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: relu ou tanh
    - Função de Loss: mean_squared_error
    - Épocas e earlystop: 500, patience 100
  - Threshold: 3%, 5% e 7%
  
## **X : classificação_2_lstm**
  - Técnica de ML: **Classificação**
  - Window Size (Time Step): **30 dias**
  - Dia predito (Future date): **1 dia** no futuro
  - Threshold: **3%**
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 20
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: softmax
    - Função de Loss: sparse_categorical_crossentropy
    - Épocas e earlystop: 500, patience 100

## **X : classificação_1_lstm**
  - Técnica de ML: **Classificação**
  - Window Size (Time Step): **30 dias**
  - Dia predito (Future date): **1 dia** no futuro
  - Threshold: **5%**
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 20
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: softmax
    - Função de Loss: sparse_categorical_crossentropy
    - Épocas e earlystop: 500, patience 100


## **X : classificação_3_lstm**
  - Técnica de ML: **Classificação**
  - Window Size (Time Step): **30 dias**
  - Dia predito (Future date): **1 dia** no futuro
  - Threshold: **7%**
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 20
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: softmax
    - Função de Loss: sparse_categorical_crossentropy
    - Épocas e earlystop: 500, patience 100


## **X : classificação_4_lstm**
  - Técnica de ML: **Classificação**
  - Window Size (Time Step): **15 dias**
  - Dia predito (Future date): **1 dia** no futuro
  - Threshold: **3%**
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 20
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: softmax
    - Função de Loss: sparse_categorical_crossentropy
    - Épocas e earlystop: 500, patience 100

## **X : classificação_5_lstm**
  - Técnica de ML: **Classificação**
  - Window Size (Time Step): **15 dias**
  - Dia predito (Future date): **1 dia** no futuro
  - Threshold: **5%**
  - Seed: 0
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3332 dias, 
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 20
      - Camadas de LSTM: 1
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout: entre 0 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
      - Função de Ativação: softmax
    - Função de Loss: sparse_categorical_crossentropy
    - Épocas e earlystop: 500, patience 100