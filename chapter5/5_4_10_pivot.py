df = pd.DataFrame(data={'date': ['2021-2-20']*3 + ['2021-2-21']*3,
	'stock': ['SPY','AAPL','GOOG']*2,
	'forecast1': ['T','F','F','T','T','T'],
	'forecast2': ['F','F','T','T','F','T'],
	'forecast3': ['T','T','F','F','T','F']})

# make a pivot table
df.pivot(index='date', columns='stock', values='forecast1')

# make a pivot table with hierarchical columns (multiple values)
df.pivot(index='date', columns='stock', values=['forecast2','forecast3'])