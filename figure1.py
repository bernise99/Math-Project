import matplotlib.pyplot as plt

# Define parameters and initial conditions
beta = 0.1
gamma = 0.05
gamma_v = 0.02
N = 1000  # Total population
s, i, r, v = 900, 100, 0, 0  # Initial conditions

# Time settings
T = 100  # Total time
dt = 0.1  # Time step

# Lists to store results
s_values, i_values, r_values, v_values, time_values = [], [], [], [], []

# Euler's method
for t in range(int(T/dt)):
    s_values.append(s)
    i_values.append(i)
    r_values.append(r)
    v_values.append(v)
    time_values.append(t*dt)

    ds = (-beta * s * i / N - gamma_v * s * v) * dt
    di = (beta * s * i / N - gamma * i) * dt
    dr = (gamma * i) * dt
    dv = (gamma_v * s * v) * dt

    s += ds
    i += di
    r += dr
    v += dv

# Plot the results
plt.plot(time_values, s_values, label='Susceptible')
plt.plot(time_values, i_values, label='Infected')
plt.plot(time_values, r_values, label='Recovered')
plt.plot(time_values, v_values, label='Vaccinated')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()
