from pandas_datareader import data
df_aapl = data.get_data_yahoo('AAPL', start='2020-03-01', end='2021-02-28')