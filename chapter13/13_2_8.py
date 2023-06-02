import math
import matplotlib.pyplot as plt

plt.style.use('grayscale')

def bond_price_dur_conv(C,P,y,mat,coupon_frequency):
    
    B = 0
    duration_sum = 0
    convexity_sum = 0

    total_payments = coupon_frequency * mat
    
    for payment in range(1,total_payments+1):
        
        payment_time = payment/coupon_frequency
            
        B +=  C * math.exp(-y * payment_time)
        duration_sum += C * payment_time* math.exp(-y * payment_time)
        convexity_sum += C * payment_time**2 * math.exp(-y * payment_time)
        
          
    B += P * math.exp(-y* mat)
    duration_sum += P * mat * math.exp(-y * mat)
    convexity_sum += P * mat**2 * math.exp(-y * mat)
    
    
    ###convention is to report duration as a positive number
    duration = -(-1/B * duration_sum)
    convexity = 1/B * convexity_sum
    
    return B,duration,convexity




def dur_conv_vs_mat(C,P,y,coupon_frequency,mat_lo,mat_hi):
    
    durations = []
    convexities = []
    maturities = range(mat_lo,mat_hi + 1)
    
    for mat in maturities:
        
        B,duration,convexity = bond_price_dur_conv(C,P,y,mat,coupon_frequency)
 
        durations.append(duration)
        convexities.append(convexity)
    
    fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (12,16))
    ax[0].plot(maturities,durations)
    ax[0].set_xlabel('Maturity')
    ax[0].set_ylabel('Duration')
    ax[0].set_title("Duration vs. Maturity")
    

    ax[1].plot(maturities, convexities)
    ax[1].set_xlabel('Maturity')
    ax[1].set_ylabel('Convexity')
    ax[1].set_title("Convexity vs. Maturity")
    
    print(convexities[-1])
        
    return 


dur_conv_vs_mat(0.04*10000/2,10000,0.04,2,1,30)


        
        
        
        
        
        
        