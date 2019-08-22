import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import dates as mpl_dates
import matplotlib.dates as mdates

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')

# the data have columns of the following: 
# YEARMONTH                    object
# NORM_DATE            datetime64[ns]
# monthly_elec_use            float64
# monthly_gas_use             float64
# monthly_tot_utils           float64


df1 = pd.read_sql_table("v_monthly_utilities",engine)
uniqx = df1['YEARMONTH']
gasusage_vals = df1['monthly_gas_use']
elecusage_vals = df1['monthly_elec_use']
dater = df1['NORM_DATE']

# Here's the meat. Now we make two Y axis objects
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax1.plot_date(dater,gasusage_vals, linestyle="solid", linewidth=1, color="#5a7d9a", markersize=4, marker="s")
ax2.plot_date(dater, elecusage_vals, linestyle="solid", color="red", markersize=5, marker="h", label="Elec Usage, kw")
ax1.set_ylabel("Gas usage (cu ft)",fontsize=9,color='#5a7d9a')
ax2.set_ylabel("Electric Usage (kwh)",fontsize=9,color='red')



# Get the current figure (gcf) and auto format the x to try to fit it better in the plot
plt.gcf().autofmt_xdate()
# reformat the date
date_format = mpl_dates.DateFormatter('%m-%Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.ylabel("Gas usage (cu ft) and Electric Usage (kwh)")
plt.title("Monthly Heat Utility Usage")

plt.grid('True')
plt.title('Bugger off')
plt.legend(loc='upper center', shadow=True)
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('two_y_axis.png')
plt.show()