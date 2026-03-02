# import packages
import numpy as np
import matplotlib.pyplot as plt

# import custom functions
from MLRT_relations import *


'''
This script is for plotting the main-sequence mass relationships with luminosity, radius, and temperature.
I made this to ensure that these mass relationships are working as intended,
and that they match results of Eker et al. (2018)
'''



# create array of masses (Msol); x-axis
x = np.linspace(0.05, 50, 1000)

fig, ax = plt.subplots(3, 2, figsize=(12, 9))

###

ax[0,0].plot(x, MS_mass2lum(x), color='orange')
ax[0,0].set_xlabel("Mass [Msol]")
ax[0,0].set_ylabel("Luminosity [Lsol]")
ax[0,0].set_title("Mass-Luminosity")

ax[0,1].plot(x, MS_mass2lum(x), color='orange')
ax[0,1].set_xlabel("log Mass [log(M/Msol)]")
ax[0,1].set_ylabel("log Luminosity [log(L/Lsol)]")
ax[0,1].loglog()
ax[0,1].set_title("Mass-Luminosity (log scale)")

###

ax[1,0].plot(x, MS_mass2radius(x), color='purple')
ax[1,0].set_xlabel("Mass [Msol]")
ax[1,0].set_ylabel("Radius [Rsol]")
ax[1,0].set_title("Mass-Radius")

ax[1,1].plot(x, MS_mass2radius(x), color='purple')
ax[1,1].set_xlabel("log Mass [log(M/Msol)]")
ax[1,1].set_ylabel("log Radius [log(R/Rsol)]")
ax[1,1].loglog()
ax[1,1].set_title("Mass-Radius (log scale)")

###

ax[2,0].plot(x, MS_mass2temp(x), color='g')
ax[2,0].set_xlabel("Mass [Msol]")
ax[2,0].set_ylabel("Temperature [K]")
ax[2,0].set_title("Mass-Temperature")

ax[2,1].plot(x, MS_mass2temp(x), color='g')
ax[2,1].set_xlabel("log Mass [log(M/Msol)]")
ax[2,1].set_ylabel("log Temp [log(T/Tsol)]")
ax[2,1].loglog()
ax[2,1].set_title("Mass-Temperature (log scale)")


plt.suptitle("Main-Sequence Mass Relationships: Luminosity, Radius, Temperature\n(based on Eker et al. 2018)", fontsize=16)
plt.tight_layout()
plt.show()
plt.savefig("outputs/MLT_relations.pdf", dpi=200)