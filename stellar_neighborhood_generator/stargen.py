# import packages
import numpy as np
import matplotlib.pyplot as plt

# import custom functions
from stargen_funcs import *


# ---------------------------
# Initial mass function (IMF)
# ---------------------------

# Starting variables to define
#age_Gyr = 13.8/2
n_samples = 1000
bins_imf = 500
bins_age = 50


samples_imf, x_grid_imf, pdf_imf = sample_from_custom_pdf(
    IMF,
    x_min=0.0005,
    x_max=100,
    n_samples=n_samples,
    n_grid=5000,
    bins=bins_imf
)

# Plot results. Density = False makes it so that N is represented by bin height, not area.
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

ax[0].hist(samples_imf, bins=bins_imf, density=False, ec='k', alpha=0.6, label=f"Sampled Distribution ({n_samples} stars)")
ax[0].plot(x_grid_imf, pdf_imf, 'r', lw=2, label="Probability Density Function (peak-matched)")

ax[0].set_xscale('log')
#plt.loglog()  # log scale for both axes

ax[0].set_title("Stellar initial mass function - frequency of stars by mass (dN/dM)")
ax[0].set_xlabel("Mass [Msol]")
ax[0].set_ylabel("Number of stars")


#ax[0].axvline(x=MS_endmass(age_Gyr), c='green', ls='--', lw=3, label=f'Age cutoff ({age_Gyr} Gyr)')


# label spectral type mass boundaries according to Mamajek's star table:
# https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt
ax[0].axvline(x=0.001, c='black', ls='--', label='1 Jupiter mass')
ax[0].axvline(x=0.013, c='brown', ls='--', label='13 M_J deuterium limit')
ax[0].axvline(x=0.078, c='red', ls='--', label='M mass threshold')
ax[0].axvline(x=0.59, c='orange', ls='--', label='K mass threshold')
ax[0].axvline(x=0.90, c='gold', ls='--', label='G mass threshold')
ax[0].axvline(x=1.08, c='khaki', ls='--', label='F mass threshold')
ax[0].axvline(x=1.70, c='lightgray', ls='--', label='A mass threshold')
ax[0].axvline(x=2.20, c='lightblue', ls='--', label='B mass threshold')
ax[0].axvline(x=18, c='blue', ls='--', label='O mass threshold')

ax[0].legend()


# ---------------------------
# Age distribution
# ---------------------------
samples_age, x_grid_age, pdf_age = sample_from_custom_pdf(
    ages_Gyr,
    x_min=0,
    x_max=13.8,  # Gyr
    n_samples=n_samples,
    n_grid=5000,
    bins=bins_age
)


ax[1].hist(samples_age, bins=bins_age, density=False, ec='k', alpha=0.6, label=f"Sampled Distribution ({n_samples} stars)")
ax[1].plot(x_grid_age, pdf_age, 'b', lw=2, label="Probability Density Function (peak-matched)")

ax[1].set_title("Stellar neighborhood age distribution (dN/dτ)")
ax[1].set_xlabel("Age [Gyr]")
ax[1].set_ylabel("Number of stars")

ax[1].legend()


###########

plt.tight_layout()
plt.savefig("plots/stellar_IMF.pdf", dpi=200)
plt.show()