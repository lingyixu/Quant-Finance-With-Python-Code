#libor rate beginning of march 2020
libor = 1.15
#monthly S&P500 returns from march 2020 to february 2021
sp500_returns = [2.61,-1.11,3.71,10.75,-2.77,-3.92,7.01,5.51,1.84,4.53,12.68,-12.51] 
sp500_returns = sp500_returns[::-1]
#fed funds rate beginning of march 2020
rf_rate = 0.0065 
delta = 1/12 #monthly payments

swap_value_per_period = []
months = range(1,len(sp500_returns)+1)
for n_months in months:
  swap_value_per_period.append(price_swap(libor,sp500_returns[:n_months],rf_rate,delta)) 
dates = pd.date_range(start = '2020-03-31', end = '2021-02-28', freq='M')
plt.plot(dates, swap_value_per_period)
plt.scatter(dates, swap_value_per_period, s = 100)
plt.xticks(dates, rotation = '45')
plt.show()