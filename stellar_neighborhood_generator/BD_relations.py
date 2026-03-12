import numpy as np

# Universally-defined constants in module
M_SOL = 1.989e30  # [kg]; solar mass
R_SOL = 6.957e8  # [m]; solar radius
M_JUP = 1.89813e27  # [kg]; Jupiter mass

def BD_temp(age_Gyr, mass_Msol):
    '''
    A function that approximates the temperature of a brown dwarf based on its age and mass.

    Given in Equation 1 of Smith & Marley (2026):  https://arxiv.org/abs/2603.09068

    This is based on a very simplified model of brown dwarf cooling, so it is not fully accurate:
      "The power law fit does not capture structure from deuterium burning or cloud formation
      and dissipation in the evolutionary behavior and produces unrealistically high temperatures at young ages."

    Input:
        age_Gyr
        mass_Msol  (will be converted to mass_Mjup in function)
    Output:
        T  [Kelvin]
    '''
    mass_Mjup = mass_Msol * (M_SOL/M_JUP)
    T = 59 * age_Gyr**(-0.324) * mass_Mjup**0.827
    return T