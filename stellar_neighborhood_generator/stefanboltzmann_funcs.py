import numpy as np

# Constants are applied to ALL functions in this module
ST_CONSTANT = 5.670374419184356e-8  # [W/m^2/K^4]; Stefan-Boltzmann constant
R_SOL = 6.957e8  # [m]; solar radius
L_SOL = 3.828e26  # [W]; solar luminosity


def SB_temp(lum_Lsol, rad_Rsol):
    '''
    Function for computing temperature (in K) via the Stefan-Boltzmann Law, given Lsol and Rsol.

    Parameters:
     * lum_Lsol
     * rad_Rsol

    Output:
     * Temperature [K]
    '''

    # convert input quantities into SI units
    lum_SI = lum_Lsol * L_SOL
    rad_SI = rad_Rsol * R_SOL

    T = ( lum_SI / (4*np.pi*(rad_SI**2)*ST_CONSTANT) )**(1/4)
    return T

def SB_radius(lum_Lsol, temp_K):
    '''
    Function for computing radius (in solar radii, Rsol) via the Stefan-Boltzmann Law, given Lsol and temperature in Kelvin.

    Parameters:
     * lum_Lsol
     * temp_K

    Output:
     * Radius [Rsol]
    '''

    # convert input quantities into SI units
    lum_SI = lum_Lsol * L_SOL

    rad_SI = np.sqrt( lum_SI / (4*np.pi*ST_CONSTANT*temp_K**4) )
    Rsol = rad_SI / R_SOL  # convert rad_SI into Rsol
    
    return Rsol

def SB_lum(rad_Rsol, temp_K):
    '''
    Function for computing luminosity (in Lsol) via the Stefan-Boltzmann Law, given Rsol and temperature in Kelvin.

    Parameters:
     * rad_Rsol
     * temp_K

    Output:
     * Luminosity [Lsol]
    '''

    # convert input quantities into SI units
    rad_SI = rad_Rsol * R_SOL

    lum_SI = 4 * np.pi * (rad_SI**2) * ST_CONSTANT * (temp_K**4)
    Lsol = lum_SI * L_SOL  # convert SI to Rsol

    return Lsol