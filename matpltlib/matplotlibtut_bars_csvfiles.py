# course from this series
# https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=3&t=0s
# make sure you open VS Code in the base folder or the paths won't work below.

from matplotlib import pyplot as plt 
import numpy as np
import csv


# in VS Code, Ctrl + / toggles line comments

plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    row = next(csv_reader)
    print(row)

# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Salary (USD)')
# plt.legend()

# plt.tight_layout() # optional to fix certain layout issues.


# plt.savefig('matpltlib/matpltut_bars.png')
# plt.show()