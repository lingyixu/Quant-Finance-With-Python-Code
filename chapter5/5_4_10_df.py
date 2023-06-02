import pandas as pd
df = pd.DataFrame(data=np.random.random(size=(5,3)),
                  index=['2014','2015','2016','2017','2018'],
                  columns=['SPY', 'QQQQ', 'IWM'])