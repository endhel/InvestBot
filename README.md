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
- **Etapa 06. Preparação dos Dados:** Preparação dos dados, utilizando algumas técnicas de transformação, para que possam ser submetidos aos algoritmos de classificação.
- **Etapa 07. Seleção de Variáveis:** seleçao dos atributos mais relevantes para explicar o comportamento do fenômeno.
- **Etapa 08. Machine Learning Modelling:** treinamento dos modelos de machine learning.
- **Etapa 09. Hyperparameter Fine Tuning:** escolha dos valores que maximizam o aprendizado do modelo para cada um dos hiperparâmetros.
- **Etapa 10. Machine Learning Performance:** avaliação da performance do modelo.
- **Etapa 11. Deploy Model to Production:** publicação do modelo em um ambiente em nuvem, para que outras pessoas possam usar os resultados para realizarem melhores investimentos.
- **Etapa 12. Criação do Telegram Bot:** criação de um bot no aplicativo de mensagens Telegram, para consultar a previsão a qualquer momento (http://t.me/invest_quarter_bot). 

# 4. Modelos de Machine Learning aplicados



# 5. Performance dos Modelos de Machine Learning

# 6. Conclusão

# 7. Próximos Passos
