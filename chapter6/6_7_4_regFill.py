import yfinance
import pandas as pd
import statsmodels.api as sm

df = yfinance.download(['XLK', 'SPY'], start='2016-01-01', end='2021-02-28')['Adj Close']
df = df.pct_change().dropna()
df_missing = df['2021-01-01':'2021-01-31']

# For backtesting or prediction, only historical data is used
df_boot1 = df[df.index.min():'2020-12-31']
linear_reg1 = sm.OLS(df_boot1['XLK'], df_boot1['SPY']).fit()
beta_hat1 = float(linear_reg1.params)
xlk_boot1 = df_missing['SPY'] * beta_hat1

# For risk management purposes, the whole time period can be used (except the missing period)
df_boot2 = pd.concat([df_boot1, df['2021-02-01':'2021-02-28']])
linear_reg2 = sm.OLS(df_boot2['XLK'], df_boot2['SPY']).fit()
beta_hat2 = float(linear_reg2.params)
xlk_boot2 = df_missing['SPY'] * beta_hat2
