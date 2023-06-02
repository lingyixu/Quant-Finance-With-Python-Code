'''
14.3.3
'''
import matplotlib.pyplot as plt
import math
plt.style.use('grayscale')
lamb = 0.04
pay_times = [1,2,3,4,5]
rf = 0.02
c = 0.02
recovery = 0.4


def price_bond(lamb,pay_times,rf,c,recovery):
    
    rf_bond = [math.exp(-x*rf) for x in pay_times]
    # print(rf_bond)
    surv_prob = [math.exp(-lamb*x) for x in pay_times]
    default_prob = [1-x for x in surv_prob]
    
    default_B = 0
    nondefault_B= 0
    
    for i in range(len(pay_times)):
        default_B += c*rf_bond[i] * surv_prob[i] + recovery*lamb*rf_bond[i]*surv_prob[i]
        nondefault_B += c*rf_bond[i]
    
    
    default_B += rf_bond[-1]*surv_prob[-1]
    nondefault_B += rf_bond[-1]
    
    return default_B,nondefault_B



def duration_conv(lamb,rf,c,recovery,Tmax):
    
    h = 0.01
    
    pay_times = range(1,Tmax+1)
    
    df_Bond_dur = []
    nondf_Bond_dur = []
    df_Bond_conv = []
    nondf_Bond_conv = []
    
    
    for maturity in pay_times:
        result = price_bond(lamb,range(1,maturity+1),rf,c,recovery)
        result_hi = price_bond(lamb,range(1,maturity+1),rf+h,c,recovery)
        result_lo = price_bond(lamb,range(1+maturity+1),rf-h,c,recovery)
        
        duration_df = -(result_hi[0]-result[0])/(result[0]*h)
        convexity_df = (result_hi[0] - 2*result[0] + result_lo[0])/(h**2)
        
        duration_nondf = -(result_hi[1]-result[1])/(result[1]*h)
        convexity_nondf = (result_hi[1] - 2*result[1] + result_lo[1])/(h**2)
        
        print(result)
        print(result_hi)
        print(result_lo)
        df_Bond_dur.append(duration_df)
        nondf_Bond_dur.append(duration_nondf)
        df_Bond_conv.append(convexity_df/result[0])
        nondf_Bond_conv.append(convexity_nondf/result[1])
        
        
    plt.figure(figsize = (15,10))
    plt.title("Duration of Defaultable Bond")
    plt.plot(pay_times,df_Bond_dur, label = 'Duration: Defaultable Bond')
    plt.plot(pay_times,nondf_Bond_dur, label = 'Duration: Non-Defaultable Bond') 
    plt.ylabel("Duration")
    plt.xlabel("Maturity")
    plt.legend()
    

        
duration_conv(lamb,rf,c,recovery,30)