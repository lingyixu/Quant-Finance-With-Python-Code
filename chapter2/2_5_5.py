def binomialTreeCallOptionPrice(N, r, sigma, S_0, T, K):
    deltaT = T/N
    u = np.exp(sigma * np.sqrt(deltaT))
    d = 1/u
    p = (np.exp(r*deltaT) - d)/(u-d)

    priceTree = [n*[None] for n in range(1,N+2)]

    for i in range(N+1): #each time period
        for j in range(i+1): #each possible price within each time period
            priceTree[i][j] = S_0 *  (u**(j)) * (d**(i-j))

    callPriceTree = [n*[None] for n in range(1,N+2)]
    #terminal payoffs
    callPriceTree[-1] = [max(px-K,0) for px in priceTree[-1]]

    for i in range(N-1,-1,-1): #each time period starting from the end
        for j in range(i+1): #each price within each time period
            callPriceTree[i][j] = np.exp(-r*deltaT)*((1-p)*callPriceTree[i+1][j] + p*callPriceTree[i+1][j+1])

    return callPriceTree[0][0]