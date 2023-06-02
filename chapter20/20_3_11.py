def momentumStrategy(monthlyPrices, n):
    """
    monthlyPrices (pandas dataframe): dataframe of end of month prices for stocks
    n (int): the number of top stocks to buy/ bottom stocks to sell 
    """
    nStocks = len(monthlyPrices.columns)
    monthlyReturns = monthlyPrices.pct_change(1)
    annualReturns = monthlyPrices.pct_change(12)
    #computing the signal as annual minus monthly return
    momentumSignal = (annualReturns - monthlyReturns).dropna()
    #ranking in each row in descending order of signal
    rankedSignal = momentumSignal.rank(axis = 1, ascending = False)
    #names of the stocks that are ranked in the top n
    longs = rankedSignal.apply(lambda x: x.index[x <= n].tolist(),axis = 1)
    longs.name = 'long'
    #names of the stocks that are ranked in the bottom n
    shorts = rankedSignal.apply(lambda x: x.index[x  > nStocks - n ].tolist(),axis = 1)
    shorts.name = 'short'
    #putting longs and shorts into a dataframe
    longShortDf = pd.concat([longs, shorts], axis = 1)
    return longShortDf