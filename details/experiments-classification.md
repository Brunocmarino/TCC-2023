# Experimentos do Projeto

## **1 : classificação_2_lstm**
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

## **2 : classificação_1_lstm**
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


## **3 : classificação_3_lstm**
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


## **4 : classificação_4_lstm**
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

## **5 : classificação_5_lstm**
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
    - 
## **6 : classificação_6_lstm**
  - Técnica de ML: **Classificação**
  - Window Size (Time Step): **15 dias**
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
  
## **7 : classificação_7_lstm**
  - Técnica de ML: **Classificação**
  - Window Size (Time Step): **30 dias**
  - Dia predito (Future date): **7 dia** no futuro
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