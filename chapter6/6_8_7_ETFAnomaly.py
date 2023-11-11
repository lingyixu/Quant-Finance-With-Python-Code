import yfinance
import numpy as np
import statsmodels.api as sm
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('grayscale')

df = yfinance.download(['XLK'], start='2020-01-01', end='2021-02-28')['Adj Close']
df = df.pct_change().dropna()

# histogram & density plot
sns.displot(df, kde=True, bins=20)

# QQ plot
sm.qqplot(df, line ='q')

# self-defined QQ plot function
def make_qqplot(df, ticker):
    '''
    df: dataframe with return data
    ticker: the stock/ETF ticker to plot against
    '''
    df_sorted = df[[ticker]].sort_values(ticker)
    l = len(df_sorted)
    mu = df_sorted[ticker].mean()
    sigma = df_sorted[ticker].std()

    # empirical quantile
    df_sorted['quantile'] = (np.array(range(l))+1)/l
    # zscore by inverse cdf
    df_sorted['zscore'] = norm.ppf(df_sorted['quantile'])
    # baseline by zscore
    df_sorted['baseline'] = df_sorted['zscore'] * sigma + mu

    plt.scatter(x=df_sorted['zscore'], y=df_sorted[ticker], alpha=0.7, color='gray')
    plt.plot(df_sorted['zscore'], df_sorted['baseline'])
    plt.show()
