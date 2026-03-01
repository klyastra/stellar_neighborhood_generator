# import packages
import numpy as np
import matplotlib.pyplot as plt

# import custom functions
from stargen_funcs import *


# ---------------------------
# Example usage
# ---------------------------

n_samples = 1000
bins = 200
age_Gyr = 4.6

samples, x_grid, pdf = sample_from_custom_pdf(
    IMF,
    x_min=0.0005,
    x_max=100,
    n_samples=n_samples,
    n_grid=5000,
    bins=bins
)

# Plot results. Density = False makes it so that N is represented by bin height, not area.
plt.figure(figsize=(14, 8))
plt.hist(samples, bins=bins, density=False, ec='k', alpha=0.6, label=f"Sampled Distribution ({n_samples} stars)")
plt.plot(x_grid, pdf, 'r', lw=2, label="Probability Density Function (peak-matched)")

plt.xscale('log')
#plt.loglog()  # log scale for both axes

plt.title("Stellar initial mass function - frequency of stars by mass (dN/dM)")
plt.xlabel("Mass [Msol]")
plt.ylabel("Number of stars")


plt.axvline(x=MS_endmass(age_Gyr), c='green', ls='--', lw=3, label=f'Age cutoff ({age_Gyr} Gyr)')


# label spectral type mass boundaries according to Mamajek's star table:
# https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt
plt.axvline(x=0.001, c='black', ls='--', label='1 Jupiter mass')
plt.axvline(x=0.013, c='brown', ls='--', label='13 M_J deuterium limit')
plt.axvline(x=0.078, c='red', ls='--', label='M mass threshold')
plt.axvline(x=0.59, c='orange', ls='--', label='K mass threshold')
plt.axvline(x=0.90, c='gold', ls='--', label='G mass threshold')
plt.axvline(x=1.08, c='khaki', ls='--', label='F mass threshold')
plt.axvline(x=1.70, c='lightgray', ls='--', label='A mass threshold')
plt.axvline(x=2.20, c='lightblue', ls='--', label='B mass threshold')
plt.axvline(x=18, c='blue', ls='--', label='O mass threshold')

plt.legend()

plt.savefig("plots/stellar_IMF.pdf", dpi=200)
plt.show()