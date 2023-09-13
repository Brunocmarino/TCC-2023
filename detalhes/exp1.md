
# **1 : regressao_1_lstm**

Variei a Quantidade de amostras: dia, mês e semana

Variei a janela de observação: 90, 60, 30, 15, 7 dias; 30 semanas

> **Modelo de ML usado** : LSTM <br>
> **Construção do Modelo** : 1 camada de 64 units <br>
> **Técnica de ML** : Regressão <br>
> **Features** : Open, High, Low, Close, Volume <br>
> **Valor Predito** : Ver Tabela <br>
> **Número de Amostras** : 3067 dias,  <br>
> **Threshold** : Não se aplica <br>
> **Window Size** : Ver tabela <br>
> **Função de Ativação** : relu <br>
> **Fução de Loss** : mean_squared_error <br>
> **Otimizador** : adam <br>
> **Épocas e earlystop** : 500, patience: 50 <br>
> **Loss e Loss/Épocas** : Gráfico criado <br>
> **Acurácia e Acurácia/Épocas** : Não se Aplica <br>
> **MAE e MAE/Épocas** : Gráfico criado <br>
> **Resultados e Métricas** : Ver tabela <br>
> **ROI** : Não fiz ainda
  
## 1.1: Amostras: 3067 dias, Window Size: 30 dias 
Resultados: <br>
MSE 1576426.91 <br>
RMSE 1255.55 <br>
MAE 931.27 <br>
R-squared 0.99
  
 ## 1.2: Amostras: 3067 dias, Window Size: 15 dias
Resultados: <br>
MSE 1340677.77 <br>
RMSE 1157.87 <br>
MAE 843.17 <br>
R-squared 0.99

## 1.3: Amostras: 3067 dias, Window Size: 7 dias 
Resultados: <br>
MSE 1249475.93 <br>
RMSE 1117.79 <br>
MAE 871.90 <br>
R-squared 0.99

## 1.4: Amostras: 3067 dias, Window Size: 60 dias 
Resultados: <br>
MSE 155824304.61 <br>
RMSE 12482.96 <br>
MAE 9410.36 <br>
R-squared 0.13

## 1.5: Amostras: 3067 dias, Window Size: 90 dias
Resultados: <br>
MSE 42173069.41 <br>
RMSE 6494.07 <br>
MAE 5020.14 <br>
R-squared 0.76

## 1.6: Amostras: 439 semanas, Window Size: 30 semanas
Resultados: <br>
MSE  <br>
RMSE  <br>
MAE  <br>
R-squared 
