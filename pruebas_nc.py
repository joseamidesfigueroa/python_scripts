import os
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset, num2date


#Leemos el netcdf que acabamos de bajar
nc = Dataset('wrf_prueba.nc')

#print(nc.variables)

#Lectura de latitudes y longitudes
lat = nc.variables['XLAT'][:]
zlon = nc.variables['XLONG'][:]    

temp = nc.variables['T2'][0,:,:]    
hum = nc.variables['RH02'][:]    

type(temp)

z = np.array(z)
z = z.reshape((len(x), len(y)))

#Lectura de niveles (Si los hubiere)
#nivel = nc.variables['level'][:]

#Construyendo el vector de tiempos
#Lectura y formato del tiempo
#unidades = nc.dimensions['Time']
#calendario = nc.variables['time'].calendar
#tiempo = nc.variables['Time'][:]
#tiempo = num2date(tiempo, units=unidades,calendar=calendario)
#tiempo = [i.strftime("%d-%m-%Y %H:%M") for i in tiempo]

    
#Ahora realizamos un plot simple seleccionando un tiempo
fig=plt.figure(figsize=(9,7), dpi=300)
ax=fig.add_subplot(1,1,1,projection=ccrs.Mercator())

#Esteticos
ax.set_extent([-92,-86,12,16])
ax.add_feature(cfeature.COASTLINE,lw=.5)
#ax.add_feature(cfeature.RIVERS,lw=0.5)
ax.add_feature(cfeature.BORDERS, lw=0.6)
#Cabezera
ax.set_title('Prueba netcdf')
#Lineas
ax.gridlines(xlocs=np.arange(11,15,0.5),
ylocs=np.arange(-90,-87,0.5),
draw_labels=True,color='gray',lw=0.1)

pc=ax.contourf(zlon,lat,temp,
#levels=levels_pm10,
transform=ccrs.PlateCarree(), 
#cmap='twilight',)
cmap='Reds')
cbar = fig.colorbar(pc, orientation="horizontal")

#fig.savefig("cams_pm10_"+f'{i}'+".png")
#plt.close(fig) 
plt.show()