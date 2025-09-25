import math
import pandas as pd
import numpy as np
from scipy import constants
from scipy.integrate import solve_ivp

def hawking_temperature(mass):
    """
    Calculates the Hawking temperature of a black hole using fundamental constants.
    Args:
        M (float): Mass of the black hole.
        
    Returns:
        float: The Hawking temperature in Kelvin.
    """
    return (constants.hbar * constants.speed_of_light**3) / (8 * math.pi * constants.k * constants.G * mass)




# --- 1. Define the ODE Function ---
def decay_ode(t, y, k_val):
    """
    The right-hand side of the differential equation: dy/dt = -k * y
    """
    return -k_val * y

def dM_dt(t, mass):
    """
    The right-hand side of the differential equation: dM/dt =- (hbar c^4)/(15360 pi G^2 m^2)
    """
    return (constants.hbar * constants.speed_of_light**4) / (15360 * math.pi * constants.G**2 * mass**2)


# --- Parameters ---
# k = 0.5
# y0 = 10.0
# t_span = [0, 10]  # Time interval [start, end]

# --- 2. Solve the ODE ---
# 'args' passes the constant k to the decay_ode function
# solution = solve_ivp(
#     fun=decay_ode, 
#     t_span=t_span, 
#     y0=[y0], 
#     args=(k,),
#     dense_output=True # Allows for continuous solution evaluation
# )

# --- 3. Evaluate and Plot ---
# Create a smooth time array for plotting
# t_plot = np.linspace(t_span[0], t_span[1], 100)
# y_solve_ivp = solution.sol(t_plot)[0] # Extract the solution values

# plt.figure(figsize=(8, 4))
# plt.plot(t_plot, y_solve_ivp, label='solve_ivp (Runge-Kutta)', color='red')
# plt.title(r'Accurate Numerical Solution of $\frac{dy}{dt} = -0.5y$')
# plt.xlabel('Time (t)')
# plt.ylabel('y(t)')
# plt.legend()
# plt.grid(True)
# plt.show()
