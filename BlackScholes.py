import numpy as np

# Parameters
S0 = 100  # initial stock price
K = 110  # strike price
r = 0.05  # risk-free interest rate
T = 1  # time to maturity
sigma = 0.2  # volatility

# Grid
N = 100  # number of time steps
M = 100  # number of stock price steps
t = np.linspace(0, T, N+1)
dt = T/N
Smax = 2*K  # maximum stock price
dS = Smax/M
S = np.linspace(0, Smax, M+1)

# Initial and boundary conditions
V = np.maximum(S-K, 0)
V[0] = 0
V[M] = Smax-K*np.exp(-r*T)

# Finite difference method
for n in range(N-1, -1, -1):
    for m in range(1, M):
        V[m] = V[m] + dt*(0.5*sigma**2*S[m]**2*(V[m+1]-2*V[m]+V[m-1])/dS**2 
                          + r*S[m]*(V[m+1]-V[m-1])/(2*dS) - r*V[m])
    V[0] = 0
    V[M] = Smax-K*np.exp(-r*t[n])

# Option price
option_price = np.interp(S0, S, V)
print(f"Option price: {option_price:.2f}")
