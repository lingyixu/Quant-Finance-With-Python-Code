def get_rolling_var(ticker, start_date, end_date, win_size, eps):
    
    assert isinstance(win_size, int), 'Please enter an integer as the window size.'
    
    # start date for price record
    price_start_date = str((pd.to_datetime(start_date) - pd.DateOffset(years=win_size)).date())
    # start date in the last widow
    last_start_date = str((pd.to_datetime(end_date) - pd.DateOffset(years=win_size) + pd.DateOffset(days=1)).date())
    
    df_price_full = data.get_data_yahoo(ticker, start=price_start_date, end=end_date)['Adj Close']
    df_ret_full = np.log(df_price_full/df_price_full.shift(1)).dropna()
    
    VaR_list = []
    VaR_port_list = []
    
    for date in pd.date_range(price_start_date, last_start_date)[1:]:
        
        last_date = str((date + pd.DateOffset(years=2) - pd.DateOffset(days=1)).date())
        df_ret = df_ret_full.loc[date:last_date]
        df_ret_port = df_ret.mean(axis=1)   # equal-weighted portfolio
        
        VaR = df_ret.quantile(eps)
        VaR_port = df_ret_port.quantile(eps)
        
        VaR_list.append(VaR)
        VaR_port_list.append(VaR_port)

    idx = pd.date_range(start_date, end_date)
    df_VaR = pd.DataFrame(data=VaR_list, index=idx, columns=ticker)
    df_VaR_port = pd.DataFrame(data=VaR_port_list, index=idx, columns=['portfolio'])
    
    return df_VaR, df_VaR_port