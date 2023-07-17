from mpl_toolkits.basemap import Basemap
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import cartopy as ax
from pylab import *
import netCDF4

plt.figure()

nc="/home/arw/trabajo/nc/rtofs_glo_2ds_f001_prog.nc"
file = netCDF4.Dataset(nc)
lat  = file.variables['Latitude'][:]
lon  = file.variables['Longitude'][:]
data = file.variables['sst'][:]
data = file.variables['sst'][ : , : , : ]
#data = file.variables['sst'][:1]
file.close()

lon = np.where(np.greater_equal(lon,500),np.nan,lon)

m=Basemap(projection='mill',lat_ts=10, \
  llcrnrlon=np.nanmin(lon),urcrnrlon=np.nanmax(lon), \
  llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
  resolution='c')

Lon, Lat = meshgrid(lon,lat, sparse=True)
x, y = m(Lon,Lat)

#------------------------------------------------
#Mi intento  de grafica

c_scheme = mp

#------------------------------------------------


#cs = m.pcolormesh(x,y,data,shading='flat', cmap=plt.cm.jet)
cs = ax.imshow(data,cmap='jet')



data = data.squeeze()
data = np.flipud(data)
fig = plt.figure(figsize=(12.8, 7.2))
proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(12.8, 7.2))
ax = plt.axes()
img = ax.imshow(data,cmap='jet')
plt.savefig('test.png')


m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()
m.drawparallels(np.arange(-90.,120.,30.), \
  labels=[1,0,0,0])
m.drawmeridians(np.arange(-180.,180.,60.), \
  labels=[0,0,0,1])

colorbar(cs)
plt.title('Example 2: Global RTOFS SST from NetCDF')
plt.show()





#--------------------------------------------------->
