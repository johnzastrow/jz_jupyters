import matplotlib.pyplot as plt

import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.xaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')



plt.legend(loc='upper left')
plt.title("Ticker Plot")


# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
# blue gray = #C4D4ED
# bluer gray = #9CB9E5
# green gray = #BCD8B1

plt.grid('True')
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('ticksandaxis.png')
plt.show()
