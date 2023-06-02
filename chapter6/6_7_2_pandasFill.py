df = pd.DataFrame(data={'date': pd.date_range(start='2021-2-19', end='2021-2-26'),
	'price': [78, 73, np.nan, 75, 79, 83, np.nan, 78]})
df.loc[:, 'price'] = df.loc[:, 'price'].interpolate(method='linear')	# interpolation
df.fillna(method='ffill')	# forward fill