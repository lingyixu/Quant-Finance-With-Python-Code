import numpy as np

s0 = 125  # inital asset price
t = 1  # maturity in years
r = 0.05  # annual risk free rate
sigma = .25  # annual volatility
n = 252  # number of steps in unit of t
N = 100000  # number of random draws
k = 125  # at-the money option

def bs_simulate(s0, t, r, sigma, n, N):
    dt = 1 / n
    dwt = np.random.normal(0, np.sqrt(dt), (N, int(n * t)))
    s = np.zeros((N, dwt.shape[1] + 1))
    s[:, 0] = s0
    for i in range(1, s.shape[1]):
        s[:, i] = s[:, i-1] + s[:, i-1] * r * \
            dt + s[:, i-1] * sigma * dwt[:, i-1]
    return s

def lookback_price(k, t, is_call, paths):
    s_m = np.max(paths, axis=1) if is_call else np.min(paths, axis=1)
    return np.fmax(s_m - k, 0) if is_call else np.fmax(k - s_m, 0)

def c(s0=s0, sigma=sigma, t=t, r=r, k=k, n=n, N=N):
    np.random.seed(0)  # to get the same random numbers every time
    paths = bs_simulate(s0, t, r, sigma, n, N)
    look_prc = np.exp(-r * t) * np.mean(lookback_price(k, t, True, paths))
    return look_prc

epsilon = 1e-6  # different epsilon gets different gamma
delta = (c(s0+epsilon) - c(s0-epsilon)) / (2*epsilon)  # 1.1608790693173887
vega = (c(s0, sigma+epsilon) - c(s0, sigma-epsilon)) / (2*epsilon)  # 106.27836798526857