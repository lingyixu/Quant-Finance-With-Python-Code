sharpe_arr = ret_arr / vol_arr
tan_idx = sharpe_arr.argmax()  # sharpe_arr contains SR of all portfolios on the efficient frontier
tan_weight = weight_arr[tan_idx,:]  # weight_arr stores the weight vector for all portfolios on the efficient frontier
tan_ret = ret_arr[tan_idx]
tan_vol = vol_arr[tan_idx]