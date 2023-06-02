import unittest
import numpy as np

def stock_price_simu(S0, r, sigma, t, N, n): 
    '''
    dSt = r * dt + sigma * dWt
    N: # simulations, n: # periods
    St_list: terminal value of each path
    dt: time interval
    '''
    St_list = np.empty(N)
    dt = t/n
    for i in range(N):
        dwt = np.random.normal(loc=0,scale=np.math.sqrt(dt),size=n)
        dSt = r*dt + sigma*dwt
        St = S0 + sum(dSt)
        St_list[i] = St
    stock_mean = np.mean(St_list)
    stock_var = np.var(St_list)
    return St_list, stock_mean, stock_var

class TestSimulation(unittest.TestCase):

    # the setUp function prepares the framework for the test
    def setUp(self):
        self.S0 = 20
        self.r = 0.05
        self.sigma = 0.5
        self.t = 1
        self.N = 1000
        self.n = 100
        self.St_list, self.stock_mean, self.stock_var = stock_price_simu(self.S0, self.r, self.sigma, self.t, self.N, self.n)

    def test_valid_t(self):
        self.assertTrue(self.t>0)
        self.assertFalse(self.t<=0)

    def test_valid_sigma(self):
        self.assertTrue(self.sigma>0)
        self.assertFalse(self.sigma<=0)

    def test_valid_N(self):
        self.assertTrue(self.N>0)
        self.assertFalse(self.N<=0)

    def test_valid_n(self):
        self.assertTrue(self.n>0)
        self.assertFalse(self.n<=0)

unittest.main()