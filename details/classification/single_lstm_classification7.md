# Single Layer LSTM Classification 7
    df.Close.size: 3332
    target_df_Close.size: 3296
    target_df_Change.size: 3296
    target_df_Variation.size: 3296
    target_df_Class.size: 3296

    Target Class
    0     913
    1    1162
    2    1221
    Name: YClass, dtype: int64

    Tamanhos dos dados:
    size: 3296
    train_size: 2307
    validation_size: 329
    test_size: 660

    x_train_data.shape: (2336, 5)
    x_val_data.shape: (358, 5)
    x_test_data.shape: (689, 5)
    y_train_data.shape: (2307, 1)
    y_val_data.shape: (329, 1)
    y_test_data.shape: (660, 1)

    Formas dos DataFrames e arrays:
    df.shape: (3332, 5)
    x_train.shape: (2307, 30, 5), y_train.shape: (2307, 1)
    x_val.shape: (329, 30, 5), y_val.shape: (329, 1)
    x_test.shape: (660, 30, 5), y_test.shape: (660, 1)
## Melhor modelo RandomSearch

    Trial 100 Complete
    Best val_loss So Far: 1.08890700340271
    Total elapsed time: 00h 44m 03s
    Showing 10 best trials
    Objective(name="val_loss", direction="min")

    Trial 060 summary
    Hyperparameters:
    num_lstm_units: 80
    dropout_rate: 0.2805087862970485
    learning_rate: 0.09275112873609004
    Score: 1.08890700340271

## Treinamento 
    Treinado por 500 épocas com EarlyStop com paciência de 100 épocas
![Alt text](./img/loss7.png)

## Métricas de Classificação
    ------------- Train -------------
    Métricas por classe:
    Precisão: [0.         0.         0.39618552]
    Recall: [0. 0. 1.]
    F1-Score: [0.         0.         0.56752561]
    AUC Médio: [0.5 0.5 0.5]

    Média das métricas:
    Acurácia: 0.3961855223233637
    Precisão: 0.3961855223233637
    Recall: 0.3961855223233637
    F1-Score: 0.3961855223233637
    AUC Médio: 0.5471391417425228

    ----------- Validation ----------
    Métricas por classe:
    Precisão: [0.37083333 0.         0.41573034]
    Recall: [0.73553719 0.         0.30081301]
    F1-Score: [0.49307479 0.         0.3490566 ]
    AUC Médio: [0.50478783 0.5        0.52419291]

    Média das métricas:
    Acurácia: 0.3829787234042553
    Precisão: 0.3829787234042553
    Recall: 0.3829787234042553
    F1-Score: 0.38297872340425526
    AUC Médio: 0.5372340425531914

    ------------- Test -------------
    Métricas por classe:
    Precisão: [0.59322034 0.         0.29284526]
    Recall: [0.19774011 0.         0.95652174]
    F1-Score: [0.29661017 0.         0.44840764]
    AUC Médio: [0.57402534 0.5        0.5318323 ]

    Média das métricas:
    Acurácia: 0.3196969696969697
    Precisão: 0.3196969696969697
    Recall: 0.3196969696969697
    F1-Score: 0.3196969696969697
    AUC Médio: 0.48977272727272736
![Alt text](./img/auc7.png)