import numpy as np
import matplotlib.pyplot as plt

def solve_SIR(S0, I0, beta=0.3, gamma=0.1, gamma_v=0.05, delta_t=0.01, T=365):
    times = int(T / delta_t)
    res = np.zeros((times, 4))
    res[0, :] = [S0, I0, 1 - S0 - I0, delta_t]

    def dS(S, I, V):
        return -beta * I * S / N - gamma_v * S * V

    def dI(S, I):
        return beta * I * S / N - gamma * I

    for i in range(1, times):
        S, I, V = res[i - 1, 0], res[i - 1, 1], res[i - 1, 3]
        res[i, 0] = res[i - 1, 0] + delta_t * dS(S, I, V)
        res[i, 1] = res[i - 1, 1] + delta_t * dI(S, I)
        res[i, 3] = res[i - 1, 3] + delta_t * gamma_v * S * V
        res[i, 2] = 1 - res[i, 0] - res[i, 1] - res[i, 3]

    return res

def plot_SIR(res, title=''):
    cols = ['blue', 'orange', 'green', 'red']
    time = res[:, 3]

    plt.plot(time, res[:, 0], label='S', color=cols[0])
    plt.plot(time, res[:, 1], label='I', color=cols[1])
    plt.plot(time, res[:, 2], label='R', color=cols[2])
    plt.plot(time, res[:, 3], label='V', color=cols[3])

    plt.xlabel('Days')
    plt.ylabel('Population')
    plt.title(title)
    plt.legend()
    plt.show()

# Example usage:
S0_example = 0.99
I0_example = 0.01
N = 7_900_000_000
result = solve_SIR(S0_example, I0_example, N, T=365)
plot_SIR(result, 'SIR Model with Vaccinations Example')
