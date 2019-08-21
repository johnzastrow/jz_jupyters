# course from this series
# https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=3&t=0s
# make sure you open VS Code in the base folder or the paths won't work below.

from matplotlib import pyplot as plt 
import numpy as np
import os 


# plt.style.available
# https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html
# plt.style.use('classic')

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]


py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

x_indexes = np.arange(len(ages_x))
barwidth = 0.25


# Use the array created from the x values and to scoot the bars one way or the other so they
# don't just lay on top of each other. Use the barwdith variable as an arbitrary value to set 
# both width and the bar offsets. Use math in the .bar arguments to adjust offsets. Add or 
# subtract values to add some padding between the bars too.

plt.bar(x_indexes - barwidth - 0.01, dev_y, width=barwidth, color='k', label='All Devs') # k-- formats the line 

plt.bar(x_indexes, py_dev_y, width=barwidth, color='#5a7d9a', label='Python only')

plt.bar(x_indexes + barwidth + 0.01, js_dev_y, width=barwidth, color='#adad3b', label='Javascript only')

plt.grid('True')

# Using numpy array to set the x axis allowing us to shift it for the bars, then sets the values
# to the array index. Use xticks to re-assign the true values to the x axis.

plt.xticks(ticks=x_indexes, labels=ages_x)
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Salary (USD)')
plt.legend()

plt.tight_layout() # optional to fix certain layout issues.

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

# mak
plt.savefig('matpltut_bars.png')
plt.show()