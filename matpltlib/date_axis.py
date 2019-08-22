import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import dates as mpl_dates
import matplotlib.dates as mdates

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

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

df1 = pd.read_sql_table("v_monthly_utilities",engine)

uniqx = df1['YEARMONTH']
gasusage_vals = df1['monthly_gas_use']
elecusage_vals = df1['monthly_elec_use']
dater = df1['NORM_DATE']

# Here's the meat. Now we make two Y axis objects
fig, ax = plt.subplots()

# format the ticks and labels
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.tick_params(axis='x', which='major', grid_linewidth='2', grid_color='#CCCCCC', grid_alpha=0.2)
ax.tick_params(axis='x', which='major', labelsize=9, labelcolor='#AAAAAA', pad=3, labelrotation=90)
ax.tick_params(axis='y', which='both', labelsize=9)
ax.tick_params(axis='both', which='minor', labelsize=7)

# Possible tick_params values
# 'size', 'width', 'color', 'tickdir', 'pad', 'labelsize', 'labelcolor', 
# 'zorder', 'gridOn', 'tick1On', 'tick2On', 'label1On', 'label2On', 'length', 
# 'direction', 'left', 'bottom', 'right', 'top', 'labelleft', 'labelbottom', 
# 'labelright', 'labeltop', 'labelrotation', 'grid_agg_filter', 'grid_alpha', 
# 'grid_animated', 'grid_antialiased', 'grid_clip_box', 'grid_clip_on', 
# 'grid_clip_path', 'grid_color', 'grid_contains', 'grid_dash_capstyle', 
# 'grid_dash_joinstyle', 'grid_dashes', 'grid_drawstyle', 'grid_figure', 
# 'grid_fillstyle', 'grid_gid', 'grid_in_layout', 'grid_label', 'grid_linestyle', 
# 'grid_linewidth', 'grid_marker', 'grid_markeredgecolor', 'grid_markeredgewidth', 
# 'grid_markerfacecolor', 'grid_markerfacecoloralt', 'grid_markersize', 
# 'grid_markevery', 'grid_path_effects', 'grid_picker', 'grid_pickradius',
#  'grid_rasterized', 'grid_sketch_params', 'grid_snap', 'grid_solid_capstyle', 
#  'grid_solid_joinstyle', 'grid_transform', 'grid_url', 'grid_visible', 
#  'grid_xdata', 'grid_ydata', 'grid_zorder', 'grid_aa', 'grid_c', 'grid_ds', 
# 'grid_ls', 'grid_lw', 'grid_mec', 'grid_mew', 'grid_mfc', 'grid_mfcalt', 'grid_ms'

goodlabels = ["Gas Usage, cu ft","Elec Usage, kw"] # optional way to control labels
goodcolors = ['#C4D4ED','#9CB9E5','#BCD8B1'] # optional way to control colors
plt.stackplot(dater,gasusage_vals,elecusage_vals, labels=goodlabels, colors=goodcolors)

# reformat the date
year_format = mpl_dates.DateFormatter('%Y')
plt.gca().xaxis.set_major_formatter(year_format)
month_format = mpl_dates.DateFormatter('%m')
plt.gca().xaxis.set_minor_formatter(month_format)
# These do work to change label sizes, but we'll try adjusting ax since that's what we're doing here
# plt.tick_params(axis='both', which='minor', labelsize=8)
# plt.tick_params(axis='both', which='major', labelsize=10)

plt.ylabel("Gas usage (cu ft) and Electric Usage (kwh)", fontsize=9,color='#5a7d9a')
plt.title("Monthly Heat Utility Usage Data Axis Example")
plt.legend(loc='upper center', shadow=True)

plt.grid('True')
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('date_axis.png')
plt.show()