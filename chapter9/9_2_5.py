from scipy.stats import norm, lognorm
S_0 = 100
K = 100
r = 0
sigma_bs = 0.2
sigma_bach = 20
T = 1
b = 500
N = 1000

#Black-Scholes
density_bs = lognorm(s = sigma_bs*np.sqrt(T), scale = np.exp(np.log(S_0)+ (r - 0.5*(sigma_bs**2))*T)).pdf
print("Black-Scholes price:",price_digital_call_quad(S_0 = S_0,K = K,r = r,T = T,density_func = density_bs,b = b,N = N))
#Black-Scholes price: 0.4641456578462726

#Bachelier
density_bach = norm(loc = S_0*np.exp(r*T),scale = sigma_bach*np.sqrt(T)).pdf
print("Bachelier price:",price_digital_call_quad(S_0 = S_0,K = K,r = r,T = T,density_func = density_bach,b = b,N = N))
#Bachelier price: 0.5039894228040073