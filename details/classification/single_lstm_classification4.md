# Single Layer LSTM Classification 3

df.Close.size: 3332
target_df_Close.size: 3317
target_df_Change.size: 3317
target_df_Variation.size: 3317
target_df_Class.size: 3317

Target Class
0     417
1    2409
2     491
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



## Treinamento 
    Treinado por 500 épocas com EarlyStop com paciência de 100 épocas
![Alt text](./img/loss4.png)

## Métricas de Classificação


![Alt text](./img/auc4.png)