def priceDigiCall(paths, K, r):
    """paths: 2D np array, each subarray represents a period in time"""
    terminalVals = paths[-1]
    payoffs = np.where(terminalVals > K,1,0)
    return np.exp(-r*T)*np.mean(payoffs)

def priceOneTouchCall(paths, K, r):
    """paths: 2D np array, each subarray represents a period in time"""
    maxVals = np.max(paths, axis = 0)
    payoffs = np.where(maxVals > K,1,0)
    return np.exp(-r*T)*np.mean(payoffs)