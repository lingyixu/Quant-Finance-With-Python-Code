# use the dataframe in the melt example
df.set_index('date', inplace=True)
df.loc['2021-2-20']   # row access
df.loc[['2021-2-20']]   # subtable
df.loc[:,['SPY','AAPL']]   # subtable