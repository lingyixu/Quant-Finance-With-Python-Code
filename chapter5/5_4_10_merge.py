dfSPY = pd.DataFrame(data=np.random.random(size=(5,1)), 
                     index=['2014','2015','2016','2017','2018'], columns=['SPY'])
dfQQQ = pd.DataFrame(data=np.random.random(size=(5,1)), 
                     index=['2014','2015','2016','2017','2018'], columns=['QQQ'])
dfSPY.join(dfQQQ)