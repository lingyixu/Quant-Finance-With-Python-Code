from cev_formula import cev_call
from py_vollib.black_scholes.implied_volatility import implied_volatility
S_0 = 100
T = 0.5
r = 0.02
sigma_0 = 25
ks = np.linspace(50,150,101,endpoint=True)
betas = np.array([0,0.25,0.5,0.75,1])
vols = sigma_0/(S_0**betas)
imp_vols = []
for b,vol in zip(betas,vols) :
  if b != 1:
    imp_vols.append( [implied_volatility(cev_call(S_0,K,T,vol,b,r),S_0,K,T,r,'c') for K in ks] )
  else:
    imp_vols.append( [implied_volatility(bs_call(S_0,K,T,vol,r),S_0,K,T,r,'c') for K in ks] )



fig,ax = plt.subplots(figsize = (12,8))
ax.set_title(r"Impact of $\beta$ on volatility skew")
ax.set_xlabel("Strike")
ax.set_ylabel("Implied volatility")
ax.plot(ks,imp_vols[0],label = r'$\beta$ = %.2f, $\sigma$ = %.2f' %(betas[0],vols[0]), linestyle = '-' , color = 'black')
ax.plot(ks,imp_vols[1],label = r'$\beta$ = %.2f, $\sigma$ = %.2f' %(betas[1],vols[1]), linestyle = '--', color = 'black')
ax.plot(ks,imp_vols[2],label = r'$\beta$ = %.2f, $\sigma$ = %.2f' %(betas[2],vols[2]), linestyle = ':' , color = 'black')
ax.plot(ks,imp_vols[3],label = r'$\beta$ = %.2f, $\sigma$ = %.2f' %(betas[3],vols[3]), linestyle = '-.', color = 'black')
ax.plot(ks,imp_vols[4],label = r'$\beta$ = %.2f, $\sigma$ = %.2f' %(betas[4],vols[4]), linestyle = '-', color = 'gray')
ax.legend()
#plt.savefig('8_1_8')
plt.show()