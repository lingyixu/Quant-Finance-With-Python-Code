def price_digital_call_quad(S_0,K,r,T,density_func, b, N):
    """ Using left riemann sum"""
    width = (b-K)/N
    nodes = np.arange(K,b,width)
    areas = [width * density_func(node) for node in nodes]
    px = np.exp(-r*T)*sum(areas)
    return px
