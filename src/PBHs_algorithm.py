#!/usr/bin/env python3  

import math 
import pandas as pd
import numpy as np
from scipy import constants
from scipy.integrate import solve_ivp

# Constants
M_CRITICAL = 1e20  # Critical mass in grams
MINIMUM_SURVIVING_MASS = 5e14     # Minimum mass in grams
SIGMA_DIFF = 0.5

def phi(mass: float) -> float:
    """
    Calculate the function phi based on mass M.
    """
    exponential_term = - (math.log(mass / M_CRITICAL  ))** 2 / (2*SIGMA_DIFF ** 2)
    return (1/mass) * math.exp(exponential_term)

def evaporation_time(mass: float) -> float:
    """
    Calculate the evaporation time in yearsfor a given mass.
    """
    return 1e10 * (mass/MINIMUM_SURVIVING_MASS) ** 3  # in years


def main() -> None:
    """
    Entry point of the program.
    """
    m = 1e19
    print(f"Phi({m} g) = {phi(m):.2e} g-1")
    print(f"Evaporation time for {m} g = {evaporation_time(m)/1e9:.2e} billion years")

if __name__ == "__main__":

    main()
