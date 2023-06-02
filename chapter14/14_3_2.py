def price_bond(lamb,pay_times,rf,c,recovery):
    
    rf_bond = [math.exp(-x*rf) for x in pay_times]
    surv_prob = [math.exp(-lamb*x) for x in pay_times]
    default_prob = [1-x for x in surv_prob]
    
    default_B = 0
    nondefault_B= 0
    
    for i in range(len(pay_times)):
        default_B += c*rf_bond[i] * surv_prob[i] + recovery*lamb*rf_bond[i]*surv_prob[i]
        nondefault_B += c*rf_bond[i]
    
    
    default_B += rf_bond[len(pay_times)]*surv_prob[len(pay_times)]
    nondefault_B += rf_bond[len(pay_times)]
    
    return default_B,nondefault_B

