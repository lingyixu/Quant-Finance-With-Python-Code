def min_var_portfolio(sigma_1,sigma_2,rho):
    numerator = sigma_2**2 - sigma_1*sigma_2*rho
    denominator = sigma_1**2 + sigma_2**2 - 2*sigma_1*sigma_2*rho
    w_1 = numerator/denominator
    return (w_1,1-w_1)

min_var_portfolio(0.25,0.3,-0.4)

#(0.5647058823529412, 0.43529411764705883)