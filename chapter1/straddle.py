def straddle_payoff(S,K):
    call = call_payoff(S,K)
    put = put_payoff(S,K)
    return call+put

K=100
terminal_px = np.linspace(0,200,201,endpoint=True)
straddle_payoffs = straddle_payoff(terminal_px,K)

plt.plot(terminal_px, straddle_payoffs)
plt.title('Long Straddle with K=100')
plt.xlabel('Asset Price at Maturity')
plt.ylabel('Payoff')
plt.show()