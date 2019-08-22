import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import dates as mpl_dates

engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')

# data object testing
# query = '''show tables'''
# df = pd.read_sql_query(query,engine)
# df = pd.read_sql_table("v_monthly_utilities",engine)
# print(df.dtypes)
# df.tail()
# print("----------")

# the data have columns of the following: 
# YEARMONTH                    object
# NORM_DATE            datetime64[ns]
# monthly_elec_use            float64
# monthly_gas_use             float64
# monthly_tot_utils           float64


df1 = pd.read_sql_table("v_monthly_utilities",engine)
# pandas needs an ID, we'll use the data of the measurements
# here we are setting up the X and Y on the chart
uniqx = df1['YEARMONTH']
gasusage_vals = df1['monthly_gas_use']
elecusage_vals = df1['monthly_elec_use']
dater = df1['NORM_DATE']

# Make the figure wider to see things better
plt.figure(figsize=(15,10))


# Use the array created from the x values and to scoot the bars one way or the other so they
# don't just lay on top of each other. Use the barwdith variable as an arbitrary value to set 
# both width and the bar offsets. Use math in the .bar arguments to adjust offsets. Add or 
# subtract values to add some padding between the bars too.

# x_indexes = np.arange(len(uniqx))
# barwidth = 0.25

plt.plot_date(dater, gasusage_vals, linestyle="solid", color="#5a7d9a")
plt.plot_date(dater, elecusage_vals, linestyle="solid", color="red")
# plt.bar('x_indexes','gasusage_vals',width=barwidth, color="#5a7d9a", label="Gas Usage (cu ft)")
# plt.bar('x_indexes','gas_usage',width=barwidth, color="#5a7d9a", data=df1, label="Gas Usage (cu ft)")

# Get the current figure (gcf) and auto format the x to try to fit it better in the plot
plt.gcf().autofmt_xdate()
# reformat the date
date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.xlabel("Year and Month")
plt.ylabel("Gas usage (cu ft) and Electric Usage (kwh)")
plt.title("Monthly Heat Utility Usage")
plt.grid('True')
plt.legend()
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('gas_usage_more_complex.png')
plt.show()



goodlabels = ["Gas Usage, cu ft","Elec Usage, kw"] # optional way to control labels
goodcolors = ['#C4D4ED','#9CB9E5','#BCD8B1'] # optional way to control colors
plt.stackplot(dater,gasusage_vals,elecusage_vals, labels=goodlabels, colors=goodcolors)
plt.gcf().autofmt_xdate()
# reformat the date
date_format = mpl_dates.DateFormatter('%b, %y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.xlabel("Year and Month")
plt.ylabel("Gas usage (cu ft) and Electric Usage (kwh)")
plt.title("Monthly Heat Utility Usage")
plt.legend(loc='upper center', shadow=True)


# Creating a second Y axis
# xer = np.arange(0, 10, 0.1)
# y1 = 0.05 * xer**2
# y2 = -1 *y1

# fig, ax1 = plt.subplots()

# ax2 = ax1.twinx()
# ax1.plot(xer, y1, 'g-')
# ax2.plot(xer, y2, 'b-')

# ax1.set_xlabel('X data')
# ax1.set_ylabel('Y1 data', color='g')
# ax2.set_ylabel('Y2 data', color='b')

plt.grid('True')
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('energystackplot.png')
plt.show()