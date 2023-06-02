from random import choices

def bootstrapSyntheticReturns(historicalReturns, numberOfPaths, pathLength):
    nAssets = 1
    if (len(historicalReturns.shape) > 1):
        nAssets = historicalReturns.shape[1]
    
    paths = np.zeros((pathLength, nAssets,numberOfPaths))
    for path in range(numberOfPaths):
        dateIdcs = choices(range(1, len(historicalReturns)), k = pathLength) #with replacement
        paths[:, :, path] = historicalReturns[dateIdcs, :]

    return paths