# Single Layer LSTM Classification 11
    df.Close.size: 3332
    target_df_Close.size: 3311
    target_df_Change.size: 3311
    target_df_Variation.size: 3311
    target_df_Class.size: 3311

    Target Class
    0     684
    1    1675
    2     952
    Name: YClass, dtype: int64

    Tamanhos dos dados:
    size: 3311
    train_size: 2317
    validation_size: 331
    test_size: 663

    x_train_data.shape: (2331, 5)
    x_val_data.shape: (345, 5)
    x_test_data.shape: (677, 5)
    y_train_data.shape: (2317, 1)
    y_val_data.shape: (331, 1)
    y_test_data.shape: (663, 1)

    Formas dos DataFrames e arrays:
    df.shape: (3332, 5)
    x_train.shape: (2317, 15, 5), y_train.shape: (2317, 1)
    x_val.shape: (331, 15, 5), y_val.shape: (331, 1)
    x_test.shape: (663, 15, 5), y_test.shape: (663, 1)
## Melhor modelo RandomSearch



## Treinamento 
    Treinado por 500 épocas com EarlyStop com paciência de 100 épocas
![Alt text](./img/loss11.png)

## Métricas de Classificação
    
    
![Alt text](./img/auc11.png)