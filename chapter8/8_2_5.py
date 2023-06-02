from py_vollib.black_scholes.implied_volatility import implied_volatility

S_0 = 100
T = 0.5
r = 0.02
sigma_0 = 2.5
alpha = 0.3
beta = 0.5
rho = 0.3

ks = np.linspace(50,150,101,endpoint=True)
ks = np.delete(ks, np.where(ks == S_0)) #to avoid S_0 == K that the asymptotic formula cannot handle directly
alphas = np.array([0.25,0.5,0.75, 1])
rhos = np.array([-0.5,0,0.33,0.66])
imp_vols_alpha = []
imp_vols_rho = []
for a,p in zip(alphas,rhos) :
    imp_vols_alpha.append( [implied_volatility(sabr_call(S_0,K,T,sigma_0,r,a,beta,rho),S_0,K,T,r,'c') for K in ks] )
    imp_vols_rho.append( [implied_volatility(sabr_call(S_0,K,T,sigma_0,r,alpha,beta,p),S_0,K,T,r,'c') for K in ks] )

fig,ax = plt.subplots(figsize = (12,8))
ax.set_title(r"Impact of $\alpha$ on volatility skew")
ax.set_xlabel("Strike")
ax.set_ylabel("Implied volatility")
ax.plot(ks,imp_vols_alpha[0],label = r'$\alpha$ = %.2f' %(alphas[0]), linestyle = '-' , color = 'black')
ax.plot(ks,imp_vols_alpha[1],label = r'$\alpha$ = %.2f' %(alphas[1]), linestyle = '--', color = 'black')
ax.plot(ks,imp_vols_alpha[2],label = r'$\alpha$ = %.2f' %(alphas[2]), linestyle = ':' , color = 'black')
ax.plot(ks,imp_vols_alpha[3],label = r'$\alpha$ = %.2f' %(alphas[3]), linestyle = '-.', color = 'black')
ax.legend()
plt.show()

fig,ax = plt.subplots(figsize = (12,8))
ax.set_title(r"Impact of $\rho$ on volatility skew")
ax.set_xlabel("Strike")
ax.set_ylabel("Implied volatility")
ax.plot(ks,imp_vols_rho[0],label = r'$\rho$ = %.2f' %(rhos[0]), linestyle = '-' , color = 'black')
ax.plot(ks,imp_vols_rho[1],label = r'$\rho$ = %.2f' %(rhos[1]), linestyle = '--', color = 'black')
ax.plot(ks,imp_vols_rho[2],label = r'$\rho$ = %.2f' %(rhos[2]), linestyle = ':' , color = 'black')
ax.plot(ks,imp_vols_rho[3],label = r'$\rho$ = %.2f' %(rhos[3]), linestyle = '-.', color = 'black')
ax.legend()
plt.show()