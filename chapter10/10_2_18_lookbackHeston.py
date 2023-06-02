S0 = 100
r = 0.05
T = 1
v0 = 0.08
sigma = 0.2
k = 0.7
theta = 0.1
rho = 0
n = 5000
N = 100
K_list = [90, 105, 120]
rho_list = np.arange(-1.01, 1, 0.25)

# initialize dataframes for storing prices under different K's and rho's
df_call = pd.DataFrame()
df_put = pd.DataFrame()

# calculate option prices using the function defined above
for K in K_list:
    call_price_list = []
    put_price_list = []
    
    for rho in rho_list:
        call_price = lookback_heston_simu(S0, K, r, T, v0, sigma, k, theta, rho, n, N, 'call').mean()
        put_price = lookback_heston_simu(S0, K, r, T, v0, sigma, k, theta, rho, n, N, 'put').mean()
        call_price_list.append(call_price)
        put_price_list.append(put_price)
        
    df_call[K] = pd.Series(call_price_list)
    df_put[K] = pd.Series(put_price_list)

# plot the prices
df_call.plot()
df_put.plot()