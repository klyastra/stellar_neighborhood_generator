# import packages
import numpy as np
import matplotlib.pyplot as plt

# import custom functions
from WD_relations import *


'''
This script is for plotting thewhite dwarf mass-radius relationships.
I made this to ensure that these mass relationships are working as intended.
'''

# Define constant
R_SOL = 695700  # km


# create array of masses (Msol); x-axis
WD_mass = np.linspace(0.01, 1.5, 1000)
x = np.linspace(0.1, 8, 1000)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

###

ax[0].plot(WD_mass, WD_mass2radius(WD_mass)*R_SOL, color='red', label='relativistic')
ax[0].plot(WD_mass, WD_mass2radius_NR(WD_mass)*R_SOL, ls='--', color='orange', label='non-relativistic', zorder=-1)
ax[0].set_xlabel("Mass [Msol]")
ax[0].set_ylabel("Radius [km]")
ax[0].set_title("White Dwarf Mass-Radius Relationship")
ax[0].grid()
ax[0].legend()

ax[1].plot(x, WD_init2final_mass(x), color='red')
ax[1].set_xlabel("Initial mass [Msol]")
ax[1].set_ylabel("Final mass [Msol]")
ax[1].set_title("White Dwarf Initial-Final Mass Relationship")
ax[1].grid()

plt.tight_layout()
plt.savefig("outputs/WD_relations.pdf", dpi=200)
plt.show()