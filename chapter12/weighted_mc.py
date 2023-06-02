import numpy as np
import cvxpy as cp
import math

def weighted_mc(call_strikes, impl_vols, s_0, tau, rf, num_nodes, lower_k, upper_k):
    nodes = np.linspace(lower_k, upper_k, num_nodes)

    x = cp.Variable(shape=num_nodes)
    obj = cp.Maximize(cp.sum(cp.entr(x)))
    
    constraints = [0.0 <= x, cp.sum(x) == 1, cp.sum(x * nodes) == s0 * math.exp(rf * tau)]

    threshold = s_0 * 0.005
    for zz, call_strike_zz in enumerate(call_strikes):
        payoffs = np.exp(-rf*tau) * np.maximum(nodes - call_strike_zz, 0.0)
        call_prices_zz = callPx(s_0, call_strike_zz, rf, impl_vols[zz], tau)
        constraints.append(cp.sum(x * payoffs) <= call_prices_zz + threshold)
        constraints.append(cp.sum(x * payoffs) >= call_prices_zz - threshold)

    prob = cp.Problem(obj, constraints)
    prob.solve(verbose=True)

    return x.value

s0 = 100.0
r = 0.0
exp_t = 0.25
upper_k = 150.0
lower_k = 50.0
n_points = 501

ks = np.linspace(lower_k, upper_k, n_points)
ivs = np.full(n_points, 0.2)

wmc_probs = weighted_mc(ks, ivs, s0, exp_t, r, n_points, lower_k, upper_k)
print(wmc_probs)
