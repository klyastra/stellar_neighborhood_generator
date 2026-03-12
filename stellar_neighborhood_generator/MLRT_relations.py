import numpy as np
from stefanboltzmann_funcs import *


### M-L relation ###
def MS_mass2lum(x):
    '''
    Calculate a main-sequence (MS) star's luminosity [Lsol] given its mass, using the M-L relation fit equation shown in
    Table 4 of Eker et al. 2018  (https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E)

    The mass-luminosity relation is a linear piecewise function in logM-logL space.

    ***This only applies to stars with masses between 0.1 to 50 Msol***
    '''

    logx = np.log10(np.asarray(x, dtype=float))  # log10 scale
    logy = np.zeros_like(logx)


    # logM and logL breakpoint values are given in Figure 8.
    # the logL value at the corresponding logM breakpoint is estimated by visual inspection of Figure 8
    logM1 = np.log10(0.45)  # first breakpoint
    logM2 = np.log10(0.72)
    logM3 = np.log10(1.05)
    logM4 = np.log10(2.40)
    logM5 = np.log10(7)  # last breakpoint

    # Slopes or power-law indices
    s0 = 2.028
    s1 = 4.572
    s2 = 5.743
    s3 = 4.329
    s4 = 3.967
    s5 = 2.865

    # y-intercepts
    b0 = -0.976
    b1 = -0.102
    b2 = -0.007
    b3 = 0.010
    b4 = 0.093
    b5 = 1.105

    # Inequalities as boolean filters
    part0 = logx < logM1
    part1 = (logx >= logM1) & (logx < logM2)
    part2 = (logx >= logM2) & (logx < logM3)
    part3 = (logx >= logM3) & (logx < logM4)
    part4 = (logx >= logM4) & (logx < logM5)
    part5 = logx >= logM5

    # piecewise function
    logy[part0] = s0*logx[part0] + b0  # include stars smaller than 0.1 Msol (logM0) so things don't break
    logy[part1] = s1*logx[part1] + b1
    logy[part2] = s2*logx[part2] + b2
    logy[part3] = s3*logx[part3] + b3
    logy[part4] = s4*logx[part4] + b4
    logy[part5] = s5*logx[part5] + b5  # include stars bigger than 50 Msol (logM6) so things don't break

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
    return Rsol/0.992  # divide by 0.992 to normalize; this is to ensure 1 Msol = 1 Rsol




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

    # Inequalities as boolean filters
    part0 = (x >= m0) & (x < m1)
    part1 = x >= m1

    # piecewise function
    y[part0] = SB_temp(MS_mass2lum(x[part0]), MS_mass2rad_lowmass(x[part0]))  # <1.5 Msol; Stefan-Boltzmann law computation from M-L and M-R relations
    y[part1] = MS_mass2temp_highmass(x[part1])  # >1.5 Msol

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

    # Inequalities as boolean filters
    part0 = (x >= m0) & (x < m1)
    part1 = x >= m1

    # piecewise function
    y[part0] = MS_mass2rad_lowmass(x[part0])  # <1.5 Msol
    y[part1] = SB_radius(MS_mass2lum(x[part1]), MS_mass2temp_highmass(x[part1]))  # >1.5 Msol; Stefan-Boltzmann law computation from M-L and M-T relations

    return y