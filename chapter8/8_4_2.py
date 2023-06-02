#given price_surface where columns are different strikes and rows are different expiries

# expiry_derivatives
expiry_derivatives = ((price_surface[2:,:] - price_surface[:-2,:]) / (expiries[2:] - expiries[:-2]).reshape(-1,1))[:,:-2]

# strike second derivative 
strike_first_derivatives = (price_surface[:,1:] - price_surface[:,:-1]) / (strikes[1:]-strikes[:-1])
strike_second_derivatives = ((strike_first_derivatives[:,1:] - strike_first_derivatives[:,:-1]) / (strikes[1:-1]-strikes[:-2]))[1:-1,]

variance_surface = expiry_derivatives/ (0.5* (strikes[:-2]**2)*strike_second_derivatives)
vol_surface = np.sqrt(variance_surface)