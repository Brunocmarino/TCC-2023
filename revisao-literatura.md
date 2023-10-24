# Revisão de Literatura
Título | Autores | Ano | Objetivo | Base de Dados | Informações da Base | Metodologias Propostas | Métricas e Resultados | Pontos Positivos | Pontos Negativos | Link 

## Forecasting Bitcoin with technical analysis: A not-so-random forest?

> Referências interessantes na introdução e conclusão da introdução
>
> Quebrou a análise em subsamples, de acordo com o ciclos do bitcoin
>
> Mostrou uma tabela com a importância das features escolhidas

 - **Autores**
    Nikola Gradojevic, Dragan Kukolj , Robert Adcock , Vladimir Djakovic
 - **Ano**
    2023
 - **Objetivo**
    Exercício empírico robusto para observar o impacto do horizonte de previsão, tipo de modelo, período de tempo e a escolha de features no desempenho da previsão do preço do bitcoin
 - **Base de Dados**
    Bloomberg Terminal and
use the hourly and daily sampling frequency for the BTC/USD. May 11, 2015 to March 7, 2019, excluding weekends. Uses natural log difference between hours
 - **Informações da Base**
  
 - **Metodologias Propostas**
  
    Modelos: ANN, FD-D-ANN, SVM, RF
    Indicadores: MA, ROC, RSI, WLPR, OBV, FG

 - **Métricas e Resultados**
 - **Pontos Positivos**
 - **Pontos Negativos**
 - **Link**

## Stock Market Forecasting with Different Input  Indicators using Machine Learning and Deep Learning Techniques: A Review
> Mostra que modelos de Deep Learning são os mais populares - LSTM, CNN, etc.
> SVM é o segundo mais popular
>
> Muitos utilizam modelos hibridos, para pegar benefícios de modelos diferentes
>
> Os modelos de Deep Learning são promissores para previsão financeira. Incorporar otimizações dos métodos e módulos de Deep Learning podem melhorar modelagem preditiva.
> 
> "The literature shows that deep learning  models  (LSTM,  CNN,  etc.)  are  the  most  popular ones. SVM is the second most popular approach. Hybridization of more than one method is the recent trend to grab the benefits of different methods. Optimization techniques  are  also  trending  along  with  traditional  machine learning approaches"
>MSE,  RMSE,  MAE,  MAPE, Accuracy, Precision, Recall, and F-score is the popular performance measures. MSE, RMSE, MAE, and MAPE are considered for regression problems (stock price  prediction), whereas Accuracy, Precision, Recall, and F-score are considered for classification problems (stock trend rediction).

 - **Autores**
 - **Ano**
 - **Objetivo**
 - **Base de Dados**
 - **Informações da Base**
 - **Metodologias Propostas**
 - **Métricas e Resultados**
 - **Pontos Positivos**
 - **Pontos Negativos**
 - **Link**

## Um modelo de Rede Neural de classificação para predição da tendência do preço Bitcoin

> Usou poucos dados, apenas 418;
> Usou apenas treino e teste (334, 84);
> Utilizou apenas dados do candlestick;
> Acurácia média de 52,90%, sendo que classificou em 0, 1;
> Gostei da análise de ROI de btc + bolsa, btc + commodities e estratégias de trading com análise técnica

 - **Autores**
    Autor Rodolfo Helfenstein
    Orientador Renata de Matos Galante
 - **Ano**
   Trabalho de conclusão de graduação 
    Porto Alegre, 2022
 - **Objetivo**
    É proposto um modelo de rede neural de classificação utilizando células LSTM para predição da tendência no preço do Bitcoin utilizando como base de dados os valores do candlestick semanal junto com o volume de transação
 - **Base de Dados**
    Yahoo e coinmarketcap

 - **Informações da Base**
    Datas de 15 de setembro de 2014 até dia 15 de setembro de 2022. A periodicidade escolhida foi o semanal, totalizando 418 registros.

 - **Metodologias Propostas**
 - **Métricas e Resultados**
 - **Pontos Positivos**
 - **Pontos Negativos**
 - **Link**
   http://hdl.handle.net/10183/254876

## An Empirical Study on Modeling and Prediction of Bitcoin Prices With Bayesian Neural Networks Based on Blockchain Information
> Usaram cross-validation e não consideraram que bootstrap era uma boa abordagem
> CrossValidation 10-fold
> Porque usar log: We use logscaled values of both output response variables to account for the large difference between Bitcoin value in the early period and its most recent value.
> Definição de Benchmark: SVR e regressão Linear
> Tem Feature selection
> Tem Rollover Framework 
> Tem Cross-Validation, 10-fold

 - **Autores**
   HUISU JANG AND JAEWOOK LEE
 - **Ano**
   2017
 - **Objetivo**
   Utilizar um modelo de BNN para prever o preço do Bitcoin com a utilização de dados atualizados de preço (até 2017), dados macroeconômicos e dados da blockchain do Bitcoin, relativos à sua oferta e demanda.
 - **Base de Dados**
   https://bitcoincharts.com/markets/
   https://blockchain.info/
   
 - **Informações da Base**
   Average block size (MB)
   Transactions per block
   Median confirmation timeandrecorded to the ledger.
   Hash rate 
   Difficulty
   Cost % of a transaction
   Miners revenue
   Confirmed transaction
   Total number of a unique Bitcoin

   Taxa de câmbio das seguintes moedas: GBP, JPY, CHF, CNY, EUR
 - **Metodologias Propostas**
   Utilizou BNN e um método de Rollover que eu não entendi

   Análise de regressão linear: analisou a correlação linear das features com o preço do bitcoin e perceberam que quase todas não eram significativas.
   Em seguida fizeram uma análise de multicolinearidade. Analisou o Vif das features e selecionou as adequadas para construir o modelo

   Criou dois modelos lineares para prever o preço e a volatividade do BTC

   BNN foi treinado com os dados do preço, da blockchain e macroeconomia. 25 features
   benchmark foi uma regressão linear e o modelo SVR
   Rodou os modelos com 25 e 16 features, sendo 16 as que foram selecionadas como as mais importantes

 - **Métricas e Resultados**
   O modelo BNN foi melhor que os outros em RMSE e  MAPE para prever o Log do preço e Log da Volatividade

   Conclui que o modelo BNN foi melhor que os outros analisados e que a seleção das features teve impacto positivo
 - **Pontos Positivos**
 - **Pontos Negativos**
 - **Link**


