# Coding Example: P&L of Delta Hedged Straddles against Implied vs. Realized Premium
import numpy as np
from scipy.stats import norm
from scipy.optimize import fsolve

s0, r, T, sigma = 100, 0.0, 1, 0.2

def func(k):
    d1 = (np.log(s0/k) + (r + 0.5*sigma**2) * T) / (sigma * np.sqrt(T))
    delta_c = norm.cdf(d1)
    delta_p = -norm.cdf(-d1)
    delta_straddle = delta_c + delta_p
    return delta_straddle


k = fsolve(func, s0)[0]
d1 = (np.log(s0/k) + (r + 0.5*sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
# call option price
c = s0 * norm.cdf(d1) - k * np.exp(-r * T) * norm.cdf(d2)
# put option price
p = k * np.exp(-r * T) * norm.cdf(-d2) - s0 * norm.cdf(-d1)
# straddle price
straddle = c + p


class BlackScholesProcess:

    def __init__(self, s0, t, r, sigma, n):
        self.s0 = s0
        self.t = t
        self.r = r
        self.sigma = sigma
        self.n = n

    def simulate(self, N):
        dt = 1 / self.n
        dwt = np.random.normal(0, np.sqrt(dt), (N, int(self.n * self.t)))
        s = np.zeros((N, dwt.shape[1] + 1))
        s[:, 0] = self.s0
        for i in range(1, s.shape[1]):
            s[:, i] = s[:, i-1] + s[:, i-1] * self.r * \
                dt + s[:, i-1] * self.sigma * dwt[:, i-1]
        self.paths = s
        return s


bs = BlackScholesProcess(s0, T, r, 0.1, 252)
np.random.seed(0)
paths = bs.simulate(10000)  # stock price paths
st = paths[:, -1]  # final stock prices
payoff = np.fmax(st - k, 0) + np.fmax(k - st, 0)  # payoff of call plus put
pnl = payoff - straddle  # profit and loss of straddles
np.mean(pnl)  # -8.059522856874947
