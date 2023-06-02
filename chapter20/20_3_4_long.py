import statsmodels.tsa.stattools as stools

def pairs_trade(series1, series2, lookWindow, tradeThreshold):
    """
    series1 and series2: numpy arrays or pandas series containing the prices of the two assets
    lookWindow (int): the window length of the used to calculate the rolling mean and standard deviation of the ratio
    tradeThreshold (float): the z-score (abs value) above which we would trade
    """
    regr = linear_model.LinearRegression(fit_intercept=False)
    s1 = series1.values.reshape(-1,1)
    s2 = series2.values.reshape(-1,1)
    regr.fit(s1, s2)
    
    spread = pd.DataFrame(s1 * regr.coef_ - s2, index=series1.index)
    adf, pvalue = stools.adfuller(spread)

    rollSpreadMean = spread.rolling(lookWindow).mean()
    rollSpreadStd = spread.rolling(lookWindow).std()
    rollSpreadZ = (spread - rollSpreadMean) / rollSpreadStd
    
    pnls = np.zeros(spread.shape[0]-1)
    capital = 0
    pos1 = 0
    pos2 = 0

    for day in range(spread.shape[0] - 1):
        if rollSpreadZ.values[day] < - tradeThreshold: #buy spread
            pos1 += 1
            pos2 += - spread.values[day]
            capital += spread.values[day] * series2[day] - series1[day]
        elif rollSpreadZ.values[day] > tradeThreshold: #sell spread
            pos1 += -1
            pos2 += spread.values[day]
            capital += series1[day] - spread.values[day] * series2[day]
        pnls[day] = capital
        
    #clear the positions on the last day
    capital += pos1 * series1[-1] + pos2 * series2[-1]
    
    pos1, pos2 = 0, 0
    return capital, pnls, rollSpreadZ