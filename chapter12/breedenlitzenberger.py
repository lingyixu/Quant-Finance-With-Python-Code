import math
from scipy.stats import norm
from scipy import interpolate

def breeden_litzenberger(strikes, vols, s_0, rf, tau, dk):
    #use linear interpolation of implied volatility
    vol_interp = interpolate.interp1d(strikes, vols, fill_value="extrapolate")

    #loop through arrays and use Breeden-Litzenberger to find Risk Neutral Density at each point
    phis = np.full(len(strikes), 0.00)
    for zz, strike_zz in enumerate(strikes):
        px_up = callPx(s_0, strike_zz + dk, rf, vol_interp(strike_zz + dk), tau)
        px = callPx(s_0, strike_zz, rf, vol_interp(strike_zz), tau)
        px_dn = callPx(s_0, strike_zz - dk, rf, vol_interp(strike_zz - dk), tau)

        numer = (px_up - 2 * px + px_dn)
        denom = (dk * dk)
        phis[zz] = numer / denom

    return phis


s0 = 100.0
r = 0.0
exp_t = 0.25
upper_k = 150.0
lower_k = 50.0
n_points = 10001

dk = (upper_k - lower_k) / n_points

ks = np.linspace(lower_k, upper_k, n_points)
ivs = np.full(n_points, 0.2)

rnd = breeden_litzenberger(ks, ivs, s0, r, exp_t, dk)
print(rnd)