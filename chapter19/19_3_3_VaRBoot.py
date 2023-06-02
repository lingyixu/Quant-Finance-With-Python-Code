import random

def var_boot(df_ret, eps, paths, pathLength):
    
    N = df_ret.shape[0]
    n = df_ret.shape[1]
    ret_simu = np.zeros((paths,n))

    for i in range(paths):
        idx_simu = random.sample(range(N), pathLength)
        path_rets = np.zeros((pathLength,n))
        for j in range(pathLength):
            ret_simu[i,:] += df_ret.iloc[idx_simu[j],:]

    df_simu = pd.DataFrame(ret_simu)
    df_simu_port = df_simu.mean(axis=1)
    VaR = df_simu_port.quantile(eps)

    return VaR