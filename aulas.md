## TTC-1 13/09/23
#### Apresentação TCC1
 - Definição do cronograma na proxima semana
 - Revisão de Literatura (crie dúvidas)
 - Correção do código (falar com o Gui)


## TTC-1 26/07/23
#### Apresentação TCC1
#### Observações a serem pesquisadas
 - Train Test Split - Estratificado em classificação com LSTM
 - Verificar o valor da loss
 - Gráfico da acurácia x época
 - Usar tabela pra mostrar resultados
 - CrossValidation
#### Férias
Começar a escrever a revisão de literatura 
Criar sumário



## TCC-1 14/06/23
#### Objetivo Geral
Entender quais dados de mercado têm maior impacto no preço do Bitcoin:
- Indicadores Técnicos
 - Valores de Preço anteriores
 - Valores da rede BTC
 - Dados Macroeconômicos (bolsa americana)
  
Analisar quais métodos de investimentos seriam melhor aplicados pelo período analisado (ROI)
- Buy and Hold
 - Médias Móveis
 - IFR
 - Aleatório
 - Outros....pesquisar
  
Utilizar Regressão e comprar com Classificação

#### Experimentos
Divisão da base
- 70, 10, 20 (treino, validação, teste)
Hiperparâmetros
- Definir quantidade de Épocas (earlyStop)
- Definir otimizadores
- usar gridSearch, RandomSearch
- Definir Loss
- Definir activation
- Definir outros hiperparâmetros
- Definir a normalização dos dados
- Analisar balanceamento entre classes
- Métricas para Problemas Multiclass
   - Considerar Matriz de Confusão, acurácia, precisão, recall e f1score
#### Experimento 1
- Classificação apenas utilizando indicadores de Preço
- Variar diferentes Threshold
#### Experimento 2
- Classificação apenas utilizando Indicadores Técnicos
#### Experimento 3
 - Classificação apenas utilizando Valores da rede BTC
#### Experimento 4
 - Classificação apenas utilizando Dados Macroeconômicos (bolsa americana)
#### Experimento 5
 - Classificação apenas utilizando todos os indicadores 
 - Analisar com feature selection os mais importantes (Filter, Wrapper, Embedded, outra)
#### Experimento 6
- Utilizar Regressão e depois formar as Classes a partir do valor previsto

## TCC-1 31/05/23

#### O que foi feito?
Leitura de 2 artigos 
- Um modelo de Rede Neural de classificação
- Usou teste e treino
- Usou semanal
- Usou 0, 1, subiu caiu
- Variou Timesteps
- Variou as Épocas
- Adição de features Mercado Financeiro
- Não Adicionou de dados da rede do BTC
- Comparou o modelo à outras estrategias de compra de ativos
#### A fazer
Escrever os Experimentos que devem ser feitos
Aprender a usar o LSTM (foco)
Escrever um esboço da proposta


## TCC-1 19/04/23
 - o dividir os dados em Treino e Teste, como devo fazer? Sequencial, Aleatório, por classe?
 - Alterar o time_step 
 - LSTM: Adicionar camadas, épocas utilizadas
 - Entender como o RMSE funciona


## TCC-1 05/04/23

#### 19/04/23
- Ler Artigos aplicados à Bitcoin e de Regressão e Classificação
Implementação do modelo usando a base de dados escolhida e algoritmos de 
- Classificação (1 modelo tradicional e 1 Deep Learning )
- Apresentar os resultados considerando a matriz de confusão 
- Apresentar as métricas para Classificação mais utilizadas nos artigos (AUC, acurácia, sensibilidade, especificidade)
- Divisão da Base de forma estratificada (70-10-20)
- Classes: 
  - Subiu mais que X%
  - Caiu mais que X%
  - Ficou de lado
- Training and validation loss (gráfico)
- Analisar a quantidade de épocas (parada antecipada, early stoping)
- Verificar um algoritmo de avaliar hiperparâmetros (grid search, random search)
- ver:https://www.youtube.com/watch?v=foYDHKHB4Q4&feature=youtu.be

#### 03/05/23
- Ler Artigos aplicados à Bitcoin e de Regressão e Classificação
- Implementação do modelo usando a base de dados escolhida e algoritmos de - Regressão (1 modelo tradicional e 1 Deep Learning )
- Apresentar as métricas para Regressão mais utilizadas nos artigos (acurácia...)
- Divisão da Base de forma estratificada (70-10-20)
- Prever o dia seguinte, semana seguinte e o mês seguinte.
- Training and validation loss