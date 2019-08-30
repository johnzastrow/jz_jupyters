import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import dates as mpl_dates

# Make the figure wider to see things better
plt.figure(figsize=(15,10))

engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')

### 2017 
my_query = ''' SELECT `day_of_year`, `temp_f_davg` FROM `weather`.`v_e1248_daily` WHERE (YEAR(d_utc) = 2017) and day_of_year < 180;'''
df1 = pd.read_sql_query(my_query,engine)
tempf_vals2017 = df1['temp_f_davg']
dater = df1['day_of_year']
plt.plot(dater, tempf_vals2017, linestyle="", color="k", linewidth=1, marker='o', label="2017" )

### 2018 
my_query2018 = ''' SELECT `day_of_year`, `temp_f_davg` FROM `weather`.`v_e1248_daily` WHERE (YEAR(d_utc) = 2018) and day_of_year < 180;'''
df2018 = pd.read_sql_query(my_query2018,engine)
tempf_vals2018 = df2018['temp_f_davg']
dater = df2018['day_of_year']
plt.plot(dater, tempf_vals2018, linestyle="", color="green", linewidth=1, marker='h', label="2018" )

### 2019 
my_query2019 = ''' SELECT `day_of_year`, `temp_f_davg` FROM `weather`.`v_e1248_daily` WHERE (YEAR(d_utc) = 2019) and day_of_year < 180;'''
df2019 = pd.read_sql_query(my_query2019,engine)
tempf_vals2019 = df2019['temp_f_davg']
dater = df2019['day_of_year']
plt.plot(dater, tempf_vals2019, linestyle="", color="red", linewidth=1, marker='H', label="2019" )

plt.ylabel("Daily Avg Temp (F)")
plt.title("Daily Air Temps (F) by Day of Year")
plt.grid('True')
plt.legend(loc='upper left', shadow=True)
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('daily_temps_day_of_Year.png')
plt.show()