dfSPYOld = pd.DataFrame(data=np.random.random(size=(5,1)),
                        index=['2009','2010','2011','2012','2013'], columns=['SPY'])
dfSPYNew = pd.DataFrame(data=np.random.random(size=(5,1)),
                        index=['2014','2015','2016','2017','2018'], columns=['SPY'])

dfSPY = pd.concat([dfSPYOld, dfSPYNew])	

