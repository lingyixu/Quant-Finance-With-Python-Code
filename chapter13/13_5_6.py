def swaprate(t,smallf):
    s_num = 0
    s_denom = 0
    
    for i in range(1,t):
        
        #s_num += discount(0,t_i,smallf)*forward(t_i,t_i + 1,smallf)
        s_num += discount(0,i,smallf) * forward(i,i+1,smallf)
        s_denom += discount(0,i,smallf)
        
    return s_num/s_denom

def rootfinder(x,t,smallf,df,prev):
    
    for i in range(1+prev,t):
        smallf[i] = x

    swap = swaprate(t,smallf)
    return swap - df['Swap Rates'][t]/100

#df is a Pandas DataFrame with Swap Rates and corresponding Maturity as columns.
#maturity is the longest maturity
def boot_strap(df,maturity):
       
    smallf = np.zeros(maturity)
    prev = 0    
    
    for k in df['Maturity']:
        result = scipy.optimize.root(rootfinder, 0.01,args = (k,smallf,df,prev))
        prev = k
    
    return smallf                
