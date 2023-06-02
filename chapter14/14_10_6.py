import numpy as np

spread = 500.0 / 10000.0
recov = 0.4
tau = 5.0
N = 100
M = 200
rho = 0.2

def index_loss_distr(N, M, rho, spread, recov, tau):
    implied_lambda = spread / (1 - recov)
    surv_prob = math.exp(-implied_lambda * tau)
    def_prob = 1 - surv_prob
    C = norm.ppf(def_prob)

    fLs = np.zeros(N+1)

    for ii in range(M+1):
        Zi = -5.0 + ii * (10 / M)
        phiZ = norm.pdf(Zi) 
        dz = 10 / M
    
        for n in range(N+1):
            innerNumer = C - rho*Zi
            innerDenom = np.sqrt(1 - rho**2)
            innerTerm = innerNumer / innerDenom

            pLCondZ = (1 - recov) * norm.cdf(innerTerm)
            fLCondZ = (math.factorial(N) / (math.factorial(n) * math.factorial(N-n))) *pLCondZ**n * (1-pLCondZ)**(N-n)
            fLs[n] += fLCondZ * phiZ * dz

    return fLs

fLs = index_loss_distr(N, M, rho, spread, recov, tau)
print(fLs)
print(fLs.sum())
plt.plot(fLs)