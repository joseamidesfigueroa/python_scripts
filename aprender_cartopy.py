import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.io.shapereader as shpreader
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import cartopy.mpl.geoaxes
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#%matplotlib inline
import numpy as np
#from vega_datasets import data as vds
from mpl_toolkits.basemap import Basemap

m1 = plt.axes(projection=ccrs.PlateCarree())
m1.coastlines()
plt.show()

fig = plt.figure()
m2 = fig.add_subplot(projection=ccrs.PlateCarree())
m2.coastlines()
plt.show()

fig = plt.figure(figsize=(14,14))
m3 = fig.add_subplot(projection=ccrs.PlateCarree())
m3.coastlines()
plt.show()

plt.figure(figsize=(12,12))
m4 = plt.axes(projection=ccrs.PlateCarree())

m4.add_feature(cfeature.LAND)
m4.add_feature(cfeature.OCEAN)
m4.add_feature(cfeature.COASTLINE)
m4.add_feature(cfeature.BORDERS, linestyle=':')
m4.add_feature(cfeature.LAKES, alpha=0.5)
m4.add_feature(cfeature.RIVERS)

m4.stock_img()
plt.show()


# latitude and longitude with east and west, etc.
plt.figure(figsize=(18, 12))
m8 = plt.axes(projection=ccrs.PlateCarree())
m8.add_feature(cfeature.LAND)
m8.add_feature(cfeature.OCEAN)
m8.add_feature(cfeature.COASTLINE)
m8.add_feature(cfeature.BORDERS, linestyle=':')
m8.add_feature(cfeature.LAKES, alpha=0.5)
m8.add_feature(cfeature.RIVERS)
m8.stock_img()
grid_lines = m8.gridlines(draw_labels=True)
grid_lines.xformatter = LONGITUDE_FORMATTER
grid_lines.yformatter = LATITUDE_FORMATTER
m8.coastlines()
plt.show()


# latitude and longitude with positive and negative
plt.figure(figsize=(18, 12))
m9 = plt.axes(projection=ccrs.PlateCarree())
grid_lines = m9.gridlines(draw_labels=True)
m9.coastlines()
plt.show()


# run time can take several minutes
# import cartopy.io.img_tiles as cimgt
plt.figure(figsize=(10,10))
stamen_terrain = cimgt.Stamen('terrain-background')
m10 = plt.axes(projection=stamen_terrain.crs)
# (x0, x1, y0, y1)
m10.set_extent([-91, -87, 12, 15], ccrs.PlateCarree()) 
grid_lines = m10.gridlines(draw_labels=True)
grid_lines.xformatter = LONGITUDE_FORMATTER
grid_lines.yformatter = LATITUDE_FORMATTER


# add map, zoom level
m10.add_image(stamen_terrain, 8)

# Agregar shape de El Salvador
shape_esa = readshapefile('/home/arw/shape/ESA_CA_wgs84','ESA_CA_wgs84')
shape = cfeature.ShapelyFeature(shape_esa, ccrs.PlateCarree())
shape_feature = cfeature.ShapelyFeature(shpreader.Reader(shape_esa).geometries(),
                                ccrs.PlateCarree(), edgecolor='black')
plt.add_feature(shape_feature, facecolor='none', edgecolor='gray') 
#m10.add_feature(shape_feature, facecolor='black')
      


plt.show()


