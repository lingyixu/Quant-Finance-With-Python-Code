from statsmodels.tsa.stattools import adfuller

data_len = 252
win_size = 21
price_corr_arr = np.zeros(data_len - win_size)
ret_corr_arr = np.zeros(data_len - win_size)

# apply rolling windows to prices and returns
for i in range(len(price_corr_arr)):
    price_corr_arr[i] = np.corrcoef(price_aapl[i:(win_size+i)], price_spy[i:(win_size+i)])[0,1]
for i in range(len(ret_corr_arr)):
    ret_corr_arr[i] = np.corrcoef(ret_aapl[i:(win_size+i)], ret_spy[i:(win_size+i)])[0,1]

# unit root tests, details will be introduced in coming sections
result1 = adfuller(price_corr_arr)
result2 = adfuller(ret_corr_arr)