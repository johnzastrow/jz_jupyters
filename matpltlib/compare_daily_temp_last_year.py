import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd
import sqlalchemy

# import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


engine = sqlalchemy.create_engine(
    "mysql+pymysql://jcz:yub.miha@192.168.1.110:3306/weather"
)

# data object testing
# query = '''show tables'''
# df = pd.read_sql_query(query,engine)
# df = pd.read_sql_table("E1248",engine)
# print(df.dtypes)
# df.tail()
# print("----------")

# id                        int64
# dt_utc           datetime64[ns]
# pressure_mbar           float64
# temp_f                  float64
# dewpoint_f              float64
# humid_perc              float64
# windsp_mph              float64
# windir_deg              float64
# a_press_mbar            float64
# a_temp_f                float64
# a_dewp_f                float64
# a_humid_perc            float64
# a_windsp_mph            float64
# a_windir_deg            float64
# ts               datetime64[ns]
# dtype: object

query1 = """select id, DAYOFYEAR(CAST(`dt_utc` AS DATE)) AS `day_of_year`, temp_f, pressure_mbar, dewpoint_f FROM E1248 WHERE DATE(dt_utc) BETWEEN CURDATE() - INTERVAL 10 DAY AND CURDATE() and temp_f <> 0 """
df1 = pd.read_sql_query(query1, engine)
temp_f_vals = df1["temp_f"]
dater = df1["day_of_year"]


query2 = """SELECT id, DAYOFYEAR(CAST(`dt_utc` AS DATE)) AS `day_of_year`, temp_f, pressure_mbar, dewpoint_f FROM E1248 WHERE DATE(dt_utc) BETWEEN CURDATE() - INTERVAL 375 DAY AND CURDATE() - INTERVAL 365 DAY AND temp_f <> 0 """
df2 = pd.read_sql_query(query2, engine)
temp_f_vals2 = df2["temp_f"]
dater2 = df2["day_of_year"]

fig, ax1 = plt.subplots()

ax1.plot(dater, temp_f_vals, linestyle="solid", linewidth=1, color="#5a7d9a", markersize=0, marker="s", label="This year")
ax1.plot(dater2, temp_f_vals2, linestyle="solid", color="red", markersize=0, marker="h", linewidth=4, alpha=0.4, label="Last year")
ax1.set_ylabel("Hourly Temp F", fontsize=9, color='#5a7d9a')

plt.title("Hourly Temps")
plt.grid("True")
plt.legend()
plt.tight_layout()  # optional to fix certain layout issues.
plt.savefig("compare_to_last_year.png")
plt.show()
