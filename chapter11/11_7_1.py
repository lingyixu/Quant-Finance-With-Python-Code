import numpy as np

s0 = 125
t = 1
r = 0.05
nu0 = .25**2
n = 252
N = 10000
xi = 0.3
rho = -0.5
kappa = 1
theta = nu0
k = 125  # at-the-money option

def heston_simulate(s0, t, r, nu0, kappa, theta, xi, rho, n, N):
    dt = 1 / n
    dwt = np.random.multivariate_normal(
        mean=(0, 0),
        cov=[[dt, rho*dt], [rho*dt, dt]],
        size=(N, int(n * t)))
    s, nu = np.zeros((N, dwt.shape[1] + 1)), np.zeros((N, dwt.shape[1] + 1))
    s[:, 0], nu[:, 0] = s0, nu0
    for i in range(1, s.shape[1]):
        s[:, i] = s[:, i-1] + s[:, i-1] * r * dt \
            + s[:, i-1] * nu[:, i-1]**0.5 * dwt[:, i-1, 0]
        nu[:, i] = nu[:, i-1] + kappa*(theta-nu[:, i-1]) \
            + xi*nu[:, i-1]**0.5*dwt[:, i-1, 1]
    s = s
    nu = nu
    return s, nu

def euro_payoffs(k, t, is_call, paths):
    st = paths[:, -1]
    return np.fmax(st - k, 0) if is_call else np.fmax(k - st, 0)

def c(s0=s0, nu0=nu0, theta=theta, t=t, r=r, kappa=kappa, xi=xi, rho=rho, n=n, N=N, k=k):
    np.random.seed(0)  # to get the same random numbers every time
    pathsS0, pathsNu = heston_simulate(s0, t, r, nu0, kappa, theta, xi, rho, n, N)
    euro_prc = np.exp(-r * t) * np.mean(euro_payoffs(k, t, True, pathsS0))
    return euro_prc

dnu0_delta = (xi * rho * epsilon) / s0

epsilon = 1e-6
smile_delta = (c(s0=s0+epsilon, nu0=nu0+dnu0_delta) - c(s0=s0-epsilon, nu0=nu0-dnu0_delta)) / (2*epsilon)  # 0.6303207156221902