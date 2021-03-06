# InvestBot: um bot para classificação de ações da bolsa de valores mediante técnicas de mineração de dados

<p align='center'>
    <img src='img/bot.jpg'>
</p>

# 1. Problema

Atualmente, muitos investidores se arriscam na bolsa de valores sem qualquer conhecimento sobre o mercado, renda variável, ou até mesmo sobre a própria empresa em que estão investindo, e por consequência, acabam perdendo o seu dinheiro. Adicionalmente, devido à alta volatilidade dos papéis e à instabilidade econômica e política brasileira, o mercado de ações se torna ainda mais traiçoeiro. Por este motivo, o objetivo deste trabalho é criar uma ferramenta que possa apoiar a decisão dos investidores.

# 2. Solução Proposta

Para solucionar o problema, será criado um bot no Telegram que é capaz de classificar as ações da bolsa de valores como confiáveis ou não confiáveis para investir. Para tal fim, as ações serão rotuladas com base no seguinte critério: se a ação render 3% ou mais até o próximo trimestre, será classificada como confiável, caso contrário, não confiável. Como o propósito do trabalho é ajudar os investidores a realizarem bons investimentos e, principalmente, não perderem dinheiro, foi usado esse valor de valorização pois além de dar uma margem de garantia que a ação irá valorizar, também faz com que as ações ditas confiáveis rendam de forma similar ao índice ibovespa, que historicamente rendeu 12% ao ano.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Para acessar o bot do modelo no telegram, clique abaixo:

[<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](http://t.me/invest_quarter_bot)

# 3. Estratégia de Solução:

- **Etapa 01. Coleta dos dados:** coleta dos dados de balanço patrimonial e demonstrativos de resultados das empresas listadas na B3 (bolsa de valores brasileira), do período de junho de 2011 a setembro de 2021.
- **Etapa 02. Descrição dos Dados:** uso de algumas técnicas estatísticas para identificar dados irrelevantes, discrepantes, faltantes ou que estejam fora do escopo do trabalho. Esta etapa é importante para descobrir o quão desafiador é o problema.
- **Etapa 03. Feature Engineering:** criação de novas variáveis que ajudem a explicar o fenômeno observado. Como o objetivo é prever a valorização das ações no futuro, serão calculados alguns indicadores fundamentalistas das empresas, pois com eles é possível antecipar o comportamento futuro dos papéis, com base nos balanços e resultados das empresas.
- **Etapa 04. Filtragem dos Dados:** antes de realizar a análise exploratória dos dados, é preciso filtrar algumas linhas e colunas que não serão mais necessárias para o restante do trabalho.
- **Etapa 05. Análise Exploratória dos Dados:** exploração dos dados, a fim de entender melhor o impacto das variáveis preditoras na variável resposta.
- **Etapa 06. Preparação dos Dados:** Preparação dos dados, utilizando algumas técnicas de transformação, para que os dados possam ser submetidos aos algoritmos de classificação.
- **Etapa 07. Seleção de Variáveis:** seleção dos atributos mais relevantes para explicar o comportamento do fenômeno.
- **Etapa 08. Machine Learning Modelling:** treinamento dos modelos de machine learning.
- **Etapa 09. Hyperparameter Fine Tuning:** escolha dos valores que maximizam o aprendizado do modelo para cada um dos hiperparâmetros.
- **Etapa 10. Machine Learning Performance:** avaliação da performance do modelo.
- **Etapa 11. Deploy Model to Production:** publicação do modelo em um ambiente em nuvem, para que outras pessoas possam usar os resultados para realizarem melhores investimentos.
- **Etapa 12. Criação do Telegram Bot:** criação de um bot no aplicativo de mensagens Telegram, para consultar a previsão a qualquer momento (http://t.me/invest_quarter_bot). 

# 4. Modelos de Machine Learning aplicados

Os testes foram realizados usando os seguintes algoritmos:

**Dummy Classifier**

**Logistic Regression**

**Decision Tree**

**K-Nearest Neighbors**

**Naive Bayes**

**Multilayer Perceptron**

**Random Forest**

# 5. Performance dos Modelos de Machine Learning

**Os valores de Precisão, Recall e F1-score são referentes à classe "confiável"**.

**Hold-out** 

| Nome do Modelo | Acurácia | Precisão    | Recall  | F1-score |
|-----------|---------|-----------|---------|---------|
|  Dummy Classifier  | 0.50 | 0.40 | 0.40  | 0.40 |
|  Logistic Regression	| 0.59 | 0.86 | 0.00   | 0.01 |
|  Decision Tree  | 0.58 | 0.49 | 0.51   | 0.50 |
|  K-Nearest Neighbors  | 0.58 | 0.50 | 0.44  | 0.46 |
|  Naive Bayes | 0.42 | 0.42 | 0.99  | 0.59 |
|  Multilayer Perceptron | 0.57 | 0.47 | 0.26 | 0.33 |
|  Random Forest | 0.64 | 0.59 | 0.43 | 0.50 |

**Performance Real - Cross Validation**

| Nome do Modelo | Acurácia | Precisão | Recall  | F1-score |
|-----------|---------|-----------|---------|---------|
|  Dummy Classifier | 0.52 | 0.42 | 0.41   | 0.41 |
|  Logistic Regression	| 0.58 | 0.37 | 0.00   | 0.01 |
|  Decision Tree  | 0.58 | 0.49 | 0.50   | 0.50 |
|  K-Nearest Neighbors  | 0.58 | 0.49 | 0.43  | 0.46 |
|  Naive Bayes | 0.48 | 0.37 | 0.59  | 0.36 |
|  Multilayer Perceptron | 0.59 | 0.50 | 0.24 | 0.32 |
|  Random Forest | 0.64 | 0.60 | 0.42 | 0.49 |

O modelo de Random Forest obteve a melhor performance, tendo alcançado 60% de precisão para classificar ações "confiáveis", logo foi o algoritmo escolhido para ser utilizado na etapa de Hyperparameter Fine Tuning.

**Performance Final - Hyperparameter Fine Tunning Cross Validation**:

Após encontrar os melhores parâmetros para o modelo através do metódo Random Search, as métricas finais para o modelo foram as seguintes:

| Nome do Modelo | Acurácia | Precisão | Recall  | F1-score |
|-----------|---------|-----------|---------|---------|
|  Random Forest | 0.64 | 0.61 | 0.39   | 0.47 |

# 6. Conclusão

O objetivo principal do trabalho foi alcançado, uma vez que através do modelo criado, utilizando o algoritmo Random Forest, foi possível classificar ações como confiáveis ou não para se investir com 60% de precisão. Além disso, os objetivos específicos também foram alcançados, sendo criado um bot no Telegram, que com o uso do modelo, apoiasse a tomada de decisão. Como conclusão, observou-se que a ferramenta construída é simples, acessível, fácil de usar, e fica como sugestão para auxiliar os investidores e apoiar a tomada de decisão.

# 7. Próximos Passos

Para trabalhos futuros, sugere-se encontrar mais variáveis dos dados, que possuem um maior impacto na variável resposta, a fim de aumentar a precisão do modelo para
classificar ações “confiáveis”. Ademais, também pode ser interessante aumentar o período de previsão do modelo para seis meses ou até um ano, pois assim poderá contribir com os investidores que visam o longo prazo. Por fim, pode-se aperfeiçoar o bot no Telegram, para que ele faça uma coleta automática dos dados atuais das empresas assim que o usuário enviar o código da ação.
