df = pd.DataFrame(data={'date': ['2021-2-20','2020-2-21', '2020-2-22'],
	'SPY': ['T','F','F'],
	'AAPL': ['F','F','T'],
	'GOOG': ['T','T','F']})
df.melt(id_vars=['date'], value_vars=['SPY','AAPL','GOOG'], value_name='forecast')