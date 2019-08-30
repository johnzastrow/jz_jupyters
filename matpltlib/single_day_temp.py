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

query = """select id, dt_utc, temp_f, pressure_mbar, dewpoint_f FROM E1248 WHERE DATE(dt_utc) BETWEEN CURDATE() - INTERVAL 2 DAY AND CURDATE() and temp_f <> 0 """
df1 = pd.read_sql_query(query, engine)
# df1 = pd.read_sql_table("E1248", engine)
temp_f_vals = df1["temp_f"]
dater = df1["dt_utc"]

# Make the figure wider to see things better
plt.figure(figsize=(15, 10))

plt.plot_date(
    dater, temp_f_vals, linestyle="solid", color="#5a7d9a", linewidth=1, marker=""
)

# Get the current figure (gcf) and auto format the x to try to fit it better in the plot
plt.gcf().autofmt_xdate()
# reformat the date
date_format = mpl_dates.DateFormatter("%b %Y")
plt.gca().xaxis.set_major_formatter(date_format)

# to add vertical lines
# xcoords = [0.22058956, 0.33088437, 2.20589566]
# for xc in xcoords:
#     plt.axvline(x=xc)

# You can use many of the keywords available for other plot commands (e.g. color, linestyle, linewidth ...).
# You can pass in keyword arguments ymin and ymax if you like in axes corrdinates (e.g. ymin=0.25, ymax=0.75
#  will cover the middle half of the plot).
# There are corresponding functions for horizontal lines (axhline) and rectangles (axvspan).

# plt.vlines(
#     "2017-07-01",
#     ymin=1,
#     ymax=80,
#     colors="#29d193",
#     label="Construction Begins",
#     linewidth=2,
# )
# plt.vlines(
#     "2017-09-06", ymin=1, ymax=80, colors="r", label="Construction Ends", linewidth=2
# )
plt.ylabel("Temperature")
plt.title("Hourly Temps")
plt.grid("True")
plt.legend()
plt.tight_layout()  # optional to fix certain layout issues.
plt.savefig("hourly_temps.png")
plt.show()
