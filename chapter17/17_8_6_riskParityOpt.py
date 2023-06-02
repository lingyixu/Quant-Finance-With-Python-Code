from scipy.optimize import minimize, Bounds, LinearConstraint

def rc_err(w):
    
    n_asset = len(cov_mat)
    denom = np.sqrt(w.T@cov_mat@w)
    numer = np.zeros(n_asset)
    rc = np.zeros(n_asset)

    for i in range(n_asset):
        numer[i] = w[i]*(cov_mat@w)[i]
        rc[i] = numer[i]/denom
        
    avg_rc = np.sum(rc)/n_asset
    err = rc - avg_rc
    squared_err = np.sum(err**2)
    
    return squared_err

bounds = Bounds([0.0]*len(cov_mat), [1.0]*len(cov_mat))
sum_constraint = LinearConstraint([1.0]*len(cov_mat), [1.0], [1.0])
w0 = np.array([1.0/len(cov_mat)]*len(cov_mat))
res = minimize(rc_err, w0, method='trust-constr', constraints=sum_constraint, bounds=bounds)
print(res.x)