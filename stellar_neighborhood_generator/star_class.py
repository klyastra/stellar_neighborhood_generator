import numpy as np
from stargen_funcs import *
from MLRT_relations import *
from spectral_types import MS_spectral_type


class Star:

    # SI-unit constants
    M_SOL = 1.989e30  # [kg]; solar mass
    R_SOL = 6.957e8  # [m]; solar radius
    T_SOL = 5778  # [K]; solar temperature
    L_SOL = 3.828e26  # [W]; solar luminosity


    def __init__(self, name, initial_mass, age):
        '''
        All "self" attributes must be defined inside the init function.
        '''
        # Input attributes
        self.name = name  # string; name of the star
        self.initial_mass = initial_mass  # [Msol]; initial mass of the star
        self.age = age  # [Gyr]; age of the star


        #########################################################
        # Derived attributes (using initial mass and age)
        #########################################################
        # First check if the star is still on the main sequence
        if self.initial_mass < MS_endmass(self.age):
            self.main_sequence = True
        else:
            self.main_sequence = False


        # If the star is on the main sequence, calculate the radius, temperature, and luminosity
        if self.main_sequence == True:
            # Derived MS properties based on mass relations by Eker et al. 2018.
            # Eker et al. 2018 paper is here:  https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E
            self.luminosity = MS_mass2lum(self.initial_mass)  # [Lsol]
            self.radius = MS_mass2radius(self.initial_mass)  # [Rsol]
            self.temperature = MS_mass2temp(self.initial_mass)  # [K]

            self.spectral_type = MS_spectral_type(self.initial_mass, self.temperature)

        # If the star is not on the main sequence, calculate the radius, temperature, and luminosity
        # PLACEHOLDER
        else:
            self.radius = 0
            self.temperature = 0
            self.luminosity = 0

            self.spectral_type = MS_spectral_type(self.initial_mass, self.temperature)  # placeholder
