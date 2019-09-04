import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import dates as mpl_dates
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

# Make the figure wider to see things better
plt.figure(figsize=(15,10))

engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')

### 2017 
my_query2017 = ''' SELECT `WEEKW`, `w_temp_f_avg` FROM `weather`.`v_e1248_weekly` WHERE (YEARY = 2017);'''
df1 = pd.read_sql_query(my_query2017,engine)
tempf_vals2017 = df1['w_temp_f_avg']
dater2017 = df1['WEEKW']
plt.plot(dater2017, tempf_vals2017, linestyle="", color="red", linewidth=1, marker='o', label="2017", markersize=8)

### 2018 
my_query2018 = ''' SELECT `WEEKW`, `w_temp_f_avg` FROM `weather`.`v_e1248_weekly` WHERE (YEARY = 2018);'''
df2018 = pd.read_sql_query(my_query2018,engine)
tempf_vals2018 = df2018['w_temp_f_avg']
dater2018 = df2018['WEEKW']
plt.plot(dater2018, tempf_vals2018, linestyle="", color="green", linewidth=1, marker='o', label="2018", markersize=6 )

### 2019 
my_query2019 = ''' SELECT `WEEKW`, `w_temp_f_avg` FROM `weather`.`v_e1248_weekly` WHERE (YEARY = 2019);'''
df2019 = pd.read_sql_query(my_query2019,engine)
tempf_vals2019 = df2019['w_temp_f_avg']
dater2019 = df2019['WEEKW']
plt.plot(dater2019, tempf_vals2019, linestyle="", color="blue", linewidth=1, marker='o', label="2019", markersize=4 )

# fig, ax = plt.subplots()
# ax.xaxis.set_minor_locator(AutoMinorLocator())
plt.ylabel("Weekly Avg Temp (F)")
plt.title("Weekly Air Temps (F) by Day of Year")
plt.grid('True')
plt.legend(loc='upper left', shadow=True)
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('weekly_temps_compare_years.png')
plt.show()