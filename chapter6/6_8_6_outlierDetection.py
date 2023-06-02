# plotting
df['ticker'].plot()

# standard deviation
mean = df['ticker'].mean()
std = df['ticker'].std()
suspected_outliers = df[(df['ticker']<mean-3*std) | (df['ticker']>mean+3*std)]

# density analysis
import seaborn as sns
import statsmodels.api as sm
sns.displot(df['ticker'], kde=True)  # histogram & density
sm.qqplot(df['ticker'], line ='q')  # QQ plot against the standard normal distribution
df['ticker'].skew()  # skewness
df['ticker'].kurtosis()  # kurtosis

# KNN
from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(n_neighbors = 3)  # n_neighbors is subject to change
model.fit(df['ticker'].values)
distances, indexes = model.kneighbors(df['ticker'].values)
distances = distances.mean(axis=1)