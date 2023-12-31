# Single Layer LSTM Classification 5

    df.Close.size: 3332 
    target_df_Close.size: 3317
    target_df_Change.size: 3317
    target_df_Variation.size: 3317
    target_df_Class.size: 3317

    Target Class
    0     213
    1    2868
    2     236
    Name: YClass, dtype: int64

    Tamanhos dos dados:
    size: 3317
    train_size: 2321
    validation_size: 331
    test_size: 665

    x_train_data.shape: (2335, 5)
    x_val_data.shape: (345, 5)
    x_test_data.shape: (679, 5)
    y_train_data.shape: (2321, 1)
    y_val_data.shape: (331, 1)
    y_test_data.shape: (665, 1)

    Formas dos DataFrames e arrays:
    df.shape: (3332, 5)
    x_train.shape: (2321, 15, 5), y_train.shape: (2321, 1)
    x_val.shape: (331, 15, 5), y_val.shape: (331, 1)
    x_test.shape: (665, 15, 5), y_test.shape: (665, 1)

## Melhor modelo RandomSearch

    Trial 100 Complete
    Best val_loss So Far: 0.605977863073349
    Total elapsed time: 01h 51m 06s
    Objective(name="val_loss", direction="min")

    Trial 013 summary
    Hyperparameters:
    num_lstm_units: 32
    dropout_rate: 0.19440549975128163
    learning_rate: 0.08961982192815122
    Score: 0.605977863073349
    ![Alt text](image.png)
## Treinamento 
    Treinado por 500 épocas com EarlyStop com paciência de 100 épocas
![Alt text](./img/loss5.png)

## Métricas de Classificação

    ----- Métricas de Classificação -----
    ------------- Train -------------
    Métricas por classe:
    Precisão: [0.         0.85695821 0.        ]
    Recall: [0. 1. 0.]
    F1-Score: [0.         0.92296984 0.        ]
    AUC Médio: [0.5 0.5 0.5]

    Média das métricas:
    Acurácia: 0.8569582076691081
    Precisão: 0.8569582076691081
    Recall: 0.8569582076691081
    F1-Score: 0.8569582076691081
    AUC Médio: 0.8927186557518313

    ----------- Validation ----------
    Métricas por classe:
    Precisão: [0.         0.81570997 0.        ]
    Recall: [0. 1. 0.]
    F1-Score: [0.        0.8985025 0.       ]
    AUC Médio: [0.5 0.5 0.5]

    Média das métricas:
    Acurácia: 0.8157099697885196
    Precisão: 0.8157099697885196
    Recall: 0.8157099697885196
    F1-Score: 0.8157099697885196
    AUC Médio: 0.8617824773413898

    ------------- Test -------------
    Métricas por classe:
    Precisão: [0.         0.91578947 0.        ]
    Recall: [0. 1. 0.]
    F1-Score: [0.         0.95604396 0.        ]
    AUC Médio: [0.5 0.5 0.5]

    Média das métricas:
    Acurácia: 0.9157894736842105
    Precisão: 0.9157894736842105
    Recall: 0.9157894736842105
    F1-Score: 0.9157894736842105
    AUC Médio: 0.9368421052631579

![Alt text](./img/auc5.png)