# Quant-Finance-With-Python-Code
Repo for code examples in Quantitative Finance with Python by Chris Kelliher

#

**[11/13/2023] Comment on Yahoo Finance data retrieval**   
#### Issue:
Function `data.get_data_yahoo()` in [`panadas_datareader`](https://github.com/pydata/pandas-datareader) no longer works due to Yahoo Finance codebase migration.   
See detailed discussion [here](https://github.com/pydata/pandas-datareader/issues/952).   
#### Solution:
Use [`yfinance`](https://github.com/ranaroussi/yfinance):
```
import yfinance as yf
df = yf.download(['XLK', 'SPY'], start='2023-01-01', end='2023-08-31')['Adj Close']
```
