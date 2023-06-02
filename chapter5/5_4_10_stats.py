df = pd.DataFrame(data=np.random.random(size=(5,3)),
                  index=['2009','2010','2011','2012','2013'],
                  columns=['SPY','AAPL','GOOG'])
print(df.mean())
print(df.std())
print(df.min())
print(df.shift(periods=2, fill_value=))
print(df.rolling(3).mean())
