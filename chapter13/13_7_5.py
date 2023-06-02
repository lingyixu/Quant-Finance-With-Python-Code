def price_caplet(sigma,t,K,delta,rate):
    
    f_0 = forward(t,t+delta,rate)
    
    d1 = (math.log(f_0/K) + 0.5*sigma**2*t)/(sigma * math.sqrt(t))
    d2 = (math.log(f_0/K) - 0.5*sigma**2*t)/(sigma * math.sqrt(t))
    
    cap = delta * discount(0,t+delta, rate) * (f_0 * sp.norm.cdf(d1) - K*sp.norm.cdf(d2))
    
    return cap

def price_cap(sigma,delta,start,length,rate,K):
    
    cap = 0
    
    for i in range(length/delta):
        
        t = start+delta*i
        caplet = price_caplet(sigma,t,K,delta,rate)
        cap += caplet
    
    return cap
        
            
    
    

