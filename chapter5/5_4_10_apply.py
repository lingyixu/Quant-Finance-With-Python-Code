# use the dataframe in the basic statistics example
# this self-defined function converts simple returns to log returns
df.apply(lambda x: np.log(x+1))
