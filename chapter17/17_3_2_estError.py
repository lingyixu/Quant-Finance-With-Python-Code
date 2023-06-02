sigma_ret = np.sqrt(np.diag(cov_mat))/np.sqrt(11)
ci_lower, ci_upper = scipy.stats.norm.interval(0.9, loc=ret, scale=sigma_ret)