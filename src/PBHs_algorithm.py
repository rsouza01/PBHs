#!/usr/bin/env python3  

import math
import json
import pandas as pd
import numpy as np
from scipy import constants
from pathlib import Path

M_CRITICAL = 0
MINIMUM_SURVIVING_MASS = 0
SIGMA_DIFF = 0

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

def load_config(config_path):
    # Load constants from file
    with open(config_path, 'r', encoding='utf-8') as f:
        _constants = json.load(f)
    globals().update(
        M_CRITICAL = _constants["M_CRITICAL"],
        MINIMUM_SURVIVING_MASS = _constants["MINIMUM_SURVIVING_MASS"],
        SIGMA_DIFF = _constants["SIGMA_DIFF"]
    )

def main() -> None:
    """
    Entry point of the program.
    """
    # load_config(Path(__file__).parent / "constants.json")
    load_config("./constants.json")
    m = 1e19
    print(f"Phi({m} g) = {phi(m):.2e} g-1")
    print(f"Evaporation time for {m} g = {evaporation_time(m)/1e9:.2e} billion years")

if __name__ == "__main__":
    main()
