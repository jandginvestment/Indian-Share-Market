from nsepy import get_history
import pandas as pd
import numpy as np

# Collect stock data for a given stock
ticker = "SBIN"
df = get_history(symbol=ticker, start=pd.to_datetime('2010-01-01'), end=pd.to_datetime('2022-12-31'))

df['Date'] = pd.to_datetime(df.index)

# Create a new column that indicates the day of the year (1-365)
df['day_of_year'] = df['Date'].dt.dayofyear

# Create a new column that indicates the year
df['year'] = df['Date'].dt.year

df['running_index'] = df.groupby('year').cumcount()
df['weekday'] = df['Date'].dt.day_name()

# Create a new DataFrame that contains the close price of each stock on each day of the year, grouped by year
comparedf = df.groupby(['running_index', 'year'])['Close'].mean().reset_index()

comparedf = comparedf[comparedf['running_index'] < 242]

# Get the close price of the stock on the same day of the last year
if not df.empty:
    if not comparedf.empty:
        last_year_close = comparedf[comparedf['year'] == 2022][comparedf['running_index'] == df.iloc[-1]['running_index']]['Close'].values[0]

# Calculate the difference between the close price of the stock on the same day of the last year and the recent close price
        difference = df.iloc[-1]['Close'] - last_year_close

# Print the result
        if difference > 0:
            print(f"{ticker} has performed better this year than the same")
