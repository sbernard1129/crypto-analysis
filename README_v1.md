# Crypto Portfolio Analysis - Phase I Project
By: Chris Larson, Farah Awad, Stephen Bernard, Cathy Slider

*November 15, 2020*
<br></br>

## Overview and Project Background
In the past five years, cryptocurrencies have multiplied exponentially in the digital currency space. 
According to _______(https:), there were ___ different cryptocurrencies traded. Today, there are over ___.

While there are tools to measure individual currency performance, there has never been a resource to analyze 
a full crypto portfolio. The project seeks to establish the fundamental components – dataframe, function call, and 
visual experience – as well as the market data to provide a real-world portfolio analysis. With its success, this 
project will lay the foundation for Phase II - a more interactive and crypto-specific experience for the user - and Phase III – the development of a user interface for deploying the model to the web and web3 spaces.
<br></br>

## Project Focus
The primary questions put forth by the project are as follows:

1. Will the dataframe structure support real-world analysis?
2. How much interactivity could the visualizations have?
3. Could the model support a full spectrum of crypto currency input options?
4. Could this model become the basic foundation on which to build a web-based user experience?

5. For the user experience, the following questions were considered:
    * Is my crypto portfolio low risk or high risk?
    * How are my portfolio assets correlated?
    * How can I construct a low/medium/high risk portfolio?
    * What and how do we define a conservative or aggressive portfolio?
    * How is my crypto performing to different benchmarks (S&P500/DowJones)
<br></br>

For all of these questions, reliable and clean data are critical. The project will analyze both five year historical and real-time data in this exploration.
<br></br>

## Data Cleanup and Exploration
The group consensus was to pull real-time market data from a reliable source, and we decided on CoinGecko as our source. Their operation began in 2014, and they have become one of the largest crypto data aggregators. Their API is easily accessible and robust. We opted to utilize a software development kit via a different API to pull in the CoinGecko data. Since Alpaca was down, we used Google Finance to pull data for the S&P 500, gold, and the 20yr U.S. Treasury prices.

In working with our vision and the wireframe we developed to layout the dashboard, we had a good sense of what we needed for the project. Wrangling the data from these sites and creating the dataframes was mostly straightforward. The biggest challenge was interpreting the UNIX dates into more workable dates for our analysis purposes. We relied on Google to help us resolve this issue. We ultimately created several .csv files to work with in developing our notebook.

It was interesting to see how CoinGecko tracked social media instances of the individual cryptocurrencies. We agreed that this information is relevant to a portfolio analysis and that it would become more complete over time as more data is generated.
<br></br>
!alt[text](/image/social_media.png)

## Data Analysis
Creating dataframes helped us to look at the data as it related to our crypto portfolio analysis goals. By working to group the collected data, we found that:

* The dataframe structure will support real-world analysis.

* The model will provide limited user interactivity in Phase I.

* However, Phase I will not allow for user input of their own crypto currencies due to the complexities of integrating widgets and tables with real-time data. (Will we be able to deliver this in Phase II? How?)

* Ultimately, the model provides a basis for developing Phases II and III as we became confident in the real-time data analysis between various cryptocurrencies and major market indices.

Regarding the user experience, the project successfully answered the following questions with the limitation that the cryptocurrencies analyzed are predetermined and not selectable in Phase I:

* Is my crypto portfolio low risk or high risk? !alt[text](/image/sharpe.png)
* How are my portfolio assets correlated? !alt[text](/image/correltion.png)
* How is my crypto performing to different benchmarks such as S&P 500/Dow? !alt[text](/image/cumul_return.png)
<br></br>

The following questions will become part of Phase II due to the charting complexities that project will resolve:

* How can I construct a low/medium/high risk portfolio?
* What and how do we define a conservative or aggressive portfolio?
<br></br>

## Findings
1. Five years of data is a long time in the cryptocurrency space, but data from this timeframe will be easier to manipulate going forward as more history is established. (Add supporting numerical data and/or visualization)

2. Other findings _______________________.

3. Other findings _______________________. 
<br></br>

## Conclusion
The project confirmed that a real-time cryptocurrency portfolio analysis is possible. As hypothesized, bringing in market data via a relaiable API yields the fundamental information from which we could construct dataframes and the visualization to demonstrate results. (Add supporting numerical data and/or visualization)

At the same time, the complexities of evaluating this data in a consistent manner is challenging due to the infancy of the crypto space. This is a consideration for Phases II and III.
<br></br>

## Challenges
1)	One of our challenges was selecting cryptocurrencies with five year historical data so that analysis and comparisons were meaningful and displayed accurately (ie: NaN rows affected numerical displays in the charts). Our initial selections were not all compatible in this regard. 

* We ultimately found currencies that were closer in time of existence historically. Through exponential aggregation, we defined mean values for the missing time period of those that did not have a full five years of history.


2)	As mentioned previously, it was initially difficult to streamline the datetime index out of the UNIX values that came through the API. 

* This was resolved by ________________________________. Visual display of code??


3)	Other challenges ______________________________.

* This was resolved by ___________________________.


4)	If the project was extended by two weeks, our team would focus on the following to improve Phase I and prepare to begin Phase II:

* Resolving conflicts with newer cryptocurrencies in the data analysis process

* Perfecting the visualization

* Developing the user experience to include cryptocurrency selections and establishing risk tolerances
<br></br>

### Concluding sentence or two.




