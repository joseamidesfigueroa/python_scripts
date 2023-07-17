import wrf
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib.cm import get_cmap
import matplotlib.colors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from netCDF4 import Dataset, num2date
from cartopy.io.shapereader import Reader


from wrf import to_np, getvar, smooth2d, get_basemap, latlon_coords, extract_times, cartopy_xlim, cartopy_ylim, latlon_coords, get_cartopy, get_cmap

# Cargar archivo netCDF de WRF
ncfile = Dataset("/home/arw/nc/wrfout_d03_2023-01-19_13:00:00")

# Obtener la temperatura en grados Celsius
temp1 = wrf.getvar(ncfile, "T2") - 273.15
temp = getvar(ncfile,"tc")
hum = getvar(ncfile, "rh2")
vv = getvar(ncfile,"wspd_wdir10", units="km h-1")[0,:]

diferencia = temp-temp1

#suaviza
temp_smooth = smooth2d(temp, 3, cenweight=4)

type(temp_smooth)

# Obtener los límites geográficos del mapa
lats, lons = wrf.latlon_coords(temp_smooth)
xlim = [lons.min(), lons.max()]
ylim = [lats.min(), lats.max()]

#Mapea el objeto
cart_proj = get_cartopy(temp_smooth)

# Crear el mapa con Cartopy
fig = plt.figure(figsize=(12,9))
#ax = plt.axes(projection=ccrs.PlateCarree())
ax = plt.axes(projection=cart_proj)
#ax.set_extent([xlim[0], xlim[1], ylim[0], ylim[1]], crs=ccrs.PlateCarree())
#ax.coastlines(resolution='10m')

# Agregar shape de El Salvador
shpfilename = '/home/arw/shape/TM_WORLD_BORDERS-0.3.shp'
ax.add_geometries(Reader(shpfilename).geometries(),
                  cart_proj,
                  facecolor='none', edgecolor='black')

# Hacer un contour plot de la temperatura

paleta=ListedColormap(['#91F1FF', '#6CC0FF', '#007FE1','#209B12','#EBF222','#FFBC00','#FF0000','#8E4C00'])

#Intento de crear una gráfica
plt.contourf(to_np(lons), to_np(lats), to_np(temp_smooth),10, cmap=get_cmap("jet"), transform=ccrs.PlateCarree())
plot_uv500 = ax.pcolormesh(lons, lats, np.sqrt(u_500**2+v_500**2), cmap=cmap)


# Agregar una barra de colores
cbar = ax.colorbar(cs, location='bottom', pad="5%")
cbar.set_label("Temperatura (C)")

# Mostrar el mapa
plt.show()
