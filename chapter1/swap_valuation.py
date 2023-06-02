def price_swap(coupon,reference_rates,rf_rate,delta):
  n_periods = len(reference_rates)

  fixed_leg = 0
  for period in range(1,n_periods+1):
    disc_factor = np.exp(-rf_rate*delta*period)
    fixed_leg += delta*coupon*disc_factor

  floating_leg  = 0 
  for period, ref_rate in enumerate(reference_rates,1):
    disc_factor = np.exp(-rf_rate*delta*period)
    floating_leg += delta*reference_rates[period-1]*disc_factor
  
  return floating_leg - fixed_leg
