# Single Layer LSTM Classification 15
    df.Close.size: 3332
    target_df_Close.size: 3272
    target_df_Change.size: 3272
    target_df_Variation.size: 3272
    target_df_Class.size: 3272

    Target Class
    0      98
    1    3048
    2     126
    Name: YClass, dtype: int64

    Tamanhos dos dados:
    size: 3272
    train_size: 2290
    validation_size: 327
    test_size: 655

    x_train_data.shape: (2349, 5)
    x_val_data.shape: (386, 5)
    x_test_data.shape: (714, 5)
    y_train_data.shape: (2290, 1)
    y_val_data.shape: (327, 1)
    y_test_data.shape: (655, 1)

    Formas dos DataFrames e arrays:
    df.shape: (3332, 5)
    x_train.shape: (2290, 60, 5), y_train.shape: (2290, 1)
    x_val.shape: (327, 60, 5), y_val.shape: (327, 1)
    x_test.shape: (655, 60, 5), y_test.shape: (655, 1)

## Melhor Modelo Random Search
    Trial 100 Complete 
    Best val_loss So Far: 0.34193724393844604
    Total elapsed time: 00h 25m 43s
    Objective(name="val_loss", direction="min")

    Trial 093 summary
    Hyperparameters:
    num_lstm_units: 16
    dropout_rate: 0.18331179892918603
    learning_rate: 0.0015210043470696266
    Score: 0.34193724393844604
## Treinamento 
    Treinado por 500 épocas com EarlyStop com paciência de 100 épocas
![Alt text](./img/loss15.png)

## Métricas de Classificação
    
    ------------- Train -------------
    Métricas por classe:
    Precisão: [0.         0.92620087 0.        ]
    Recall: [0. 1. 0.]
    F1-Score: [0.         0.96168669 0.        ]
    AUC Médio: [0.5 0.5 0.5]

    Média das métricas:
    Acurácia: 0.9262008733624454
    Precisão: 0.9262008733624454
    Recall: 0.9262008733624454
    F1-Score: 0.9262008733624454
    AUC Médio: 0.944650655021834

    ----------- Validation ----------
    Métricas por classe:
    Precisão: [0.         0.91743119 0.        ]
    Recall: [0. 1. 0.]
    F1-Score: [0.        0.9569378 0.       ]
    AUC Médio: [0.5 0.5 0.5]

    Média das métricas:
    Acurácia: 0.9174311926605505
    Precisão: 0.9174311926605505
    Recall: 0.9174311926605505
    F1-Score: 0.9174311926605505
    AUC Médio: 0.9380733944954129

    ------------- Test -------------
    Métricas por classe:
    Precisão: [0.         0.95725191 0.        ]
    Recall: [0. 1. 0.]
    F1-Score: [0.         0.97815913 0.        ]
    AUC Médio: [0.5 0.5 0.5]

    Média das métricas:
    Acurácia: 0.9572519083969465
    Precisão: 0.9572519083969465
    Recall: 0.9572519083969465
    F1-Score: 0.9572519083969465
    AUC Médio: 0.9679389312977099
![Alt text](./img/auc15.png)
    