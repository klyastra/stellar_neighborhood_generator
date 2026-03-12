import numpy as np

# Universally-defined constants in module
M_SOL = 1.989e30  # [kg]; solar mass
R_SOL = 6.957e8  # [m]; solar radius

def WD_mass2radius_NR(Msol, MMW=2):
    '''
    Sub-function that converts a white dwarf's (WD's) mass [Msol] into radius [Rsol],
    using the NON-relativistic WD mass-radius relationship.

    This function is used again in the relativistic WD mass-radius relationship.

    Input:
        Msol
    Output:
        Rsol

    The equation for the non-relativistic WD mass-radius relationship is from page 5 of:
        https://www.physics.mcgill.ca/~cumming/teaching/643/coldstars.pdf
    where it is labeled "R_(5/3)"
    '''

    # Constants
    KM_CONST = 9e8 * 10**(-5)
    # MMW = 2  mean molecular weight of matter inside the WD; typically MMW is approximately 2.  Note that MMW = 1/Y_e.

    Rsol = KM_CONST * Msol**(-1/3) * (2/MMW)**(5/3)  # in km
    # Convert km to Rsol. Note that the R_SOL constant was originally in meters.
    Rsol = Rsol / (R_SOL/1000)

    return Rsol




def WD_mass2radius(Msol, MMW=2):
    '''
    Main function that converts a white dwarf's (WD's) mass [Msol] into radius [Rsol],
    using the RELATIVISTIC WD mass-radius relationship.

    This function is used again in the relativistic WD mass-radius relationship.

    Input:
        Msol
    Output:
        Rsol

    The the non-relativistic WD mass-radius relationship is the last equation at the bottom of page 5 of:
        https://www.physics.mcgill.ca/~cumming/teaching/643/coldstars.pdf
    where it is labeled "R ~ R_(5/3)"

    For the Chandrasekhar limit R_Ch, I used 1.4154 Msol based on the general relativity limit from
    Table 1 of Carvalho et al. (2017):  https://arxiv.org/pdf/1709.01635
    '''

    # Chandrasekhar limit varies depending on mean molecular weight (MMW); MMW is assumed equal to 2 by default.
    M_CH = 1.4514 * (2/MMW)**2  # units [Msol]

    # compute relativisitic radius of WD, in units [Rsol]
    Rsol = WD_mass2radius_NR(Msol, MMW) * ( 1 - (Msol/M_CH)**(4/3) )**(1/2)

    return Rsol


def WD_init2final_mass(initial_mass):
    '''
    Function that predicts the final mass of a white dwarf after it forms from a star with a given initial mass.

    Input:
        initial_mass [Msol]
    Output:
        final_mass [Msol]

    The initial-final mass relationship for white dwarfs is based on Equations 4-6 from Cummings et al. (2018):
        https://iopscience.iop.org/article/10.3847/1538-4357/aadfd6
    * The initial-final mass relationship is a piecewise linear function.
    * Final masses and metallicity of progenitors do not present any correlation.

    Equations 1-4 from Cunningham et al. (2024) also offers a IFMR, but is limited to >1 Msol.
        https://academic.oup.com/mnras/article/527/2/3602/7420520
    '''


    initial_mass = np.asarray(initial_mass, dtype=float)
    final_mass = np.zeros_like(initial_mass)

    # Cummings et al. (2018)
    # Inequalities as boolean filters
    part0 = initial_mass < 0.83
    part1 = (initial_mass >= 0.83) & (initial_mass < 2.85)
    part2 = (initial_mass >= 2.85) & (initial_mass < 3.60)
    part3 = (initial_mass >= 3.60) #& (initial_mass < 7.20)

    # piecewise function
    final_mass[part0] = (0.5554/0.83)*initial_mass[part0]  # extrapolation;  the WD should not be more massive than the progenitor
    final_mass[part1] = 0.080*initial_mass[part1] + 0.489
    final_mass[part2] = 0.187*initial_mass[part2] + 0.184 # add additional constant for continuity
    final_mass[part3] = 0.107*initial_mass[part3] + 0.471 # ends at 7.2 Msol, but could go on

    '''
    # Cunningham et al. (2024)
    # Inequalities as boolean filters
    part0 = initial_mass < 1.0
    part1 = (initial_mass >= 1.0) & (initial_mass < 2.5)
    part2 = (initial_mass >= 2.5) & (initial_mass < 3.4)
    part3 = (initial_mass >= 3.4) & (initial_mass < 5.03)
    part4 = initial_mass >= 5.03

    # piecewise function
    final_mass[part0] = 0.555*initial_mass[part0]  # extrapolation;  the WD should not be more massive than the progenitor
    final_mass[part1] = 0.086*initial_mass[part1] + 0.469
    final_mass[part2] = 0.10*initial_mass[part2] + 0.40 + 0.034 # add additional constant for continuity
    final_mass[part3] = 0.06*initial_mass[part3] + 0.57
    final_mass[part4] = 0.17*initial_mass[part4] + 0.04 - 0.0233  # ends at 7.6 Msol, but could go on
    '''

    return final_mass  # [Msol]


def WD_luminosity(age_Gyr, mass_Msol):
    '''
    Function that approximates the luminosity of a white dwarf given its age (after forming) and final mass.

    Input:
        age_Gyr
        mass_Msol
    Output:
        lum_Lsol

    Obtained equation from Astro 127 lecture.
    '''
    
    lum_Lsol = (5e-4) * mass_Msol * age_Gyr**(-7/5)

    return lum_Lsol