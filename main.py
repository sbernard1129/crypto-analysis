import pandas as pd

portfolio_dict={}  # this could be a dict or a list. 

while True:
    tickers = input("Please enter a ticker symbol. Make an empty entry when finished: ")

    try:
        #Check if a blank was entered. If so, end the disctionary creation.
        if tickers == '':
            break

        #do some data validation.       
        #do something with the API here to get the data
        #add the response data to the portfolio dictionary
        portfolio_dict[tickers] = "some api data"

    except:
        pass

#Now turn the dicct into a data frame so we can pass it to functions that do our plots and stuff.
portfolio_df = pd.DataFrame.from_dict(portfolio_dict, orient='index')

# show the data frame
print(f"This is the port: {portfolio_df}")
    

