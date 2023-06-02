from pandas_datareader import data
from sklearn.cluster import KMeans

asset_tickers = ['SPY', 'TLT', 'AGG', 'EMB', 'ACWI', 'IWM', 'HYG', 'EFA', 'EEM', 'GOVT']
df_price = data.get_data_yahoo(asset_tickers, start='2012-03-01', end='2021-02-28')['Adj Close']
df_ret = np.log(df_price/df_price.shift(1)).dropna()

# cluster by ticker: stock vs bond
kmeans1 = KMeans(n_clusters=2, random_state=0).fit(df_ret.T)
print(kmeans1.labels_)  # [1, 0, 0, 0, 1, 1, 0, 1, 1, 0]

# cluster by date: positive vs negative returns
kmeans2 = KMeans(n_clusters=2, random_state=0).fit(df_ret)
print(kmeans2.labels_)  # [1, 1, 1, ..., 0, 1, 1]