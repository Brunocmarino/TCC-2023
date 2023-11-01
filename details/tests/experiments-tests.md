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

  Rodei 300 cenários, mas tive problema de conexão e apenas foram testados 288. Com isso apenas peguei os melhores parâmetros e não o modelo
  val_loss: 0.011150936596095562
  tempo total: 6h 28min 14s
  Cenários abordados: 288
  Melhor Cenário:
    - Número de Camadas: 1
    - Número de Células por Camada: 128
    - Taxa de Dropout: 0.21235
    - Taxa de Aprendizado: 0.018102
  
## **2 : regressao_2_lstm**
  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **30 dias**
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3067 dias, 
  - Uso de Seed aleatória: 190011106
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1 2, 3 ou 4;
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout entre as camadas: entre 0,2 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
    - Função de Loss: mean_squared_error
    - Função de Ativação: **tanh**, padrão do LSTM
    - Épocas e earlystop: 500, patience 100
    - Melhor Modelo:
      - Trial 084 summary
      -  Hyperparameters:
      -  num_lstm_layers: 1
      -  num_lstm_units: 48
      -  dropout_rate: 0.2047778725655428
      -  learning_rate: 0.05486272562976355
      -  Score (val_loss): 0.016184943728148937
  - Loss e Loss/Épocas: Gráfico criado
    ![Alt text](./imagens/regressao_tunnint_2_valLoss.png)
  - Resultados e Métricas Validação:
    - Mean Squared Error (MSE): 0.016113716357197976
    - Root Mean Squared Error (RMSE): 0.12693981391666673
    - Mean Absolute Error (MAE): 0.09495217779143617
    - Coefficient of Determination (R-squared): 0.7932416042694121
  - ROI: Não fiz ainda
  - Acurácia e Acurácia/Épocas: Não se Aplica
  - Threshold: Não se aplica
  
## **3 : regressao_3_lstm**
  - Técnica de ML: **Regressão**
  - Window Size (Time Step): **30 dias**
  - Features: Open, High, Low, Close, Volume
  - Valor Predito: Log do preço de fechamento
  - Número de Amostras: 3067 dias, 
  - Uso de Seed aleatória: 190011106
  - Modelo de ML usado: LSTM
    - Random Search
      - Cenários: 100
      - Épocas: 25
      - Camadas de LSTM: 1 2, 3 ou 4;
      - Células em cada camada LSTM: 16, 32, 64, 80, 76, 92 ou 128;
      - Dropout entre as camadas: entre 0,2 e 0,4
      - Taxa de aprendizado do otimizador Adam: entre 0,001 e 0,1
    - Função de Loss: mean_squared_error
    - Função de Ativação: **relu**
    - Épocas e earlystop: 500, patience 100
    - Melhor Modelo:
      - Total elapsed time: 02h 06m 18s
      -  Trial 082 summary
      -  Hyperparameters:
        - num_lstm_layers: 4
        - num_lstm_units: 112
        - dropout_rate: 0.2891505563741961
        - learning_rate: 0.0053345454241352135
        - Score (val_loss): 0.05823514983057976
  - Loss e Loss/Épocas: Gráfico criado
    ![Alt text](./imagens/regressao_tunning_3_valLoss.png)
  - Resultados e Métricas Validação:
    - Mean Squared Error (MSE): 0.05730019477262182
    - Root Mean Squared Error (RMSE): 0.23937459090852106
    - Mean Absolute Error (MAE): 0.1896974583311307
    - Coefficient of Determination (R-squared): 0.26476946201517737
  - ROI: Não fiz ainda
  - Acurácia e Acurácia/Épocas: Não se Aplica
  - Threshold: Não se aplica

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

