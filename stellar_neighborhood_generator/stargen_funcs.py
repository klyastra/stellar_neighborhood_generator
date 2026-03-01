import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import interp1d

def sample_from_custom_pdf(f, x_min, x_max, n_samples=10000, n_grid=10000, bins=100):
    """
    Sample from a custom probability density function using inverse transform sampling.
    
    Parameters:
        f          : function (unnormalized PDF)
        x_min      : lower bound
        x_max      : upper bound
        n_samples  : number of random samples to generate
        n_grid     : resolution for numerical integration
        
    Returns:
        samples    : array of sampled values
        x          : grid values
        pdf        : normalized PDF values
    """
    
    # Create x grid
    x = np.linspace(x_min, x_max, n_grid)
    y = f(x)

    # Ensure non-negative
    y = np.clip(y, 0, None)

    # Normalize PDF by area (this is used for probability calculations)
    area = np.trapz(y, x)
    pdf = y / area

    # Compute CDF
    cdf = cumulative_trapezoid(pdf, x, initial=0)
    cdf /= cdf[-1]  # normalize to exactly 1

    # Build inverse CDF function
    inv_cdf = interp1d(cdf, x, bounds_error=False, fill_value=(x_min, x_max))

    # Generate uniform samples
    u = np.random.rand(n_samples)

    # Transform via inverse CDF
    samples = inv_cdf(u)

    # ---------------------------------------------------------
    # Histogram scaling section (matches plotted histogram)
    # ---------------------------------------------------------

    counts, bin_edges = np.histogram(samples, bins=bins)
    max_hist_height = counts.max()

    # Scale PDF so its maximum matches tallest histogram bin
    pdf_heightnorm = pdf * (max_hist_height / pdf.max())

    return samples, x, pdf_heightnorm




def IMF(x):
    '''
    A non-normalized continuous piecewise function composed of different power-law functions for certain mass intervals.
    This entire function is to be converted into a probability density function (PDF) when normalized in the sample_from_custom_pdf() function above.
    The power law function follows the form dN/dM = C*M^(-a)
      * C = correction constant for continuity between different power law functions
      * M = mass in solar masses (Msol; x-axis)
      * a = power-law slope. Positive = decreases with mass, negative = increases with mass.
      * N = number of stars for a given mass interval.


    De Furio et al. 2025 (Fig 5) - 0.0005-0.062 Msol IMF  (https://doi.org/10.3847/2041-8213/adb96a)
      * "double power-law model with a breakpoint mass [at 0.012 Msol] best models our results"

    Li et al. 2023 - Stellar initial mass function varies with metallicity and time  (https://www.nature.com/articles/s41586-022-05488-1)
      * Kroupa slope of 1.3 for <0.5 Msol
      * Salpeter/Kroupa slope of 2.3 for >0.5 Msol

    You may refer to Artifexian's crude star population generator for reference:
    https://docs.google.com/spreadsheets/d/1UHZl5CLSJUiC7MxNmFgtw9oogko37NkEPMs4cKK8jps/edit?gid=1421409789#gid=1421409789
      * Artifexian uses the following modern stellar neighborhood spectral type distribution:
        M (Red Dwarf): ~76%
        K (Orange Dwarf): ~12%
        G (Yellow Dwarf - Sun-like): ~7.6%
        F (Yellow-white): ~3%
        A (White): ~0.6%
        B (Blue-white): ~0.13%
        O (Blue): <0.00003%
    '''

    x = np.asarray(x, dtype=float)

    # Breakpoints
    m0 = 0.0005
    m1 = 0.012
    m2 = 0.062
    m3 = 0.5
    m4 = 1.0
    m5 = 100.0  # end of mass range

    # Slopes for dN/dM  (positive alpha means decreasing with mass)
    a1 = -1.03  # MUST be negative; below the 13 M_J brown dwarf mass limit, rogue planet count decreases with mass
    a2 = 0.34  # a1 and a2 from De Furio et al. 2025
    a3 = 1.3  # Kroupa slope for <0.5 Msol
    a4 = 2.3  # Kroupa/Salpeter slope for >0.5 Msol
    a5 = 2.35  # assume extra massive stars still follow the Kroupa/Salpeter slope

    # Continuity constants
    C1 = 1.0
    C2 = C1 * m1**(a2 - a1)
    C3 = C2 * m2**(a3 - a2)
    C4 = C3 * m3**(a4 - a3)
    C5 = C4 * m4**(a5 - a4)

    y = np.zeros_like(x)

    y[(x >= m0) & (x < m1)] = C1 * x[(x >= m0) & (x < m1)]**(-a1)  # 0.0005-0.012 Msol
    y[(x >= m1) & (x < m2)] = C2 * x[(x >= m1) & (x < m2)]**(-a2)  # 0.012-0.062 Msol
    y[(x >= m2) & (x < m3)] = C3 * x[(x >= m2) & (x < m3)]**(-a3)  # 0.062-0.41 Msol
    y[(x >= m3) & (x < m4)] = C4 * x[(x >= m3) & (x < m4)]**(-a4)  # 0.41-1.0 Msol
    y[(x >= m4) & (x <= m5)] = C5 * x[(x >= m4) & (x <= m5)]**(-a5)  # 1.0-100 Msol

    return y




def MS_endmass(age_Gyr):
    """
    Gives you the maximum main-sequence (MS) star mass for a given age (assumed to be the MS lifetime for aforementioned mass)

    Input:
        time/age [Gyr]

    Output
        Maximum MS star mass in solar masses [Msol]
    """
    age_yr = age_Gyr * 10**9  # convert Gyr to plain years
    mass = ( age_yr * 10**(-10) )**(-2.5)

    return mass  # in Msol