# InvestBot: um bot para classificação de ações da bolsa de valores mediante técnicas de mineração de dados

<p align='center'>
    <img src='img/bot.jpg'>
</p>

# 1. Problema

Atualmente, muitos investidores se arriscam na bolsa de valores sem qualquer conhecimento sobre o mercado, renda variável, ou até mesmo sobre a própria empresa em que estão investindo, e por consequência, acabam perdendo o seu dinheiro. Adicionalmente, devido à alta volatilidade dos papéis e à instabilidade econômica e política brasileira, o mercado de ações se torna ainda mais traiçoeiro. Por este motivo, o objetivo deste trabalho é criar uma ferramenta que possa apoiar a decisão dos investidores.

# 2. Solução Proposta

Para solucionar o problema, será criado um bot no Telegram que é capaz de classificar as ações da bolsa de valores como confiáveis ou não confiáveis para investir. Para tal fim, as ações serão rotuladas com base no seguinte critério: se a ação render 3% ou mais até o próximo trimestre, será classificada como confiável, caso contrário, não confiável. Como o propósito do trabalho é ajudar os investidores a realizarem bons investimentos e, principalmente, não perderem dinheiro, foi usado esse valor de valorização pois além de dar uma margem de garantia que a ação irá valorizar, também faz com que as ações ditas confiáveis rendam de forma similar ao índice ibovespa, que historicamente rendeu 12% ao ano.

# 3. Estratégia de Solução:

- **Etapa 01. Coleta dos dados:** Serão coletados dados de balanço patrimonial e demonstrativos de resultados das empresas listadas na B3 (bolsa de valores brasileira), do período de junho de 2011 a setembro de 2021.
- **Etapa 02. Descrição dos Dados:** Em seguida, serão utilizadas algumas técnicas estatísticas para identificar dados irrelevantes, discrepantes, faltantes ou que estejam fora do escopo do trabalho. Esta etapa é importante para descobrir o quão desafiador é o problema.
- **Etapa 03. Feature Engineering:** Além dos dados coletados, serão 
- **Etapa 04. Filtragem dos Dados:**
- **Etapa 05. Análise Exploratória dos Dados:**
- **Etapa 06. Preparação dos Dados:**
- **Etapa 07. Seleção de Variáveis:**
- **Etapa 08. Machine Learning Modelling:**
- **Etapa 09. Hyperparameter Fine Tuning:**
- **Etapa 10. Machine Learning Performance:**
- **Etapa 11. Deploy Model to Production:**
- **Etapa 12. Criação do Telegram Bot:**

# 3. Top 3 Data Insights

# 4. Machine Learning Model Aplied

# 5. Machine Learning Model Performance

# 6. Conclusions

# 7. Lessons Learned

# 8. Next Steps

1. Try to predict the yield for longer periods of time: semester, year, 5 years, 10 years, etc.
