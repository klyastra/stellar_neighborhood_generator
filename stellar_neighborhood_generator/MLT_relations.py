import numpy as np
from stefanboltzmann_funcs import *


### M-L relation ###
def MS_mass2lum(x):
    '''
    Calculate a main-sequence (MS) star's luminosity [Lsol] given its mass, using the M-L relation fit equation shown in
    Figure 8 of Eker et al. 2018  (https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E)

    The mass-luminosity relation is a linear piecewise function in logM-logL space.

    ***This only applies to stars with masses between 0.1 to 50 Msol***
    '''

    logx = np.log10(np.asarray(x, dtype=float))  # log10 scale
    logy = np.zeros_like(logx)


    # logM and logL breakpoint values are given in Figure 8.
    # the logL value at the corresponding logM breakpoint is estimated by visual inspection of Figure 8
    logM0, logL0 = -1, -3.2  # beginning of the curve, starting from 0.1 Msol (logM = -1)
    logM1, logL1 = np.log10(0.45), -1.6  # first breakpoint
    logM2, logL2 = np.log10(0.72), -0.5
    logM3, logL3 = np.log10(1.05), 0.2
    logM4, logL4 = np.log10(2.4), 1.7
    logM5, logL5 = np.log10(7), 3.45  # last breakpoint
    logM6, logL6 = 1.6, 5.75  # end

    # Slopes
    s0 = (logL1-logL0) / (logM1-logM0)  # from logM0 to logM1
    s1 = (logL2-logL1) / (logM2-logM1)
    s2 = (logL3-logL2) / (logM3-logM2)
    s3 = (logL4-logL3) / (logM4-logM3)
    s4 = (logL5-logL4) / (logM5-logM4)
    s5 = (logL6-logL5) / (logM6-logM5)  # from logM5 to beyond

    # y-intercepts
    b0 = logL0 - s0*logM0  # from logM0 to logM1
    b1 = logL1 - s1*logM1
    b2 = logL2 - s2*logM2
    b3 = logL3 - s3*logM3
    b4 = logL4 - s4*logM4
    b5 = logL5 - s5*logM5  # from logM5 to beyond

    # piecewise function
    logy[(logx < logM1)] = s0*logx[(logx < logM1)] + b0  # include stars smaller than 0.1 Msol (logM0) so things don't break
    logy[(logx >= logM1) & (logx < logM2)] = s1*logx[(logx >= logM1) & (logx < logM2)] + b1
    logy[(logx >= logM2) & (logx < logM3)] = s2*logx[(logx >= logM2) & (logx < logM3)] + b2
    logy[(logx >= logM3) & (logx < logM4)] = s3*logx[(logx >= logM3) & (logx < logM4)] + b3
    logy[(logx >= logM4) & (logx < logM5)] = s4*logx[(logx >= logM4) & (logx < logM5)] + b4
    logy[(logx >= logM5)] = s5*logx[(logx >= logM5)] + b5  # include stars bigger than 50 Msol (logM6) so things don't break

    # convert log back to linear space
    y = 10**logy
    return y




### Define subfunctions which will be used in both M-T and M-R relation functions.

def MS_mass2temp_highmass(x):
    '''
    Input mass [Msol] for temperature [K]
    '''
    temp_K = 10**( -0.170*(np.log10(x))**2  +  0.888*np.log10(x)  +  3.671)
    return temp_K

def MS_mass2rad_lowmass(x):
    '''
    Input mass [Msol] for radius [Rsol]
    '''
    Rsol = 0.438*(x**2) + 0.479*x + 0.075
    return Rsol




### M-T relation ###
def MS_mass2temp(x):
    '''
    Calculate a main-sequence (MS) star's temperature given its mass, using the M-T relation fit equation shown in
    Table 5 of Eker et al. 2018  (https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E)


    ***This only applies to stars with masses between 0.1 to 50 Msol***
    '''

    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    # Breakpoints [log(M/Msol)].
    m0 = 0  # minimum mass allowed
    m1 = 1.5  # 1st breakpoint


    # piecewise function
    y[(x >= m0) & (x < m1)] = SB_temp(MS_mass2lum(x[(x >= m0) & (x < m1)]), MS_mass2rad_lowmass(x[(x >= m0) & (x < m1)]))  # <1.5 Msol; Stefan-Boltzmann law computation from M-L and M-R relations
    y[(x >= m1)] = MS_mass2temp_highmass(x[(x >= m1)])  # >1.5 Msol

    return y



### M-R relation ###
def MS_mass2radius(x):
    '''
    Calculate a main-sequence (MS) star's radius given its mass, using the mass-radius relation fit equation shown in
    Table 5 of Eker et al. 2018  (https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E)


    ***This only applies to stars with masses between 0.1 to 50 Msol***
    '''

    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    # Breakpoints [log(M/Msol)].
    m0 = 0  # minimum mass allowed
    m1 = 1.5  # 1st breakpoint

    # piecewise function
    y[(x >= m0) & (x < m1)] = MS_mass2rad_lowmass(x[(x >= m0) & (x < m1)])  # <1.5 Msol
    y[(x >= m1)] = SB_radius(MS_mass2lum(x[(x >= m1)]), MS_mass2temp_highmass(x[(x >= m1)]))  # >1.5 Msol; Stefan-Boltzmann law computation from M-L and M-T relations

    return y