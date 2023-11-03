# -*- coding: utf-8 -*-
"""TCC-RegressaoTunner-2-LSTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cpIV5Ruwq9LM2j9g_HtlhswWlGwSjHdM

Nesse projeto uso LSTM para descobrir qual é o preço de fechamento do bitcoin. Uso 5 features relativas ao candle de negociação diária e prevejo o preço de fechamento do dia seguinte
"""

!pip install keras-tuner
!pip install tensorflow
!pip install numpy
!pip install pandas

#Importar as bibliotecas necessárias
import os
import pandas as pd
import numpy as np
import math
import datetime
import time

# Importar sklearn para avaliar o modelo
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score
from sklearn.metrics import mean_poisson_deviance, mean_gamma_deviance, accuracy_score
from sklearn.preprocessing  import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
# from scikeras.wrappers import KerasRegressor
# from tensorflow.keras.wrappers.scikit_learn import KerasRegressor


from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint as sp_randint
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint as sp_randint
# Importar tensorflow para construir o modelo
import tensorflow as tf
import keras
from keras import optimizers
from keras.optimizers import Adam
from keras.models import Sequential, Model, load_model
from keras.layers import *
from keras.callbacks import ModelCheckpoint, History, EarlyStopping
from keras.losses import MeanSquaredError
from keras.metrics import RootMeanSquaredError
from keras.optimizers import Adam

# Importar bibliotecas para plotar gráficos

import matplotlib.pyplot as plt
from itertools import cycle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

"""## Variaveis Globais"""

TIME_STEP = 7           #número de dias usados para prever o futuro
JUMP_STEP = 1
NUM_FEATURES = 5
NUM_PREDICT_FUTURE = 30      #número do dia a serem preditos no futuro (prever o próximo dia? Prever o 7º dia?)
PATH = './drive/MyDrive/TCC/single_lstm_regression8/'
THRESHOLD = 5

"""## Definição das Seeds

"""

import tensorflow as tf
import numpy as np

# Defina a semente do TensorFlow
tf.random.set_seed(0)

# Defina a semente do NumPy
np.random.seed(0)

"""## Importar a Base de Dados"""

ticker = 'BTC-USD'
#1410825600
initial_period = int(time.mktime(datetime.datetime(2014, 9, 16, 0, 0).timetuple()))

#1675814400
final_period = int(time.mktime(datetime.datetime(2023, 10, 31, 0, 0).timetuple()))
# 3067 valores. 2300 é 75%
interval = '1d' # 1d, 1wk, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={initial_period}&period2={final_period}&interval={interval}&events=history&includeAdjustedClose=true'

data = pd.read_csv(query_string)
df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
df.index = pd.to_datetime(df['Date'], format='%Y-%m-%d')

"""Função para escolher os dados utilizados de forma sequencial. A cada t valores

"""

# def selecionaValores(df, jump_step):
#   return df[0::jump_step]

# df = selecionaValores(df, JUMP_STEP)

"""Preparação dos Dados:"""

# Retira a Data e coloca como Index
df.index = df.pop('Date')

data.dropna(inplace=True)
data.reset_index(inplace = True)

# Definir os dataframes dos objetivos a serem alcançados pelo modelo. O Y. Baseados no TimeStep e numero do dia a ser predito

ignoreDays = TIME_STEP + NUM_PREDICT_FUTURE - 1
index = np.array(df.index)[ignoreDays:]

# Dataframe com o valor de fechamento
target_df_Close = pd.DataFrame(df['Close'], index, ['Close']).rename(columns={'Close':'YClose'})

# Dataframe com a variação nominal entre os dias
array_change = np.array(target_df_Close.YClose) - np.array(df['Close'])[TIME_STEP-1 : -NUM_PREDICT_FUTURE]
target_df_Change = pd.DataFrame(array_change, index, columns=['Close']).rename(columns={'Close':'YChange'})

# Dataframe com a variação percentual entre os dias
array_variation = np.array(target_df_Change.YChange) / np.array(df['Close'])[TIME_STEP-1 : -NUM_PREDICT_FUTURE]
target_df_Variation = pd.DataFrame(array_variation*100, index, ['Close']).rename(columns={'Close':'YVariation'})


# Dataframe com a Classe baseado na variação percentual entre os dias
def defineClass(variation, THRESHOLD):
  if variation > THRESHOLD:
    return 2
  elif variation < -THRESHOLD:
    return 0
  else:
    return 1
# Apply the defineClass function to each data point in the array_variation
classifications = [defineClass(variation*100, 3) for variation in array_variation]
target_df_Class3 = pd.DataFrame(classifications, index, ['Close']).rename(columns={'Close':'YClass'})

# Apply the defineClass function to each data point in the array_variation
classifications = [defineClass(variation*100, 5) for variation in array_variation]
target_df_Class5 = pd.DataFrame(classifications, index, ['Close']).rename(columns={'Close':'YClass'})

# Apply the defineClass function to each data point in the array_variation
classifications = [defineClass(variation*100, 7) for variation in array_variation]
target_df_Class7 = pd.DataFrame(classifications, index, ['Close']).rename(columns={'Close':'YClass'})

# Imprimir informações sobre o tamanho das séries de dados
print(f'df.Close.size: {df.Close.size}')
print(f'target_df_Close.size: {target_df_Close.size}')
print(f'target_df_Change.size: {target_df_Change.size}')
print(f'target_df_Variation.size: {target_df_Variation.size}')
print()

#plt.plot(df.index, df['Close'])

"""## Divisão em Treino, Validação e Teste"""

# Divisão entre 70% treino, 10% validação e 20% teste
size = len(target_df_Close)
train_size = int(size * 0.7)
validation_size = int(size * 0.1)
test_size = size - train_size - validation_size

x_train_data = df[: train_size + TIME_STEP - 1]
x_val_data = df[ train_size : (train_size + validation_size + TIME_STEP - 1)]
x_test_data = df[train_size + validation_size : -NUM_PREDICT_FUTURE]

y_train_data = target_df_Close[: train_size]
y_val_data = target_df_Close[train_size : (train_size + validation_size)]
y_test_data = target_df_Close[(train_size + validation_size) :]

#Serão usados nas etapas finais do projeto
y_train_class3 = target_df_Class3[: train_size]
y_val_class3 = target_df_Class3[train_size : (train_size + validation_size)]
y_test_class3 = target_df_Class3[(train_size + validation_size) :]

y_train_class5 = target_df_Class5[: train_size]
y_val_class5 = target_df_Class5[train_size : (train_size + validation_size)]
y_test_class5 = target_df_Class5[(train_size + validation_size) :]

y_train_class7 = target_df_Class7[: train_size]
y_val_class7 = target_df_Class7[train_size : (train_size + validation_size)]
y_test_class7 = target_df_Class7[(train_size + validation_size) :]

y_train_variation = target_df_Variation[: train_size]
y_val_variation = target_df_Variation[train_size : (train_size + validation_size)]
y_test_variation = target_df_Variation[(train_size + validation_size) :]

# Imprimir informações sobre os tamanhos dos dados
print('Tamanhos dos dados:')
print(f'size: {size}')
print(f'train_size: {train_size}')
print(f'validation_size: {validation_size}')
print(f'test_size: {test_size}')
print()

# Imprimir os tamanhos dos dados em linhas separadas
print('x_train_data.shape:', x_train_data.shape)
print('x_val_data.shape:', x_val_data.shape)
print('x_test_data.shape:', x_test_data.shape)
print('y_train_data.shape:', y_train_data.shape)
print('y_val_data.shape:', y_val_data.shape)
print('y_test_data.shape:', y_test_data.shape)
print()

#Transforma os dados para suavizar as variações em escala absoluta
# Transforma input data
scaler_train_input = MinMaxScaler(feature_range=(0, 1))
scaled_train_input = scaler_train_input.fit_transform(x_train_data)

scaled_val_input = scaler_train_input.transform(x_val_data)
scaled_test_input = scaler_train_input.transform(x_test_data)

# Transforma output data para o log do resultado
# scaled_train_output = np.array(y_train_data)
# scaled_val_output = np.array(y_val_data)
# scaled_test_output = np.array(y_test_data)
scaled_train_output = np.log10(np.array(y_train_data))
scaled_val_output = np.log10(np.array(y_val_data))
scaled_test_output = np.log10(np.array(y_test_data))

def createDataset(x, y, time_step=1):
  input = []
  output = []
  for i in range(len(y)):
    row = np.array([e for e in x[i : i + time_step]])
    input.append(row)
    output.append(y[i])
  return np.array(input), np.array(output)

x_train, y_train = createDataset(scaled_train_input, scaled_train_output, TIME_STEP)
x_val, y_val = createDataset(scaled_val_input, scaled_val_output, TIME_STEP)
x_test, y_test = createDataset(scaled_test_input, scaled_test_output, TIME_STEP)

# Imprimir informações sobre as formas dos DataFrames e arrays
print('Formas dos DataFrames e arrays:')
print(f'df.shape: {df.shape}')
print(f'x_train.shape: {x_train.shape}, y_train.shape: {y_train.shape}')
print(f'x_val.shape: {x_val.shape}, y_val.shape: {y_val.shape}')
print(f'x_test.shape: {x_test.shape}, y_test.shape: {y_test.shape}')
print()

"""## Construção do Modelo LSTM

### Random Search com LSTM
"""

import keras_tuner as kt
import keras.backend as K

def build_singleLayer_lstm_model(hp):
  #Variables to change with RandomSearch
  units = hp.Int('num_lstm_units', min_value=16, max_value=128, step=16)
  dropout = hp.Float('dropout_rate', min_value=0, max_value=0.4)
  learningRate = hp.Float('learning_rate', min_value=0.001, max_value=0.1, sampling='log')
  activation = hp.Choice('activation', ['tanh', 'relu'])

  model = keras.Sequential()
  model.add(LSTM(
      units = units,
      return_sequences=False,
      input_shape = (x_train.shape[1], x_train.shape[2]),
      activation=activation
      ))
  model.add(Dropout(dropout))
  model.add(Dense(1))
  optimizer = Adam(learning_rate=learningRate)
  model.compile(loss='mean_squared_error', optimizer=optimizer,metrics=['mean_squared_error'])
  return model

earlystopping = EarlyStopping(monitor='val_loss', patience=25, restore_best_weights=True)

tuner = kt.RandomSearch(
    build_singleLayer_lstm_model,
    objective='val_loss',
    max_trials=100,
    executions_per_trial=1,
    directory=PATH,
    overwrite=True,
    project_name='lstm_tuning')

tuner.search_space_summary()

tuner.search(x_train, y_train, epochs=25, validation_data=(x_val, y_val), callbacks=[earlystopping], batch_size=32, verbose=1)
tuner.results_summary()

#Get the best model and hyperparameters
best_model = tuner.get_best_models(num_models=1)[0];
best_model.save(PATH + 'best_model_tunner.hdf5');
best_model.build(x_train.shape);
best_model.summary();
best_hyperparameters = tuner.get_best_hyperparameters(num_trials=1)[0];

"""## Mostra Treina o melhor modelo com EarlyStop"""

best_model = load_model(PATH + 'best_model_tunner.hdf5')
best_model.build(x_train.shape);
best_model.summary();

earlystopping = EarlyStopping(monitor='val_loss', patience=100, restore_best_weights=True)

#Define um checkpoint para a melhor época
checkpoint_path = PATH + 'best_model_earlyStop.hdf5'
checkpoint = ModelCheckpoint(filepath=checkpoint_path,
                             monitor='val_loss',
                             verbose=1,
                             save_best_only=True,
                             mode='min')
callbacks = [checkpoint, earlystopping]
#Train the best model
history = best_model.fit(x_train, y_train, epochs=500, batch_size=32, validation_data=(x_val, y_val), verbose=1,
                              callbacks=callbacks)

"""## Resultados

Gráfico de Perda por Época
"""

checkpoint_path = PATH + 'best_model_earlyStop.hdf5'
loaded_model = load_model(checkpoint_path)
output_file = open(PATH + "saida.txt", "w")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# ax1.plot(history.history['r_square'])
# ax1.plot(history.history['val_r_square'])
# ax1.set_title('Model r_square')
# ax1.set_ylabel('r_square')
# ax1.set_xlabel('Epoch')
# ax1.legend(['Train', 'Validation'], loc='upper left')


ax2.plot(history.history['loss'])
ax2.plot(history.history['val_loss'])
ax2.set_title('Model Loss = Mean Squared Error')
ax2.set_ylabel('Loss')
ax2.set_xlabel('Epoch')
ax2.legend(['Train', 'Validation'], loc='upper left')
plt.show()

"""Métricas de Desempenho

"""

y_train_predict_log = loaded_model.predict(x_train)

y_val_predict_log = loaded_model.predict(x_val)

y_test_predict_log = loaded_model.predict(x_test)

def printResults(expected, result):
  mse = mean_squared_error(expected, result)
  rmse = np.sqrt(mse)
  mae = mean_absolute_error(expected, result)
  r2 = r2_score(expected, result)
  mape = np.mean(np.abs((expected - result) / expected)) * 100
  print(f"MAE: {mae}")
  print(f"MSE: {mse}")
  print(f"RMSE: {rmse}")
  print(f"MAPE: {mape}%")
  print(f"R²: {r2}")

print('----- Métricas de Regressão -----')
print('------------- Train -------------')
printResults(y_train, y_train_predict_log)
print('---------- Validation -----------')
printResults(y_val, y_val_predict_log)
print('-------------- Test -------------')
printResults(y_test, y_test_predict_log)
print()

"""## Transformar Regressão e Classes

"""

print("Target Class Threshold: 3")
class_counts = target_df_Class3['YClass'].value_counts().sort_index()
print(class_counts)
print()

print("Target Class Threshold: 5")
class_counts = target_df_Class5['YClass'].value_counts().sort_index()
print(class_counts)
print()

print("Target Class Threshold: 7")
class_counts = target_df_Class7['YClass'].value_counts().sort_index()
print(class_counts)
print()
print()

# y_test_predict = valor predito
# y_test = preço real
# y_test_class = a classe da variação percentual real
# y_test_variation = a variação percentual real
# Para prever o percentual predito, é necessário encontrar o valor real anterior
# Para isso, deve-se usar o valor real e a variação real. Variação = (V_final - V_inicial)/V_inicial

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
def printClassificationResults(y_test_class):
  y_test_predict = 10 ** y_test_predict_log
  y_test_real = 10 ** y_test
  y_test_class = np.array(y_test_class)

  def defineClass(variation):
    if variation > THRESHOLD:
      return 2
    elif variation < -THRESHOLD:
      return 0
    else:
      return 1
  def find_initial_price(preco_final, variacao_percentual):
    return preco_final / (1 + (variacao_percentual / 100))

  y_test_initial = [find_initial_price(y_test_real[i], np.array(y_test_variation)[i]) for i in range(len(y_test_real))]

  y_test_variation_predict = ((y_test_predict - y_test_initial) / y_test_initial) * 100

  y_test_class_predict = [defineClass(variation) for variation in y_test_variation_predict]


  # Transforme as classes reais e previstas em rótulos binários
  lb = LabelBinarizer()
  y_test_class_bin = lb.fit_transform(y_test_class)
  y_test_class_predict_bin = lb.transform(y_test_class_predict)

  accuracy = accuracy_score(y_test_class, y_test_class_predict)
  # Precisão, Recall e F1-Score (para cada classe)
  precision = precision_score(y_test_class, y_test_class_predict, average=None)
  recall = recall_score(y_test_class, y_test_class_predict, average=None)
  f1 = f1_score(y_test_class, y_test_class_predict, average=None)
  roc_auc = roc_auc_score(y_test_class_bin, y_test_class_predict_bin, average=None)

  average_precision = precision_score(y_test_class, y_test_class_predict, average='micro')
  average_recall = recall_score(y_test_class, y_test_class_predict, average='micro')
  average_f1 = f1_score(y_test_class, y_test_class_predict, average='micro')
  average_auc = roc_auc_score(y_test_class_bin, y_test_class_predict_bin, average='micro')

  print("Métricas por classe:")
  print("Precisão:", precision)
  print("Recall:", recall)
  print("F1-Score:", f1)
  print("AUC Médio:", roc_auc)
  print()
  print("Média das métricas:")
  print("Acurácia:", accuracy)
  print("Precisão:", average_precision)
  print("Recall:", average_recall)
  print("F1-Score:", average_f1)
  print("AUC Médio:", average_auc)
  print()


  def plotROC(y_true, y_score, class_names):
      n_classes = len(class_names)

      # Inicialize a figura do gráfico
      plt.figure(figsize=(8, 6))

      # Defina as cores para as curvas ROC
      colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

      # Plote as curvas ROC para cada classe
      for i in range(n_classes):
          fpr, tpr, _ = roc_curve(y_true[:, i], y_score[:, i])
          roc_auc = auc(fpr, tpr)
          plt.plot(fpr, tpr, color=colors[i], lw=2, label=f'Class {class_names[i]} (AUC = {roc_auc:.2f})')

      # Plot the random chance line
      plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Chance')

      # Customize the plot
      plt.xlim([0.0, 1.0])
      plt.ylim([0.0, 1.05])
      plt.xlabel('False Positive Rate')
      plt.ylabel('True Positive Rate')
      plt.title('ROC Curves for Multiclass Classification')
      plt.legend(loc='lower right')
      plt.show()

  # Supondo que y_test_class_bin e y_test_class_predict_bin são matrizes com as probabilidades das classes
  class_names = [0, 1, 2]  # Nomes das classes ou rótulos
  plotROC(y_test_class_bin, y_test_class_predict_bin, class_names)

print('=============================')
print('Métricas para o THRESHOLD = 3')
printClassificationResults(y_test_class3)

print('=============================')
print('Métricas para o THRESHOLD = 5')
printClassificationResults(y_test_class5)

print('=============================')
print('Métricas para o THRESHOLD = 7')
printClassificationResults(y_test_class7)

"""Mostrar as métricas de Classificação

"""

# from sklearn.metrics import roc_curve, auc
# import matplotlib.pyplot as plt

# def plotROC(y_true, y_score, class_names):
#     n_classes = len(class_names)

#     # Inicialize a figura do gráfico
#     plt.figure(figsize=(8, 6))

#     # Defina as cores para as curvas ROC
#     colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

#     # Plote as curvas ROC para cada classe
#     for i in range(n_classes):
#         fpr, tpr, _ = roc_curve(y_true[:, i], y_score[:, i])
#         roc_auc = auc(fpr, tpr)
#         plt.plot(fpr, tpr, color=colors[i], lw=2, label=f'Class {class_names[i]} (AUC = {roc_auc:.2f})')

#     # Plot the random chance line
#     plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Chance')

#     # Customize the plot
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.05])
#     plt.xlabel('False Positive Rate')
#     plt.ylabel('True Positive Rate')
#     plt.title('ROC Curves for Multiclass Classification')
#     plt.legend(loc='lower right')
#     plt.show()

# # Supondo que y_test_class_bin e y_test_class_predict_bin são matrizes com as probabilidades das classes
# class_names = [0, 1, 2]  # Nomes das classes ou rótulos
# plotROC(y_test_class_bin, y_test_class_predict_bin, class_names)

# Calcule o AUC médio para todas as classes
# None (padrão): Nesse caso, o AUC é calculado separadamente para cada classe e retornado como uma matriz. Não é um AUC médio.
# micro: Calcula o AUC médio considerando todas as instâncias individualmente. Ele faz isso tratando todas as previsões como uma única matriz de valores verdadeiros e previstos, e, em seguida, calculando o AUC.
# macro: Calcula o AUC médio para cada classe individualmente e, em seguida, tira a média desses valores. Isso atribui o mesmo peso a cada classe, independentemente do número de instâncias em cada classe.
# weighted: Calcula o AUC médio para cada classe individualmente e, em seguida, tira a média desses valores, dando pesos iguais a cada classe com base no número de instâncias na classe. Classes com mais instâncias têm um peso maior.
# https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html
# In a multi-class classification setup with highly imbalanced classes, micro-averaging is preferable over macro-averaging. In such cases, one can alternatively use a weighted macro-averaging, not demoed here.
# Micro (average='micro'): Nessa abordagem, o AUC médio é calculado considerando todas as instâncias (amostras de dados) individualmente, independentemente da classe a que pertencem. Todas as previsões e rótulos verdadeiros são tratados como se fossem de uma única classe. Isso significa que cada instância tem o mesmo peso na métrica, independentemente de qual classe ela pertença. É como se todas as instâncias fossem combinadas em uma única classe para calcular o AUC.
# Em resumo, a abordagem "micro" calcula o AUC médio considerando todas as instâncias individualmente, sem considerar as classes. Isso significa que o desempenho geral do modelo é avaliado sem levar em consideração a estrutura de várias classes no problema de classificação. Essa abordagem é útil quando você deseja avaliar o desempenho global do modelo em todas as instâncias de forma igual.
# Se você usar average='None', obterá métricas para cada classe separadamente, o que pode ser útil se você estiver interessado no desempenho específico de cada classe.
# Se você usar average='micro', estará avaliando o desempenho geral do modelo, considerando igualmente todas as instâncias, independentemente da classe a que pertencem.
# Se você usar average='macro', todas as classes são tratadas igualmente, independentemente do número de instâncias em cada classe.
# Se você usar average='weighted', as classes são tratadas com pesos iguais ao número de instâncias em cada classe.

# Esses resultados indicam que, embora o modelo possa ter um desempenho globalmente bom, ele pode estar tendo dificuldade em discriminar entre classes individuais. Os resultados com average=None estão indicando que o modelo não está fazendo melhor do que uma classificação aleatória (AUC de 0.5) para cada classe em relação às outras.

# Portanto, ao avaliar o desempenho de um modelo multiclasse, é importante considerar não apenas a AUC global, mas também as AUCs individuais para cada classe, pois essas métricas podem fornecer insights valiosos sobre como o modelo está se saindo em relação a cada classe específica.
# O AUC micro é uma métrica que leva em consideração o desempenho global do classificador em relação a todas as classes, agregando as estatísticas de desempenho de todas as classes em uma única métrica.

# from sklearn.metrics import roc_curve
# import matplotlib.pyplot as plt

# def plotCurveROC(class_id):
#   # Calcule a curva ROC
#   fpr, tpr, _ = roc_curve(y_test_class_bin[:, class_id], y_test_class_predict_bin[:, class_id])

#   # Plote a curva ROC
#   plt.figure()
#   plt.plot(fpr, tpr, color='darkorange', lw=2, label=f"Classe {class_id} vs o restante")
#   plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
#   plt.xlim([0.0, 1.0])
#   plt.ylim([0.0, 1.05])
#   plt.xlabel('Taxa de falsos positivos')
#   plt.ylabel('Taxa de verdadeirospositivos')
#   plt.title(f'ROC Curve for Class {class_id}')
#   plt.legend(loc='lower right')
#   plt.show()

# plotCurveROC(0)
# plotCurveROC(1)
# plotCurveROC(2)

output_file.close()



# Calcular e imprimir as métricas de regressão
# mse = mean_squared_error(y_val, y_val_predict_results)
# rmse = np.sqrt(mse)
# mae = mean_absolute_error(y_val, y_val_predict_results)
# r2 = r2_score(y_val, y_val_predict_results)
# mape = np.mean(np.abs((y_val - y_val_predict_results) / y_val)) * 100

# y_val_predict.shape
# (303, 30, 1)
# 303: This is the number of data points or samples in your validation dataset. Each data point represents one day.
# 30: These are the time steps or sequence length used for making predictions. In your LSTM model, you are considering a sequence of 30 time steps to predict the next value.
# 1: This is the number of features being predicted. In your case, you are predicting the closing price of Bitcoin, which is a single numerical value.

# # Código para mais de uma camada de LSTM
# def build_multilayer_lstm_model(hp):
#   model = keras.Sequential()
#   for _ in range(hp.Int('num_lstm_layers', min_value=1, max_value=4)):
#       model.add(LSTM(
#           units=hp.Int('num_lstm_units', min_value=16, max_value=128, step=16),
#           return_sequences=True,
#           input_shape = (x_train.shape[1], x_train.shape[2]),
#           activation='relu'
#           ))
#       model.add(Dropout(hp.Float('dropout_rate', min_value=0.2, max_value=0.4)))
#   model.add(Dense(1))

#   optimizer = Adam(learning_rate=hp.Float('learning_rate', min_value=0.001, max_value=0.1, sampling='log'))
#   model.compile(loss='mean_squared_error', optimizer=optimizer)

#   return model