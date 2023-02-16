from nsepy import get_history
import pandas as pd
import numpy as np

# Collect stock data for a given stock
ticker = "SBIN"
df = get_history(symbol=ticker, start=pd.to_datetime('2010-01-01'), end=pd.to_datetime('2022-12-31'))

# Create a new column that indicates the day of the year (1-365)
df['day_of_year'] = df.index.dayofyear

# Create a new column that indicates the year
df['year'] = df.index.year

# Create a new DataFrame that contains the close price of each stock on each day of the year, grouped by year
comparedf = df.groupby(['day_of_year', 'year'])['Close'].mean().reset_index()

# Get the close price of the stock on the same day of the last year
last_year_close = comparedf[comparedf['year'] == 2022][comparedf['day_of_year'] == df.iloc[-1]['day_of_year']]['Close'].values[0]

# Calculate the difference between the close price of the stock on the same day of the last year and the recent close price
difference = df.iloc[-1]['Close'] - last_year_close

# Print the result
if difference > 0:
    print(f"{ticker} has performed better this year than the same
