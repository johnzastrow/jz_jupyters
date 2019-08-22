from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# In order to represent the curved surface of the earth on a two-dimensional map, a map projection is needed. 
# Since this cannot be done without distortion, there are many map projections, each with it’s own advantages and disadvantages. 
# Basemap provides 24 different map projections. Some are global, some can only represent a portion of the globe. 
# When a Basemap class instance is created, the desired map projection must be specified, along with information about the 
# portion of the earth’s surface that the map projection will describe. There are two basic ways of doing this. One is to 
# provide the latitude and longitude values of each of the four corners of the rectangular map projection region. 
# The other is to provide the lat/lon value of the center of the map projection region along with the width and height of the 
# region in map projection coordinates.

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
# m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
#             llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

# Resolution of boundary database to use. Can be c (crude), l (low), i (intermediate), h (high), f (full) or None. 
# If None, no boundary data will be read in (and class methods such as drawcoastlines will raise an if invoked). 
# Resolution drops off by roughly 80% between datasets. Higher res datasets are much slower to draw. Default c. 
# Coastline data is from the GSHHS (http://www.soest.hawaii.edu/wessel/gshhs/gshhs.html). 
# State, country and river datasets from the Generic Mapping Tools (http://gmt.soest.hawaii.edu).

# ax = set default axes instance (default None - matplotlib.pyplot.gca() may be used to get the current axes instance). 
# If you do not want matplotlib.pyplot to be imported, you can either set this to a pre-defined axes instance, 
# or use the ax keyword in each Basemap method call that does drawing. In the first case, all Basemap method calls 
# will draw to the same axes instance. In the second case, you can draw to different axes with the same Basemap instance. 
# You can also use the ax keyword in individual method calls to selectively override the default axes instance.


# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.
map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='#EDEAE1',lake_color='#DEE6F2')
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#DEE6F2')
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))

plt.title('Filled continent background')

plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('GlobalDemoBaseMap.png')
plt.show()


# setup Lambert Conformal basemap. The following are the corners of the map for extents
# Upper left 68.57846975, -28.83201944
# lower Right 22.62373272, 61.52264668
m = Basemap(projection='merc',llcrnrlat=22,urcrnrlat=68, llcrnrlon=-28,urcrnrlon=61,lat_ts=30,resolution='l')
# draw coastlines.
m.drawcoastlines()
# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
m.drawmapboundary(fill_color='#DEE6F2')
m.drawcountries(linewidth=0.25)
# fill continents, set lake color same as ocean color.
m.fillcontinents(color='#EDEAE1',lake_color='#DEE6F2')
plt.savefig('LambertProjectDemoMap.png')
plt.show()