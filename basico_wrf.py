import pandas as ps
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import glob
import matplotlib as mpl
import matplotlib.colors as colors
import matplotlib.ticker as ticker
import shapefile as shp
import cartopy.crs as ccrs
import cartopy.feature as cfeature

df = xr.open_dataset('wrf_prueba.nc')

sf = shp.Reader('C:/R/shapes/ESA_CA_wgs84.shp')

temp = df['T2'][0,:,:]-273.15
print(temp.values)
print(df.variables)

hum = df['RH02'][0,:,:]

temp2 = temp*hum

df_lat = df['XLAT'][0,:,0]
print(df_lat.values)

df_lon = df['XLONG'][0,0,:]
print(df_lon.values)

X, Y = np.meshgrid(df_lon, df_lat)

shp = gpd.read_file('C:/R/shapes/ESA_CA_wgs84.shp')

fig, ax = plt.subplots(figsize=(12,10))
cont = ax.contourf(X,Y, temp2, cmap='jet', extend='both')
cbar = fig.colorbar(cont,ax=ax)
cbar.set_label("Mapa de prueba", labelpad = +1, fontsize=18)

ax.set_title('Titulo del mapa')
ax.set_xlabel("Longitud", fontsize=18)
ax.set_ylabel("Latitud", fontsize=18)

ax.set_ylim(min(df_lat).values,max(df_lat).values)
ax.set_xlim(min(df_lon).values,max(df_lon).values)


plt.grid()
plt.tight_layout()
shp.plot(ax=ax, color='black')
plt.show()
