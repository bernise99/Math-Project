import matplotlib.pyplot as plt

# Define parameters
beta = 0.3
gamma = 0.1
gamma_v = 0.05
N = 7_900_000_000  # Total population

# Initial conditions
s, i, r, v = 7_899_999_900, 100, 0, 0  # Starting with 100 infected individuals

# Time settings
T = 365  # Total time in days
dt = 1  # Time step in days

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
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.legend()
plt.show()
