def MS_spectral_type(mass, temp):
    '''
    This is a function that returns a main sequence (MS) spectral type for a given temperature.

    MS spectral type temperature boundaries are based on Table 7 of Eker et al. (2018)
    https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E
    
    Late M-type spectral type temperature boundaries are based on Mamajek's star table:
    https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt

    Parameters:
    temperature [K]

    Returns:
    MS spectral type  (string)
    '''

    ###

    '''
    Brown dwarfs (BDs):
    * Refer to Gizis (2024) Figure 3.16 for temperature ranges of BD spectral types
     ** Gizis (2024) book chapter:  https://iopscience.iop.org/book/mono/978-0-7503-3387-0/chapter/bk978-0-7503-3387-0ch3
     ** Note that the Y spectral type is not defined very strictly when it comes to temperature.
     ** Compare to Wikipedia's list of Y dwarfs:  https://en.wikipedia.org/wiki/List_of_Y-dwarfs
    '''

    # Y-dwarfs; based on Wikipedia Y-dwarf list & Gizis 2024
    if (temp < 25):  # <= 25 K; hypothetical extrapolation
        return "Y9"
    elif (temp >= 25) & (temp < 75):  # 50 +/- 25 K; hypothetical extrapolation
        return "Y8"
    elif (temp >= 75) & (temp < 125):  # 100 +/- 25 K; hypothetical extrapolation
        return "Y7"
    elif (temp >= 125) & (temp < 175):  # 150 +/- 25 K; hypothetical extrapolation
        return "Y6"
    elif (temp >= 175) & (temp < 225):  # 200 +/- 25 K; hypothetical extrapolation
        return "Y5"
    elif (temp >= 225) & (temp < 275):  # 250 +/- 25 K; based on WISE 0855-0714
        return "Y4"
    elif (temp >= 275) & (temp < 325):  # 300 +/- 25 K
        return "Y3"
    elif (temp >= 325) & (temp < 375):  # 350 +/- 25 K
        return "Y2"
    elif (temp >= 375) & (temp < 425):  # 400 +/- 25 K
        return "Y1"
    elif (temp >= 425) & (temp < 480):  # roughly 450 +/- 25 K;  T/Y transition
        return "Y0"


    # T-dwarfs; based on Mamajek's table
    elif (temp >= 480) & (temp < 500):  # T/Y transition
        return "T9.5"
    elif (temp >= 500) & (temp < 600):  # 550 +/- 50 K; use T9.5 and T8.5 temps as boundaries
        return "T9"
    elif (temp >= 600) & (temp < 750):  # use T8.5 and T7.5 temps as boundaries
        return "T8"
    elif (temp >= 750) & (temp < 887.5):  # use T7.5 and avg (T6+T7)/2 temps as boundaries
        return "T7"
    elif (temp >= 887.5) & (temp < 1040):  # use avg (T6+T7)/2 and T5.5 temps as boundaries
        return "T6"
    elif (temp >= 1040) & (temp < 1170):  # use T5.5 and T4.5 temps as boundaries
        return "T5"
    elif (temp >= 1170) & (temp < 1190):  # use T4.5 and avg (T4+T3)/2 temps as boundaries
        return "T4"
    elif (temp >= 1190) & (temp < 1210):  # use avg (T4+T3)/2 and (T2+T3)/2 temps as boundaries
        return "T3"
    elif (temp >= 1210) & (temp < 1230):  # use avg (T2+T3)/2 and (T1+T2)/2 temps as boundaries
        return "T2"
    elif (temp >= 1230) & (temp < 1247.5):  # use avg (T1+T2)/2 and (T0+T1)/2 temps as boundaries
        return "T1"
    elif (temp >= 1247.5) & (temp < 1312.5):  # use avg (T0+T1)/2 and (L9+T0)/2 temps as boundaries; L/T transition
        return "T0"


    # L-dwarfs; based on Mamajek's table
    elif (temp >= 1312.5) & (temp < 1395):  # L/T transition
        return "L9"
    elif (temp >= 1395) & (temp < 1475):
        return "L8"
    elif (temp >= 1475) & (temp < 1540):
        return "L7"
    elif (temp >= 1540) & (temp < 1630):
        return "L6"
    elif (temp >= 1630) & (temp < 1790):
        return "L5"
    elif (temp >= 1790) & (temp < 1895):
        return "L4"
    elif (temp >= 1895) & (temp < 1990):
        return "L3"
    elif (temp >= 1990) & (temp < 2110):
        return "L2"
    elif (temp >= 2110) & (temp < 2215):
        return "L1"
    elif (temp >= 2215) & (temp < 2310):  # M9.5/L0 transition
        return "L0"

    '''
    Main-sequence (MS) stars:

    O2 spectral type from Table 7 of Eker et al. (2018)
        https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.5491E
    
    All other spectral type temperature boundaries are based on Mamajek's star table:
        https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt

    '''

    # M-type stars
    if (temp >= 2310) & (temp < 2365):  # M/L transition
        return "M9.5V"
    elif (temp >= 2365) & (temp < 2420):  # Use avg (M9.5+M9)/2 and M8.5 temp (2420 K) as boundaries
        return "M9V"
    elif (temp >= 2420) & (temp < 2630):  # between M8.5V-M7.5V
        return "M8V"
    elif (temp >= 2630) & (temp < 2740):  # between M7.5V-M6.5V
        return "M7V"
    elif (temp >= 2740) & (temp < 2930):  # between M6.5V-M5.5V
        return "M6V"
    elif (temp >= 2930) & (temp < 3110):  # between M5.5V-M4.5V
        return "M5V"
    elif (temp >= 3110) & (temp < 3270):  # between M4.5V-M3.5V
        return "M4V"
    elif (temp >= 3270) & (temp < 3470):  # between M3.5V-M2.5V
        return "M3V"
    elif (temp >= 3470) & (temp < 3620):  # between M2.5V-M1.5V
        return "M2V"
    elif (temp >= 3620) & (temp < 3770):  # between M1.5V-M0.5V
        return "M1V"
    elif (temp >= 3770) & (temp < 3890):  # upper limit is the averaged temp of M0V and K9V
        return "M0V"

    # K-type stars
    elif (temp >= 3890) & (temp < 3960):  # lower limit is the averaged temp of M0V and K9V, upper limit is K9V-K8V average.
        return "K9V"
    elif (temp >= 3960) & (temp < 4045):  # okay, you get the point for the temp boundaries.
        return "K8V"
    elif (temp >= 4045) & (temp < 4200):
        return "K7V"
    elif (temp >= 4200) & (temp < 4370):
        return "K4V"
    elif (temp >= 4370) & (temp < 4520):
        return "K5V"
    elif (temp >= 4520) & (temp < 4715):
        return "K4V"
    elif (temp >= 4715) & (temp < 4965):
        return "K3V"
    elif (temp >= 4965) & (temp < 5135):
        return "K2V"
    elif (temp >= 5135) & (temp < 5220):
        return "K1V"
    elif (temp >= 5220) & (temp < 5325):
        return "K0V"

    # G-type stars
    elif (temp >= 5325) & (temp < 5430):
        return "G9V"
    elif (temp >= 5430) & (temp < 5515):
        return "G8V"
    elif (temp >= 5515) & (temp < 5575):
        return "G7V"
    elif (temp >= 5575) & (temp < 5630):
        return "G6V"
    elif (temp >= 5630) & (temp < 5670):
        return "G5V"
    elif (temp >= 5670) & (temp < 5700):
        return "G4V"
    elif (temp >= 5700) & (temp < 5745):
        return "G3V"
    elif (temp >= 5745) & (temp < 5815):
        return "G2V"
    elif (temp >= 5815) & (temp < 5895):
        return "G1V"
    elif (temp >= 5895) & (temp < 5990):  # upper bound is F9.5V
        return "G0V"
    
    # F-type stars
    elif (temp >= 5990) & (temp < 6115):  # lower bound is F9.5V
        return "F9V"
    elif (temp >= 6115) & (temp < 6230):
        return "F8V"
    elif (temp >= 6230) & (temp < 6315):
        return "F7V"
    elif (temp >= 6315) & (temp < 6450):
        return "F6V"
    elif (temp >= 6450) & (temp < 6610):
        return "F5V"
    elif (temp >= 6610) & (temp < 6710):
        return "F4V"
    elif (temp >= 6710) & (temp < 6785):
        return "F3V"
    elif (temp >= 6785) & (temp < 6920):
        return "F2V"
    elif (temp >= 6920) & (temp < 7120):
        return "F1V"
    elif (temp >= 7120) & (temp < 7310):
        return "F0V"
    
    # A-type stars
    elif (temp >= 7310) & (temp < 7495):
        return "A9V"
    elif (temp >= 7495) & (temp < 7675):
        return "A8V"
    elif (temp >= 7675) & (temp < 7835):
        return "A7V"
    elif (temp >= 7835) & (temp < 8005):
        return "A6V"
    elif (temp >= 8005) & (temp < 8175):
        return "A5V"
    elif (temp >= 8175) & (temp < 8425):
        return "A4V"
    elif (temp >= 8425) & (temp < 8700):
        return "A3V"
    elif (temp >= 8700) & (temp < 9050):
        return "A2V"
    elif (temp >= 9050) & (temp < 9500):
        return "A1V"
    elif (temp >= 9500) & (temp < 10400):  # B9.5V as upper bound
        return "A0V"
    
    # B-type stars
    elif (temp >= 10400) & (temp < 11500):  # B9.5V as lower bound
        return "B9V"
    elif (temp >= 11500) & (temp < 13150):
        return "B8V"
    elif (temp >= 13150) & (temp < 14250):
        return "B7V"
    elif (temp >= 14250) & (temp < 15100):
        return "B6V"
    elif (temp >= 15100) & (temp < 16050):
        return "B5V"
    elif (temp >= 16050) & (temp < 16700):
        return "B4V"
    elif (temp >= 16700) & (temp < 18500):  # B2.5V as upper bound
        return "B3V"
    elif (temp >= 18500) & (temp < 24500):  # B2.5V as lower bound, B1.5V upper bound
        return "B2V"
    elif (temp >= 24500) & (temp < 29000):  # B1.5V as lower bound, B0.5V upper bound
        return "B1V"
    elif (temp >= 29000) & (temp < 31900):  # B0.5V as lower bound, O9.5V upper bound
        return "B0V"

    # O-type stars
    elif (temp >= 31900) & (temp < 34300):
        return "O9V"
    elif (temp >= 34300) & (temp < 36100):
        return "O8V"
    elif (temp >= 36100) & (temp < 38300):
        return "O7V"
    elif (temp >= 38300) & (temp < 40500):
        return "O6V"
    elif (temp >= 40500) & (temp < 42150):
        return "O5V"
    elif (temp >= 42150) & (temp < 43900):
        return "O4V"
    elif (temp >= 43900) & (temp < 50950):
        return "O3V"
    elif (temp >= 50950):
        return "O2V"
    
    # everything else
    else:
        return "-"
    