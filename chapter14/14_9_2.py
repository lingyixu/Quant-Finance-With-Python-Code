from scipy.stats import norm

def payer_swaption(F,sigma,t,K, swapT, rf, const_lamb, coupon_frequency):
    d1 = (math.log(F/K) + 0.5*sigma**2*t)/(sigma * math.sqrt(t))
    d2 = (math.log(F/K) - 0.5*sigma**2*t)/(sigma * math.sqrt(t))

    ra = 0.0
    matT = swapT + t
    total_payments = int(coupon_frequency * (matT - t))
    for payment in range(1,total_payments+1):
        payment_time = payment/coupon_frequency
        ra += math.exp(-rf * payment_time) * math.exp(-const_lamb * payment_time) 

    swn_px = ra * (F * norm.cdf(d1) - K * norm.cdf(d2))       
    return swn_px

payer_swaption(500.0/10000.0, 0.2, 1.0, 500.0 / 10000.0, 5.0, 0.01, 0.025, 2)