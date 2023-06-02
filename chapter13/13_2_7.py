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

bond_price_dur_conv(0.05/2*10000,10000,0.04,5,2)

# (10430.589989789156, 4.498366646086723, 21.596380839001984)





