import math
import pandas as pd
import numpy as np

import scipy.constants as const
from astropy import constants as astro_const
from decimal import Decimal


solar_mass_grams = 1000 * astro_const.M_sun.value

# Planck mass in kg
planck_mass_g = np.sqrt(
    (const.hbar * const.c) / const.G
) * 1000

# Formula for Hawking Temperature (T_bh)

# T_bh = (h_bar * c**3) / (8 * pi * k_b * G * M)

# Variables:
# h_bar: Reduced Planck constant
# c: Speed of light
# k_b: Boltzmann constant
# G: Gravitational constant
# M: Mass of the black hole
# pi: math.pi

def hawking_temp_from_fundamental(h_bar, c, k_b, G, M):
    """
    Calculates the Hawking temperature of a black hole using fundamental constants.
    
    Args:
        h_bar (float): Reduced Planck constant.
        c (float): Speed of light.
        k_b (float): Boltzmann constant.
        G (float): Gravitational constant.
        M (float): Mass of the black hole.
        
    Returns:
        float: The Hawking temperature in Kelvin.
    """
    return (h_bar * c**3) / (8 * math.pi * k_b * G * M)

# Approximate formula for Hawking Temperature

# T_bh = 6.2e-8 K / (M / M_solar)

# Variables:
# M: Mass of the black hole
# M_solar: Mass of the Sun

def hawking_temp_from_solar_mass(M, M_solar):
    """
    Calculates the Hawking temperature of a black hole in Kelvin
    using its mass relative to the mass of the Sun.
    
    Args:
        M (float): Mass of the black hole.
        M_solar (float): Mass of the Sun.
        
    Returns:
        float: The Hawking temperature in Kelvin.
    """
    return (6.2e-8) / (M / M_solar)

# Example usage with some known values
# h_bar = 1.054571817e-34 # J*s
# c = 2.99792458e8 # m/s
# k_b = 1.380649e-23 # J/K
# G = 6.67430e-11 # N*m^2/kg^2
# M_solar = 1.98847e30 # kg

# Let's say we have a black hole with a mass 10 times that of the sun
# M_bh = 10 * M_solar

# You would call the functions like this:
# T_bh_fundamental = hawking_temp_from_fundamental(h_bar, c, k_b, G, M_bh)
# T_bh_approximate = hawking_temp_from_solar_mass(M_bh, M_solar)


def critical_mass_for_bg_temperature(temperature_background):
    return 1.23e26/temperature_background

def dm_dt(mass_grams, temperature):
    dm_dt_lambda = 1.75e-80
    dm_dt_A = 3.96e24
    first_term = -dm_dt_A/mass_grams**2
    second_term = dm_dt_lambda *mass_grams**2 * temperature**4

    first_term_exp = extract_exponent_decimal(str(first_term))
    second_term_exp = extract_exponent_decimal(str(second_term))
    
    return first_term + second_term, first_term, second_term, first_term_exp == second_term_exp

def extract_exponent_decimal(number_string):
    """
    Extracts the exponent from a number string in scientific notation.
    """
    # 1. Create a Decimal object from the string
    d = Decimal(number_string)

    # 2. Get the number's internal representation tuple
    #    (sign, digits, exponent)
    exponent = d.as_tuple().exponent

    # For numbers in scientific notation, this exponent is the 'E' part.
    # Note: Decimal uses a negative exponent for small numbers (e.g., -27)
    # and a positive exponent for large numbers (e.g., 2).
    return exponent