def pcaAnalysis(stockReturns):
    """
    stockReturns: Pandas DataFrame of stock returns
    """
    corrMat = stockReturns.corr()
    eigenvalues, eigenvectors = np.linalg.eig(corrMat)
    explainedVarianceRatio = eigenvalues/np.sum(eigenvalues)
    return eigenvalues, eigenvectors, explainedVarianceRatio