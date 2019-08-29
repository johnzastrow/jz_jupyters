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
# df = pd.read_sql_table("v_e1248_daily",engine)
# print(df.dtypes)
# df.tail()
# print("----------")

# d_utc              datetime64[ns]
# day_of_year                 int64
# temp_f_davg               float64
# hdd_d65                   float64
# hdd_d70                   float64
# temp_f_dmin               float64
# temp_f_dmax               float64
# windsp_mph_davg           float64
# recs                        int64


df1 = pd.read_sql_table("v_e1248_daily",engine)
tempf_vals = df1['temp_f_davg']
dater = df1['d_utc']

# Make the figure wider to see things better
plt.figure(figsize=(15,10))

plt.plot_date(dater, tempf_vals, linestyle="solid", color="#5a7d9a", linewidth=1, marker='')

# Get the current figure (gcf) and auto format the x to try to fit it better in the plot
plt.gcf().autofmt_xdate()
# reformat the date
date_format = mpl_dates.DateFormatter('%b %y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.vlines('2017-07-01', ymin=1, ymax=80, colors='#29d193', label='Construction Begins', linewidth=2)
plt.vlines('2017-09-06', ymin=1, ymax=80, colors='r', label='Construction Ends', linewidth=2)

plt.vlines('2018-01-01', ymin=1, ymax=80, colors='k', label='2018', linewidth=2)
plt.vlines('2019-01-01', ymin=1, ymax=80, colors='k', label='2019', linewidth=2)
plt.ylabel("Daily Avg Temp (F)")
plt.title("Daily Air Temps (F)")
plt.grid('True')
plt.legend()
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('daily_temps.png')
plt.show()