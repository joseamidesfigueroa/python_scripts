import netCDF4
import matplotlib.colors                                     # Matplotlib colors
import cartopy, cartopy.crs as ccrs                          # Plot maps
import cartopy.io.shapereader as shpreader                   # Import shapefiles
import matplotlib.pyplot as plt
import numpy as np  
import shapefile as shp

#Carga el mapa
sf = shp.Reader("//home/arw/shape/TM_WORLD_BORDERS-0.3.shp")

#Carga el netcdf
nc="/home/arw/trabajo/nc/rtofs_recortado_f01.nc"

#Lee elnetcdf
file = netCDF4.Dataset(nc)

#Identifico y asigno las latitudes
lats  = file.variables['Latitude'][:]

#Identifico y asigno las longitudes
lons  = file.variables['Longitude'][:]

#Asigno la variable que quiero analizar
data = file.variables['sst'][ : , : , : ]

#Quito la proyección de la variable para su uso más facil con imshow
data = data.squeeze()

#Comienzo el plot
#------------------------------------------------
#Roto los datos ya que están al reves
data = np.flipud(data)
#Creo la figura según el tamaño que requiera
fig = plt.figure(figsize=(12.8, 7.2))
#Defino los límites 
limites = [-120,-60,0,30]
ax = plt.axes()
img = ax.imshow(data,cmap='jet', extent=limites)
plt.show()
#plt.savefig('test.png')
#------------------------------------------------


#Hacia GeoTiff
#Importa las librerias a utilizar
#------------------------------------------------
import xarray as xr 
import rioxarray as rio 



nc_paraGT=xr.open_dataset("/home/arw/trabajo/nc/rtofs_recortado_f01.nc")
nc_paraGT

bT = nc_paraGT['sst']


bT = bT.rio.set_spatial_dims(x_dim='X', y_dim='Y')
bT.rio.crs
bT.rio.write_crs("epsg:4326", inplace=True)
bT.rio.to_raster(r"ssh.tiff")

#------------------------------------------------
