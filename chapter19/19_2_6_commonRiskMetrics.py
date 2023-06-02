df_ret_port = df_ret.mean(axis=1)
eps = 0.05

vol = df_ret_port.std()*np.sqrt(252)   # annualized volatility
down_vol = df_ret_port[df_ret_port<0].std()*np.sqrt(252)   # annualized downside deviation
VaR = df_ret_port.quantile(eps)   # daily VaR
CVaR = df_ret_port[df_ret_port<=VaR].mean()   # daily CVaR