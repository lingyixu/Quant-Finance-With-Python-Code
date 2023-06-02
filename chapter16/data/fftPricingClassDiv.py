from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt

class StochProc(ABC):
    
    def __init__(self, s_0, r, q, t):
        super().__init__()
        self.s_0 = s_0
        self.r = r
        self.q = q
        self.t = t

    @abstractmethod
    def characteristic_fn(self, u):
        print('Not implemented in base class')
        pass

    def calc_fft_call_prices(self, alpha, N, delta_v, K = None):
        assert (alpha > 0 ), "Alpha has to be greater than 0"
        delta = np.zeros(N)
        delta[0] = 1
        delta_k = (2*np.pi)/(N*delta_v)
        if K == None:
            beta = np.log(self.s_0) - delta_k*N*0.5 
        else:
            beta = np.log(K) - delta_k*N*0.5
        k_list = np.array([(beta +(i-1)*delta_k) for i in range(1,N+1) ])
        v_list = np.arange(N) * delta_v
        x_numerator = np.array( [((2-delta[i])*delta_v)*np.exp(-(self.r-self.q)*self.t)  for i in range(N)] )
        x_denominator = np.array( [2 * (alpha + 1j*i) * (alpha + 1j*i + 1) for i in v_list] )
        x_exp = np.array( [np.exp(-1j*(beta)*i) for i in v_list] )
        x_list = (x_numerator/x_denominator)*x_exp* np.array([self.characteristic_fn(i - 1j*(alpha+1)) for i in v_list])
        y_list = np.fft.fft(x_list)
        prices =np.array( [(1/np.pi) * np.exp(-alpha*(beta +(i-1)*delta_k)) * np.real(y_list[i-1]) for i in range(1,N+1)] )
        return prices, np.exp(k_list)

    def calc_fft_digi_call_prices(self, alpha, N, delta_v, K = None):
        assert (alpha > 0 ), "Alpha has to be greater than 0"
        delta = np.zeros(N)
        delta[0] = 1
        delta_k = (2*np.pi)/(N*delta_v)
        if K == None:
            beta = np.log(self.s_0) - delta_k*N*0.5 
        else:
            beta = np.log(K) - delta_k*N*0.5
        k_list = np.array([(beta +(i-1)*delta_k) for i in range(1,N+1) ])
        v_list = np.arange(N) * delta_v
        x_numerator = np.array( [((2-delta[i])*delta_v)*np.exp(-(self.r-self.q)*self.t)  for i in range(N)] )
        x_denominator = np.array( [2 * (alpha + 1j*i) for i in v_list] )
        x_exp = np.array( [np.exp(-1j*(beta)*i) for i in v_list] )
        x_list = (x_numerator/x_denominator)*x_exp* np.array([self.characteristic_fn(i - 1j*alpha) for i in v_list])
        y_list = np.fft.fft(x_list)
        prices =np.array( [(1/np.pi) * np.exp(-alpha*(beta +(i-1)*delta_k)) * np.real(y_list[i-1]) for i in range(1,N+1)] )
        return prices, np.exp(k_list)

    def calc_fft_digi_put_prices(self, alpha, N, delta_v, K = None):
        assert (alpha < 0 ), "Alpha has to be less than 0"
        delta = np.zeros(N)
        delta[0] = 1
        delta_k = (2*np.pi)/(N*delta_v)
        if K == None:
            beta = np.log(self.s_0) - delta_k*N*0.5 
        else:
            beta = np.log(K) - delta_k*N*0.5
        k_list = np.array([(beta +(i-1)*delta_k) for i in range(1,N+1) ])
        v_list = np.arange(N) * delta_v
        x_numerator = np.array( [((2-delta[i])*delta_v)*np.exp(-(self.r-self.q)*self.t)  for i in range(N)] )
        x_denominator = np.array( [2 * (alpha + 1j*i) for i in v_list] )
        x_exp = np.array( [np.exp(-1j*(beta)*i) for i in v_list] )
        x_list = -(x_numerator/x_denominator)*x_exp* np.array([self.characteristic_fn(i - 1j*alpha) for i in v_list])
        y_list = np.fft.fft(x_list)
        prices =np.array( [(1/np.pi) * np.exp(-alpha*(beta +(i-1)*delta_k)) * np.real(y_list[i-1]) for i in range(1,N+1)] )
        return prices, np.exp(k_list)


class Heston(StochProc):

    def __init__(self, sigma, v_0, k, p, theta, r,q, s_0, t):
        super().__init__(s_0,r,q,t)
        self.sigma = sigma
        self.v_0 = v_0
        self.k = k
        self.p = p
        self.theta = theta 
    
    def characteristic_fn(self, u):
        """
        For log price
        """
        lambd = np.sqrt((self.sigma**2)*((u**2)+1j*u) + (self.k - 1j*self.p*self.sigma*u)**2) 
        omega_numerator = np.exp(1j*u*np.log(self.s_0)+1j*u*(self.r-self.q)*self.t+(1/(self.sigma**2))*self.k*self.theta*self.t*(self.k - 1j*self.p*self.sigma*u))
        omega_denominator = (np.cosh(0.5*lambd*self.t) + (1/lambd)*(self.k - 1j*self.p*self.sigma*u)*np.sinh(0.5*lambd*self.t))**((2*self.k*self.theta)/(self.sigma**2))
        phi = (omega_numerator/omega_denominator) * np.exp(-((u**2 + 1j*u)*self.v_0)/(lambd*(1/np.tanh(0.5*lambd*self.t)) + (self.k - 1j*self.p*self.sigma*u)))
        return phi

class Merton_Jump_Diffusion(StochProc):
    def __init__(self, sigma, lambd, a, gamma, r, q, s_0, t):
        super().__init__(s_0,r,q,t)
        self.sigma = sigma
        self.lambd = lambd
        self.a = a
        self.gamma = gamma

    def characteristic_fn(self, u):
        """
        For price
        """
        omega = -0.5*(self.sigma**2) - self.lambd*(np.exp(self.a + 0.5* self.gamma)-1)
        term_1 = 1j*u*omega*self.t
        term_2 = 0.5*(u**2)*(self.sigma**2)*self.t
        term_3 = self.lambd*self.t*(np.exp(1j*u*self.a - 0.5*(u**2)*(self.gamma**2))-1)
        return np.exp(term_1 - term_2 + term_3)

class Variance_Gamma(StochProc):
    def __init__(self, sigma, theta, nu, r, q, s_0, t):
        super().__init__(s_0,r,q,t)
        self.sigma = sigma
        self.theta = theta
        self.nu = nu

    # def characteristic_fn(self, u):
    #     """
    #     for price
    #     """
    #     denominator = 1 - 1j*u*self.theta*self.nu + 0.5* (self.sigma**2)*(u**2)*(self.nu)
    #     power = self.t/self.nu
    #     phi = (1/denominator)**(power)
    #     return phi

    def characteristic_fn(self, u):
        """
        for log price
        """
        omega = (1/self.nu)*np.log(1-self.theta*self.nu - 0.5*(self.sigma**2)*self.nu)
        denominator = 1 - 1j*u*self.theta*self.nu + 0.5* (self.sigma**2)*(u**2)*(self.nu)
        power = self.t/self.nu
        phi = ((self.s_0*np.exp( self.t*(self.r-self.q + omega )))**(1j*u) )/ (denominator**power)
        return phi
