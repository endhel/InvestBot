# InvestBot: a bot for stock classification using fundamentalist analysis

<p align='center'>
    <img src='img/bot.jpg'>
</p>

# 1. Problem

InvestBot is a decision support tool for investors. It consists of classifying stocks on the stock exchange as a reliable investment or not to buy at that particular time, based on the following criteria:

- if the stock price will yield 3% or more until the next quarter

That is, a stock will be classified as reliable if it yields 3% or more. If the stock depreciates, or yield less than 3%, it will be classified as unreliable. 

**An important question is: how will we predict if a stock will appreciate until the next quarter?**

Basically, we will use a very famous approach in the investment world: fundamental analysis. This technique aims to determine the intrinsic value of a company, and its growth potential. For this, it uses some data that are called fundamental indicators, and these can be found from the balance sheet and income statement of companies.

With the data from the indicators collected, and the classes of stocks already defined, following the criteria explained above, some classification models will be trained, in order that they can predict whether a stock will appreciate more than 3% until the next quarter.

However, a doubt may arise: **fundamental analysis is used for medium and long-term investments, so is it possible to analyze the data of fundamental indicators to determine if a stock will appreciate until the next quarter? Well, that's what we'll find out at the end of this work.** As the fundamental analysis makes it possible to discover the real value of a stock, it may be possible from it to determine whether a stock will appreciate in value until the next quarter.

**The main objective here is to build a tool that supports investors' decision making for short-term investments, helping him to determine whether an action is reliable to buy at any given time.**

In the next sections, each of the steps necessary for us to reach the desired result will be developed.

# 2. Solution Strategy

To solve the problem, we will follow these steps:

- **0.0.** Data Collection.
- **1.0.** Data Description.
- **2.0.** Feature Engineering
- **3.0.** Data Filtering
- **4.0.** Exploratory Data Analysis
- **5.0.** Data Preparation
- **6.0.** Feature Selection
- **7.0.** Machine Learning Modelling
- **8.0.** Hyperparameter Fine Tuning
- **9.0.** Machine Learning Performance
- **10.0.** Deploy Model to Production

# 3. Top 3 Data Insights

# 4. Machine Learning Model Aplied

# 5. Machine Learning Model Performance

# 6. Conclusions

# 7. Lessons Learned

# 8. Next Steps

1. Try to predict the yield for longer periods of time: semester, year, 5 years, 10 years, etc.
