import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use('grayscale')


data = [[1,2,3,4,5,7,10,30],[1,1,1,1,1,2,3,20],[2.8438,3.060,3.126,3.144,3.150,3.169,3.210,3.237]]
data = np.array(data)
data = data.T




def d_2_f(d,delta):

    return 1/delta*(1/d -1)

def f_2_d(f,delta):
    
    return 1/(f*delta +1)

def swap_2_fr(swap_rate,delta):

    d_result=np.zeros(len(swap_rate))
    d_result[0]=1/(1+swap_rate[0]*1)
    
    for i in range(1,len(swap_rate)):
        
        part_a=(i+1)-sum(d_result[:i])-swap_rate[i]*np.sum(delta[:i]*d_result[:i])
        d_result[i]=part_a/(1+swap_rate[i]*delta[i])
    
    f = []
    
    for i in range(len(swap_rate)):
    
        f.append(d_2_f(d_result[i],delta[i]))
    
    return f,d_result


swap_rate=data[:,2]/100
delta = data[:,1]
f,d_result= swap_2_fr(swap_rate,delta)

plt.figure(1,figsize = (12,8))
plt.plot(data[:,0],f)
plt.title("Extracted Forward Rates")
plt.xlabel("Maturity")
plt.ylabel("Forward Rates")

