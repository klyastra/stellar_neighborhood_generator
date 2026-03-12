# import packages
import numpy as np
import matplotlib.pyplot as plt

# import custom functions
from stargen_funcs import *
from star_class import Star


# ---------------------------
# Initial mass function (IMF)
# ---------------------------

# Starting variables to define
#age_Gyr = 13.8/2
n_samples = 1000
bins_imf = 500
bins_age = 50

# The RNG seed is manually inputted by user
seed = input("Enter a integer for the RNG seed: ")

if is_integer(seed) == True:
    print("You entered: " + seed)
    seed = int(seed)  # convert string to int
if is_integer(seed) == False:
    print("Your seed is invalid because it is not an integer. Moving on using a default seed of 0...")
    seed = 0

# Begin generating stars
samples_imf, x_grid_imf, pdf_imf = sample_from_custom_pdf(
    IMF,
    x_min=0.0005,
    x_max=100,
    n_samples=n_samples,
    n_grid=5000,
    bins=bins_imf,
    seed=seed
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



# ---------------------------
# Save results to output
# ---------------------------

# Save plot 

plt.tight_layout()
plt.savefig("outputs/IMF+ages.pdf", dpi=200)
plt.show()


# Save samples as CSV
### Use the class "Star" to create a list of stars
import pandas as pd

samples_stage, samples_spT, samples_radii, samples_temp, samples_lum = [], [], [], [], []
samples_remnantage, samples_finalmass = [], []

for i in range(n_samples):
    star = Star(f"Star {i+1}", samples_imf[i], samples_age[i])

    samples_stage.append(star.evol_stage)
    samples_spT.append(star.spectral_type)
    samples_radii.append(star.radius)
    samples_temp.append(star.temperature)
    samples_lum.append(star.luminosity)
    
    samples_remnantage.append(star.remnant_age)
    samples_finalmass.append(star.final_mass)

# Compile all 1D arrays as columns of pandas dataframe table
output = {
    'Initial mass [Msol]': samples_imf,
    'Age [Gyr]': samples_age,
    'Evolutionary stage': samples_stage,
    'Spectral type': samples_spT,
    'Radii [Rsol]': samples_radii,
    'Temperature': samples_temp,
    'Luminosity [Lsol]': samples_lum,
    'Remnant age [Gyr]': samples_remnantage,
    'Final mass [Msol]': samples_finalmass,
}

df = pd.DataFrame(output)

# Export the DataFrame to a CSV file named 'output_data.csv'
df.to_csv('outputs/output.csv', sep='\t', index=False)  # tab delimiter to separate columns

print(f"Samples of {n_samples} stars have been saved to the 'outputs' folder.")
