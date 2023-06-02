def portfolioStats(expectedReturnVector, weightsVector, covarianceMatrix):
    """
    expectedReturnVector & weightsVector: np arrays of vector columns
    covarianceMatrix: 2D symmetric np array
    """ 
    portfolioExpRet = expectedReturnVector.T@weightsVector
    portfolioVol = np.sqrt(weightsVector.T @ covarianceMatrix @ weightsVector)
    return portfolioExpRet[0,0], portfolioVol[0,0]