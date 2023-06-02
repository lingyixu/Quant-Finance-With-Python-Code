from pyfinance.options import BSM as BlackScholes

def coveredCallsBacktest(priceAndVolData):
    """
    priceAndVolData: DataFrame with columns giving the price of the security and the historical market volatility (in that order)
    """
    priceAndVolData['CallPx'] = BlackScholes(S0 = priceAndVolData.iloc[:,0],
                                        K = priceAndVolData.iloc[:,0], T= 1/12,
                                        r=.01, sigma=priceAndVolData.iloc[:,1]/100).value()
    priceAndVolData['CoveredCallPayoff'] = np.nan
    priceAndVolData['Profit/Loss'] = np.nan
    priceAndVolData['PnL'] = 0

    for i in range(1,len(priceAndVolData)):
        underlyingPayoff = priceAndVolData.iloc[i,0] - priceAndVolData.iloc[i-1,0]
        callPayoff = np.maximum(priceAndVolData.iloc[i,0] - priceAndVolData.iloc[i-1,0], 0)
        priceAndVolData.iloc[i,priceAndVolData.columns.get_loc('CoveredCallPayoff')] = underlyingPayoff - callPayoff
        priceAndVolData.iloc[i,priceAndVolData.columns.get_loc('Profit/Loss')] = priceAndVolData['CoveredCallPayoff'][i] + priceAndVolData['CallPx'][i-1]
        priceAndVolData.iloc[i,priceAndVolData.columns.get_loc('PnL')] = priceAndVolData['Profit/Loss'][i] + priceAndVolData['PnL'][i-1]
    
    return monthlyData