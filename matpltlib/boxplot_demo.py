import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
print(spread)
print("----------")
print(flier_high)
print("~~~~~~~~~~~~~~~~~~~~~~")
print(flier_low)
print("~~~~~~~~~~~~~~~~~~~~~~")
print(center)

# matplotlib.pyplot.boxplot(x, notch=None, sym=None, vert=None, 
# whis=None, positions=None, widths=None, patch_artist=None, 
# bootstrap=None, usermedians=None, conf_intervals=None, 
# meanline=None, showmeans=None, showcaps=None, showbox=None, 
# showfliers=None, boxprops=None, labels=None, flierprops=None, 
# medianprops=None, meanprops=None, capprops=None, 
# whiskerprops=None, manage_ticks=True, 
# autorange=False, zorder=None, *, data=None)[source]

fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(data, boxprops=None, showfliers=False)
plt.grid("True")
plt.tight_layout()  # optional to fix certain layout issues.
plt.savefig("boxplot1.png")
plt.show()
