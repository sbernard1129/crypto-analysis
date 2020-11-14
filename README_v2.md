# Crypto Portfolio Analysis - Phase I Project
By: Chris Larson, Farah Awad, Stephen Bernard, Cathy Slider

*November 15, 2020*
<br></br>

## Overview and Project Background
In the past five years, cryptocurrencies have multiplied exponentially in the digital currency space. 
A few years ago there were less than 500 different cryptocurrencies traded. Today, there are nearly 2000.

While there are tools to measure individual currency performance, there has never been a resource to analyze 
a full crypto portfolio. The project seeks to establish the fundamental components – dataframe, function call, and 
visual experience – as well as the market data to provide a real-world portfolio analysis.
<br></br>

## Project Focus
The primary questions put forth by the project are as follows:
1. What would the data reveal when comparing cryptocurrencies and other market indices?

2. Could a user of this dashboard learn the following?:
* What is the risk level of my portfolio?
* How are my portfolio assets correlated?
* How are my assets performing relative to other assets, including benchmarks?
* How can I construct a low/medium/high risk portfolio?
* What and how do we define a low/medium/high risk portfolio?
<br></br>

For all of these questions, reliable and clean data were critical. The project analyzed both five year historical and real-time data.
<br></br>

## Data Cleanup and Exploration
The group consensus was to pull real-time market data from a reliable source, and we decided on CoinGecko for this. Their operation began in 2014, and they have become one of the largest crypto data aggregators. Their API is easily accessible and robust. We opted to utilize a software development kit via a different API to pull in the CoinGecko data. Since Alpaca was down, we used Google Finance to pull data for the S&P 500, gold, and the 20yr U.S. Treasury prices.

In working with our vision and the wireframe we developed to layout the dashboard, we had a good sense of what we needed for the project. Wrangling the data from these sites and creating the dataframes was mostly straightforward. The biggest challenge was interpreting the UNIX dates into more workable dates for our analysis purposes. We relied on Google to help us resolve this issue. We ultimately created several .csv files to work with for developing our notebook.

It was interesting to see how CoinGecko tracked social media instances of the individual cryptocurrencies. We agreed that this information is relevant to a portfolio analysis and that it would become more relevant and complete over time as more data is generated.
<br></br>
!alt[text](/image/social_media.png)

## Data Analysis
The project successfully answered the majority of the user questions as follows:
<br></br>
1) What is the risk level of my portfolio?
!alt[text](Images/rolling_beta.png)
!alt[text](Images/stand_dev.png)
!alt[text](/Images/sharpe.png)
<br></br>
2) How are my assets correlated?
!alt[text](/Images/correlation.png)
<br></br>
3) How is my crypto performing relative to other benchmarks?
!alt[text](Images/market_cap.png)
!alt[text](/Images/cumul_returns.png)
!alt[text](/Images/sum_cumul_returns.png)
!alt[text](Images/violin.png)
<br></br>

The following questions will become part of the next phase of the project due to the charting complexities it will resolve:
 
* What and how do we define a low/medium/high risk portfolio?
* How can I construct a low/medium/high risk portfolio?
<br></br>

## Findings and Conclusion
Although the complexity of evaluating this data was challenging due to the infancy of the crypto space, the overall results of the project were positive and encouraging.

* A real-time cryptocurrency portfolio analysis is possible and worthwhile.
* We have the ability to measure performance.
* We know how crypto assets are correlated to each other and to other assets.
* The data provided unexpected results and proves the value of visualizations in the analysis process.
* In the future, tracking daily changes in social media metrics may provide a leading indicator in cryptocurrency performance.
!alt[text}(/Images/social_media.png)]
<br></br>

## Challenges
1) Streamlining the datetime index out of the UNIX values that came through the API. 
* This was resolved by ________________________________. Visual display of code??

2) Incorporating the level of user interactivity that we initially sought.
* This was resolved by ________________________________. Visual display of code??

3) If the project was extended by two weeks, our team would:
* Perfect the visualization and incorporate more interactivity
* Develop the user experience to include cryptocurrency selections and establishing risk tolerances
<br></br>

Concluding statement??




