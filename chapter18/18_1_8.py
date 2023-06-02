import matplotlib.pyplot as plt
from pandas_datareader import data

df_px = data.get_data_yahoo(('CAD=X'), start='2010-03-01', end='2021-02-28').loc[:, 'Adj Close'].to_frame()
df_rets = df_px.pct_change(1).dropna()
df_signal = df_rets.shift(10).dropna()

def calcRollingIC(df_rets, df_signal, roll_window_length):
    roll_ics = df_rets.rolling(roll_window_length).corr(df_signal)

    print(roll_ics.mean())

    plt.plot(roll_ics)
    plt.show()

    plt.plot(roll_ics.rolling(100).mean().dropna())
    plt.show()

    plt.plot(roll_ics.cumsum().dropna())
    plt.show()
    
    return roll_ics

calcRollingIC(df_rets, df_signal, 10)