from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig_path = Path(__file__).parent.parent / 'figures'
plt.style.use('grayscale')


class HestonProcess:

    def __init__(self, s0, t, r, nu0, kappa, theta, xi, rho, n):
        """Initialize a Heston stochastic process

        Args:
            s0 (float): inital asset price
            t (float): maturity in years
            r (float): annual risk free rate, or r-q for dividend paying assets
            nu0 (float): initial variance
            kappa (float): revertion rate or speed of revertion
            theta (float): long-term variance
            xi (float): volatility of volatility
            rho (float): correlation of Wiener processes
            n (float): number of steps in unit of t

        Reference: https://en.wikipedia.org/wiki/Heston_model
        """
        self.s0 = s0
        self.t = t
        self.r = r
        self.nu0 = nu0
        self.kappa = kappa
        self.theta = theta
        self.xi = xi
        self.rho = rho
        self.n = n

    def simulate(self, N):
        dt = 1 / self.n
        dwt = np.random.multivariate_normal(
            mean=(0, 0),
            cov=[[dt, self.rho*dt], [self.rho*dt, dt]],
            size=(N, int(self.n * self.t)))
        s, nu = np.zeros((N, dwt.shape[1] + 1)), np.zeros((N, dwt.shape[1] + 1))
        s[:, 0], nu[:, 0] = self.s0, self.nu0
        for i in range(1, s.shape[1]):
            s[:, i] = s[:, i-1] + s[:, i-1] * self.r * dt \
                + s[:, i-1] * nu[:, i-1]**0.5 * dwt[:, i-1, 0]
            nu[:, i] = nu[:, i-1] + self.kappa*(self.theta-nu[:, i-1]) \
                + self.xi*nu[:, i-1]**0.5*dwt[:, i-1, 1]
        self.s = s
        self.nu = nu
        return s, nu


class EuropeanOptionPricer:
    """European option"""

    def __init__(self, k, t, is_call):
        self.k = k
        self.t = t
        self.is_call = is_call

    def price(self, paths):
        st = paths[:, -1]
        return np.fmax(st - self.k, 0) if self.is_call else np.fmax(self.k - st, 0)


def calc_option_prc(option_pricer, stoch_proc):
    """calculate option price by option pricer and stochastic process

    Args:
        option_pricer (OptionPricer): object of OptionPricer
        stoch_proc (StochasticProcess): object of StochasticProcess

    Returns:
        np.float
    """
    payoff = option_pricer.price(stoch_proc.s)
    price = np.mean(np.exp(-stoch_proc.r * stoch_proc.t) * payoff)
    return price


o = pd.read_csv("USDBRL_options.csv", index_col=0, header=[0, 1])

s0 = 0.19975
t = 21 / 252  # 1 month to maturity
r = 0.05
nu0 = .25**2
n = 252
N = 10000
xi = 0.3
rho = -0.5
kappa = 1
theta = nu0
ks = o['StrikePrice'].to_numpy().flatten() / 10_000

c_deltas, p_deltas = [], []
c_vegas, p_vegas = [], []
for k in ks:
    def c(s0=s0, nu0=nu0, theta=theta, t=t, r=r, kappa=kappa, xi=xi, rho=rho, n=n, N=N, k=k):
        np.random.seed(0)  # to get the same random numbers every time
        heston = HestonProcess(s0, t, r, nu0, kappa, theta, xi, rho, n)
        heston.simulate(N)
        call = EuropeanOptionPricer(k, t, is_call=True)
        prc = calc_option_prc(call, heston)
        return prc

    def p(s0=s0, nu0=nu0, theta=theta, t=t, r=r, kappa=kappa, xi=xi, rho=rho, n=n, N=N, k=k):
        np.random.seed(0)  # to get the same random numbers every time
        heston = HestonProcess(s0, t, r, nu0, kappa, theta, xi, rho, n)
        heston.simulate(N)
        put = EuropeanOptionPricer(k, t, is_call=False)
        prc = calc_option_prc(put, heston)
        return prc

    epsilon = 1e-6
    c_delta = (c(s0+epsilon) - c(s0-epsilon)) / (2*epsilon)
    c_vega = (c(s0, nu0+epsilon, theta+epsilon) - c(s0, nu0-epsilon, theta-epsilon)) \
        / (2*epsilon)
    p_delta = (p(s0+epsilon) - p(s0-epsilon)) / (2*epsilon)
    p_vega = (p(s0, nu0+epsilon, theta+epsilon) - p(s0, nu0-epsilon, theta-epsilon)) \
        / (2*epsilon)

    c_deltas.append(c_delta)
    c_vegas.append(c_vega)
    p_deltas.append(p_delta)
    p_vegas.append(p_vega)

plt.figure(figsize=(12, 8))
plt.title("Delta of Call Option")
plt.xlabel("Strike")
plt.ylabel("Delta")
plt.plot(ks, c_deltas)
plt.hlines(0, ks[0], ks[-1], linestyles='dashed')
plt.savefig(fig_path / 'sag_call_delta.png')

plt.figure(figsize=(12, 8))
plt.title("Delta of Put Option")
plt.xlabel("Strike")
plt.ylabel("Delta")
plt.plot(ks, p_deltas)
plt.hlines(0, ks[0], ks[-1], linestyles='dashed')
plt.savefig(fig_path / 'sag_put_delta.png')

plt.figure(figsize=(12, 8))
plt.title("Vega of Call Option")
plt.xlabel("Strike")
plt.ylabel("Vega")
plt.plot(ks, c_vegas)
plt.hlines(0, ks[0], ks[-1], linestyles='dashed')
plt.savefig(fig_path / 'sag_call_vega.png')

plt.figure(figsize=(12, 8))
plt.title("Vega of Put Option")
plt.xlabel("Strike")
plt.ylabel("Vega")
plt.plot(ks, p_vegas)
plt.hlines(0, ks[0], ks[-1], linestyles='dashed')
plt.savefig(fig_path / 'sag_put_vega.png')
