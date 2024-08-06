# TCC-2023
Projeto de conclusão de curso do Bruno Couto Mariño na Universidade de Brasília (UNB).

## Descrição
Monografia apresentada como requisito para conclusão do Curso de Engenharia da Computação na UNB, com a orientadora Prof.a Dr.a Roberta Barbosa Oliveira.
Título: Análise da predição da tendência do preço do Bitcoin utilizando Long Short-Term Memory (LSTM) para as tarefas de regressão e classificação. 

O documento está disponível nos links abaixo:
- [Biblioteca Digital da UNB](https://bdm.unb.br/handle/10483/38449)
- [Monografia em PDF](./2023_BrunoCoutoMarino_tcc.pdf)

## Código
O código utilizado está disponível na pasta 'code' e é separado em 
[classificação](./code/tcc-classification-tunner-final.ipynb) e [regressão](./code/tcc-regression-tunner-final.ipynb).

## Meu Contato
Bruno Couto Mariño - 61981399964 - @brunocmarino

## Resumo da Proposta
Este trabalho propõe uma análise da predição da tendência do preço do Bitcoin
para as técnicas de regressão e de classificação utilizando o modelo Long Short-Term
Memory (LSTM). Também apresenta uma forma de comparar as técnicas, ao transformar
o valor encontrado pelo modelo de regressão em classes e analisar os resultados a partir
das métricas de desempenho de classificação. Para esse objetivo, são utilizados os preços
diários de abertura e de fechamento, máximo e mínimo diários e o volume de negociações
em dólares. A classificação utiliza três classes, que são definidas a partir de um limite
superior e inferior de variação percentual do preço; já a regressão utiliza o log base 10 do
preço de fechamento como alvo. Então, os resultados da regressão são transformados em
variação percentual e classificados de acordo com os limites de 3%, 5% e 7%. Assim é
possível analisar os resultados das métricas de classificação para o modelo de regressão.

## Resumo dos Resultados
O melhor cenário para o modelo de classificação apresentou janela de tempo de 15 dias, um
limite de 7% e previu a classe da tendência do preço para 1 dia no futuro. Ele obteve um
desempenho de 0,95789 para acurácia, precisão, revocação e f1-score; e um Area Under
the ROC Curve médio de 0,96842. Em relação ao modelo de regressão, o melhor cenário
utilizou janela de tempo de 30 dias, previu o log do preço para 1 dia no futuro. O modelo
alcançou um desempenho de 0,01274 para o Mean Absolute Error, 0,00027 para Mean
Squared Error, 0,01667 para Root Mean Squared Error, 0,28828% para Mean Absolute
Percentage Error e 0,98042 para o R2. Após transformar o resultado da regressão em
classes de acordo com a variação percentual predita, ele obteve um desempenho para um
limite de 7% de 0,94553 para acurácia, precisão, revocação e f1-score; e um Area Under
the ROC Curve médio de 0,95915. Ao comparar ambas as técnicas, a classificação se
mostrou mais assertiva.
