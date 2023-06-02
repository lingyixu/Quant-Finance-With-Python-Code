def pairs_trade(currentRatio, longTermRatio, stdRatio, tradeThreshold):

    currentZScore = (currentRatio-longTermRatio)/stdRatio
    
    if currentZScore < - tradeThreshold:
        return 'Buy the spread'
    elif currentZScore > tradeThreshold: 
        return 'Sell the spread'
    else:
        return 'Do nothing'