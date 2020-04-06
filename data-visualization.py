import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

api_key = 'U7C32IDVAVDT39ST'

    # American Airlines stock market prices
ticker = "AAL"

    # JSON file with all the stock market data for AAL from the last 20 years
url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)

    # Save data to this file
file_to_save = 'stock_market_data-%s.csv'%ticker
df = pd.read_csv(file_to_save)


plt.figure(figsize = (18,9))
plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
plt.xticks(range(0,df.shape[0],200),df['Date'].loc[::200],rotation=45)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Mid Price',fontsize=18)
plt.show()
