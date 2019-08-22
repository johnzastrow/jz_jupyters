# SQLite dataset
# We create a simple dataset using this code:

import sqlite3 as lite
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Don't create the database if it exists. Uncomment the sections below if it doesn't
# create the database. Uncomment below.
con = lite.connect('map_data.db')
 
# insert some data. Uncomment below.
# with con:
#     cur = con.cursor()    
#     cur.execute("CREATE TABLE Places(id INTEGER PRIMARY KEY, country TEXT, Places INT, center_lat real, center_long real)")
#     cur.execute("INSERT INTO Places VALUES(NULL,'Germany',81197537, 48.77710549, 9.11677075)")
#     cur.execute("INSERT INTO Places VALUES(NULL,'France', 66415161, 48.91291265, 2.21997772)")
#     cur.execute("INSERT INTO Places VALUES(NULL,'Hungary', 46439864, 47.52549896, 19.04276840)")
#     cur.execute("INSERT INTO Places VALUES(NULL,'Italy', 60795612, 42.03804167, 12.50358686)")
#     cur.execute("INSERT INTO Places VALUES(NULL,'Spain', 46439864, 40.36413496, -3.61373196)")

# convert the coords into float numbers
cur = con.cursor()
coords = cur.execute("""
select cast(center_long as float),
cast(center_lat as float)
from Places;""").fetchall()

results = cur.fetchall()
print(results)


# Setup the basemap
# setup Lambert Conformal basemap. The following are the corners of the map for extents
# Upper left 68.57846975, -28.83201944
# lower Right 22.62373272, 61.52264668
# m = Basemap(projection='merc',llcrnrlat=22,urcrnrlat=68, llcrnrlon=-28,urcrnrlon=61,lat_ts=30,resolution='l')
m = Basemap(projection='merc',llcrnrlat=22,urcrnrlat=68, llcrnrlon=-28,urcrnrlon=61,lat_ts=30,resolution='l')
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
# draw coastlines.
m.drawcoastlines()
# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
m.drawmapboundary(fill_color='#DEE6F2')
m.drawcountries(linewidth=0.25)
# fill continents, set lake color same as ocean color.
m.fillcontinents(color='#EDEAE1',lake_color='#DEE6F2')

# x, y = m(
# [l[0] for l in coords],
# [l[1] for l in coords])
# m.scatter(x, y, 1, marker='o', color='red')

# samples data
NYClat, NYClon = 40.7127, -74.0059
xpt, ypt = m(NYClon, NYClat)
m.plot(xpt, ypt, 'c*', markersize=15)

LAlat, LAlon = 34.05, -118.25
xpt, ypt = m(LAlon, LAlat)
m.plot(xpt, ypt, 'g^', markersize=15)

plt.savefig('EuropePlaceMap.png')
plt.show()

# As you can see, the results are formatted as a list of tuples. Each tuple corresponds to a row in the database that we accessed. 
# Before we move on, it’s good practice to close Connection objects and Cursor objects that are open. 
# This prevents the SQLite database from being locked. When a SQLite database is locked, you may be 
# unable to update the database, and may get errors. We can close the Cursor and the Connection like this:

cur.close()
con.close()