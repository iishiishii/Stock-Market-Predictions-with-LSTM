import pandas as pd
import datetime as dt

api_key = 'U7C32IDVAVDT39ST'

    # American Airlines stock market prices
ticker = "AAL"

    # JSON file with all the stock market data for AAL from the last 20 years
url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)

    # Save data to this file
file_to_save = 'stock_market_data-%s.csv'%ticker
df = pd.read_csv(file_to_save)

df.sort_values('Date')
