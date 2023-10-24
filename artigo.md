### Título
    Previsão de Tendência do preço do Bitcoin utilizando LSTM 

### Sumário
    1. Introdução
       1. Contextualização do Problema
       2. Objetivo do projeto
       3. Estrutura do documento
    2. Fundamentação Teórica
       1. Conceitos do mercado financeiro
          - Gráfico de Velas
          - Indicadores Técnicos
          - Indicadores Macroeconômicos
       2. Conceitos da rede Bitcoin
          1. Indicadores da rede Bitcoin
       3. Machine Learning e Deep Learning
       4. LSTM e DeepLearning
       5. Métricas de Avaliação de Desempenho
    3. Revisão de Literatura
       - Um modelo de Rede Neural de classificação para predição da tendência do preço Bitcoin
        
    4. Metodologia
       1. Formato dos Dados
       2. Normalização
       3. Janela de Observação (*timesteps*)
       4. Valor/Dia/momento? predito
       5. Épocas
       6. Experimentos realizados
          1. la
          2. la
          3. la
       7. Avaliação dos Modelos
    5. Resultados
       1. Ferramentas Utilizadas
       2. Experimentos realizados
          1. la
          2. la
          3. la
    6. Conclusão e Trabalhos Futuros

> 



### Fundamentação Teórica

#### Um modelo de Rede Neural de classificação para predição da tendência do preço Bitcoin
    Utilizou o modelo LSTM para classificar se o valor do Bitcoin subiu ou caiu, através de uma análise do histórico de preço semanal e do volume de negociações. Usou apenas 418 valores, referentes às semanas.

    O artigo variou a janela de observação (*timesteps*) e as épocas (*epochs*). Também analisou a utilização de dados macroeconômicos junto ao modelo, porém gerou uma acurácia menor (51,82%), se comparada à utilização apenas dos dados históricos do bitcoin (52,9%)

    Gerou um retorno sobre o investimento, caso comprasse ou vendesse o bitcoin de acordo com o modelo criado, e métricas de acurácia. Comparou os resultados à algumas estratégias de negociação de ativos. Seu modelo apenas com os dados do bitcoin, atingiu uma acurácia de 52,9% e um retorno sobre o investimento de 122,82%.


#### Stock Market Forecasting with Different Input Indicators using Machine Learning and Deep Learning Techniques: A Review

    Realizou um estudo sobre 50 artigos publicados entre Jan-2018 to Dec-2021 que utilizam machine learning e deep learning para previsão do mercado de ações. Foram levados em consideração preços históricos, indicadores técnicos e fundamentalistas, análise de sentimentos e outros fatores.

    O artigo conclui que a literatura mostra que os modelos de aprendizagem profunda (LSTM, CNN, etc.) são os mais populares. SVM é a segunda abordagem mais popular. Também ressalta que a hibridização de mais de um método é a tendência recente para aproveitar os benefícios de cada um. As técnicas de otimização também estão em alta junto com as abordagens tradicionais de aprendizado de máquina

    Os autores concluem que, em relação às métricas de desenpenho MSE, RMSE, MAE, MAPE, Acurácia, precisão, recall e F-score são as as mais populares. Para problemas de regressão (previsão do preço das ações) são mais utilizados MSE, RMSE, MAE e MAPE; enquanto para problemas de classificação (predição da tendência das ações ), Acurácia, Precisão, Recall e F-score são considerados
    MSE, RMSE, MAE, MAPE, Acurácia, precisão, recall e F-score são as medidas de desempenho mais populares. 

#### An Empirical Study on Modeling and Prediction of Bitcoin Prices With Bayesian Neural Networks Based on Blockchain Information

    O Artigo seleciona as mais relevantes features da blockchain do bitcoin e as utiliza para treinar um modelo de predição do preço de negociação do ativo

### Ler depois 
https://medium.com/analytics-vidhya/predicting-bitcoin-prices-with-lstm-19e578d389c4


\section{Sumário}
    \renewcommand{\labelenumii}{\arabic{enumi}.\arabic{enumii}}
    \renewcommand{\labelenumiii}{\arabic{enumi}.\arabic{enumii}.\arabic{enumiii}}
    \renewcommand{\labelenumiv}{\arabic{enumi}.\arabic{enumii}.\arabic{enumiii}.\arabic{enumiv}}
    
    \begin{enumerate}
    \item Introdução
        \begin{enumerate}
        \item Contextualização do Problema
        \item Objetivo do projeto
        \item Estrutura do documento
        \end{enumerate}
    
    \item Fundamentação Teórica
        \begin{enumerate}
        \item Conceitos do mercado financeiro
            \begin{enumerate}
            \item Gráfico de Velas
            \item Indicadores Técnicos
            \item Indicadores Macroeconômicos
            \end{enumerate}
        \item Conceitos da rede Bitcoin
            \begin{enumerate}
            \item Indicadores da rede Bitcoin
            \end{enumerate}
        \end{enumerate}
    \item Revisão de Literatura
        \begin{enumerate}
        \item Um modelo de Rede Neural de classificação para predição da tendência do preço Bitcoin
        \end{enumerate}
    \item Metodologia
        \begin{enumerate}
        \item Arquitetura do modelo proposto
            \begin{enumerate}
            \item Formato dos Dados
            \item Normalização
            \item Janela de Observação (\emph{timesteps})
            \item Valor/Dia/momento? predito
            \item Épocas
            \item Experimentos realizados
                \begin{enumerate}
                \item la
                \item la
                \item la
                \end{enumerate}
            \end{enumerate}
        \item Avaliação dos Modelos
        \end{enumerate}
 \item Resultados
         \begin{enumerate}
         \item Ferramentas Utilizadas
         \item Experimentos realizados
            \begin{enumerate}
            \item la
            \item la
            \item la
            \end{enumerate}
        \end{enumerate}
 \item Conclusão e Trabalhos Futuros