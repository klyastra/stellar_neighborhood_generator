import numpy as np
from stargen_funcs import *
from MLRT_relations import *
from WD_relations import *
from BD_relations import *
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


        if self.age < mass2lifetime(self.initial_mass):
            self.evol_stage = "Main sequence"
        elif (mass2lifetime(self.initial_mass) <= self.age < 1.1*mass2lifetime(self.initial_mass)) & (self.initial_mass < 8.0):
            self.evol_stage = "Giant"
        elif (self.age >= 1.1*mass2lifetime(self.initial_mass)) & (self.initial_mass < 8.0):
            self.evol_stage = "White dwarf"
        elif (mass2lifetime(self.initial_mass) <= self.age < 1.1*mass2lifetime(self.initial_mass)) & (self.initial_mass >= 8.0):
            self.evol_stage = "Supergiant"
        elif (self.age >= 1.1*mass2lifetime(self.initial_mass)) & (8.0 <= self.initial_mass < 20):
            self.evol_stage = "Neutron star"
        elif (self.age >= 1.1*mass2lifetime(self.initial_mass)) & (self.initial_mass >= 20):
            self.evol_stage = "Black hole"
        else:
            self.evol_stage = "Unknown"  # error message - something went wrong...


        # If the star is on the main sequence, calculate the radius, temperature, and luminosity
        if self.evol_stage == "Main sequence":
            # Define these attributes
            self.final_mass = self.initial_mass  # assume no mass loss
            self.remnant_age = '-'  # not applicable

            if self.initial_mass >= 0.078:  # above hydrogen burning limit
                # Derived MS properties based on mass relations by Eker et al. 2018.
                # Eker et al. 2018 paper is here:  https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E
                self.luminosity = MS_mass2lum(self.initial_mass)  # [Lsol]
                self.radius = MS_mass2radius(self.initial_mass)  # [Rsol]
                self.temperature = MS_mass2temp(self.initial_mass)  # [K]
            else:  # brown dwarfs
                self.temperature = BD_temp(self.age, self.initial_mass)  # [K]
                self.luminosity = MS_mass2lum(self.initial_mass)  # [Lsol]
                self.radius = MS_mass2radius(self.initial_mass)  # [Rsol]


            self.spectral_type = MS_spectral_type(self.initial_mass, self.temperature)

        # If the star is not on the main sequence, calculate the radius, temperature, and luminosity
        # PLACEHOLDER
        elif self.evol_stage == "White dwarf":
            # Define these atrributes
            self.final_mass = WD_init2final_mass(self.initial_mass)  # [Msol]
            self.remnant_age = self.age - 1.1*mass2lifetime(self.initial_mass)  # [Gyr]

            # Use WD relationships
            self.radius = WD_mass2radius(self.final_mass)  # [Rsol]
            self.luminosity = WD_luminosity(self.remnant_age, self.final_mass)  # [Lsol]
            # Compute temperature from WD relationships
            self.temperature = SB_temp(self.luminosity, self.radius)  # [K]

            self.spectral_type = MS_spectral_type(self.final_mass, self.temperature)

        else:
            self.radius = 0
            self.temperature = 0
            self.luminosity = 0

            self.spectral_type = "-"  # placeholder
            
            self.final_mass = '-'
            self.remnant_age = '-'
