import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import dates as mpl_dates
import seaborn as sns


engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')

# data object testing
# query = '''show tables'''
# df = pd.read_sql_query(query,engine)
# df = pd.read_sql_table("v_daily_electric",engine)
# print(df.dtypes)
# df.tail()
# print("----------")

# d_local    datetime64[ns]
# d_kwh             float64
# recs                int64
# dtype: object
# ----------


df1 = pd.read_sql_table("v_daily_electric",engine)
elecusage_vals = df1['d_kwh']
dater = df1['d_local']

# Make the figure wider to see things better
plt.figure(figsize=(15,10))

plt.plot_date(dater, elecusage_vals, linestyle="solid", color="#5a7d9a", linewidth=1, marker='')

# Get the current figure (gcf) and auto format the x to try to fit it better in the plot
plt.gcf().autofmt_xdate()
# reformat the date
date_format = mpl_dates.DateFormatter('%b %Y')
plt.gca().xaxis.set_major_formatter(date_format)

# to add vertical lines
# xcoords = [0.22058956, 0.33088437, 2.20589566]
# for xc in xcoords:
#     plt.axvline(x=xc)

# You can use many of the keywords available for other plot commands (e.g. color, linestyle, linewidth ...). 
# You can pass in keyword arguments ymin and ymax if you like in axes corrdinates (e.g. ymin=0.25, ymax=0.75
#  will cover the middle half of the plot). 
# There are corresponding functions for horizontal lines (axhline) and rectangles (axvspan). 

plt.vlines('2017-07-01', ymin=1, ymax=80, colors='#29d193', label='Construction Begins', linewidth=2)
plt.vlines('2017-09-06', ymin=1, ymax=80, colors='r', label='Construction Ends', linewidth=2)
plt.ylabel("Electric Usage (kwh)")
plt.title("Daily Electrical Usage")
plt.grid('True')
plt.legend()
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('daily_electric.png')
plt.show()

# sns.set()
# plt.figure(figsize=(10, 6), dpi= 80, facecolor='w', edgecolor='k')
# plt.subplot(2,1,1)
# sns.boxplot(x="d_local", y="d_kwh", data=df1)
# plt.ylabel("ytrty")
# plt.figure(figsize=(10, 6), dpi= 80, facecolor='w', edgecolor='k')
# plt.subplot(2,1,2)
# sns.violinplot(x="d_local", y="d_kwh", data=df1)
# plt.ylabel("868  u8666u67")
# plt.tight_layout()
# plt.show()

# sns.set()
# plt.figure(figsize=(10, 6), dpi= 80, facecolor='w', edgecolor='k')
# # plt.subplot(2,1,1)
# sns.boxplot(x="d_local", y="d_kwh", data=df1)
# plt.ylabel("ytrty")
# # plt.figure(figsize=(10, 6), dpi= 80, facecolor='w', edgecolor='k')
# # plt.subplot(2,1,2)
# # sns.violinplot(x="d_local", y="d_kwh", data=df1)
# # plt.ylabel("868  u8666u67")
# plt.tight_layout()
# plt.show()