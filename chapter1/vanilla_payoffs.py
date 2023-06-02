def call_payoff(S,K):
  return np.maximum(S-K,0)

def put_payoff(S,K):
  return np.maximum(K-S,0)