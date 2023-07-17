from netCDF4 import Dataset, num2date
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from mpl_toolkits.basemap import Basemap
import pandas as pd
import pyproj
from pyproj import Proj
import numpy as np

from wrf import to_np, getvar, smooth2d, get_basemap, latlon_coords, extract_times

#Carga el netcdf
ncfile = Dataset("/home/arw/nc/wrfout_d03_2023-01-19_13:00:00")

# Define la proyección mercator
mercator = Proj(proj='merc', lat_ts=0, lat_0=0, lon_0=0, x_0=0, y_0=0)

#Extrae las variables
temp = getvar(ncfile,"tc")

#Aplico la proyección Mercator
x, y = latlon_coords(temp)


hum = getvar(ncfile, "rh2",meta=True)
vv = getvar(ncfile,"wspd_wdir10", units="km h-1", meta=True)[0,:]

#tiempo = getvar(ncfile, "times"smooth2d--------------------->
##Índice por calor
##Define las constantes y relaciones
a=-8.78469476
b=1.61139411
c=2.338548839
d=0.14611605
e=0.012308094
f=0.016424828
g=0.002211732
h=0.00072546
i=0.000003582
B1=b*temp
C1=c*hum
#Multiplico dos arreglos
CC1 = np.multiply(temp,hum)
D1=d*CC1
DD1=np.power(temp,2)
E1=e*DD1
EE1=np.power(hum,2)
F1=f*EE1
FF1=np.multiply(np.power(temp,2),hum)
G1=g*FF1
GG1=np.multiply(np.power(hum,2),temp)
H1=h*GG1
HH1=np.multiply(np.power(hum,2),np.power(temp,2))
I1=i*HH1
ST=a+B1+C1-D1-E1-F1+G1+H1-I1

##--------------------------------------------------->
#else:
##--------------------------------------------------->
##Indice por viento
#
#    a=13.1267
#    b=0.6215
#    c=11.37
#    d=0.3965
#
#    B1=b*temp
#    V=pow(vv,0.16)
#
#    C1=c*V
#    D1=d*temp*V
#
#    ST=(a+B1-C1+D1)
##--------------------------------------------------->
#
## Se suaviza
smooth_slp = smooth2d(temp, 3, cenweight=4)

## Obtiene las coordenadas de latitud y longitud
lats, lons = latlon_coords(smooth_slp)

# Se genera un objeto mapa 
bm = get_basemap(smooth_slp)

# Se crea la figura
fig = plt.figure(figsize=(12,9))

#bm.drawcoastlines(linewidth=0.25)

# Se añade un shapefile
bm.readshapefile('/home/arw/shape/ESA_CA_wgs84','ESA_CA_wgs84')

# Convert the lats and lons to x and y.  Make sure you convert the lats and
# lons to numpy arrays via to_np, or basemap crashes with an undefined
# RuntimeError.
x, y = bm(to_np(lons), to_np(lats))

# Draw the contours and filled contours
bm.contour(x, y, to_np(smooth_slp), 8, colors="black", linewidths=0.25)
bm.contourf(x, y, to_np(temp), 8, colors=['#91F1FF', '#6CC0FF', '#007FE1','#209B12','#EBF222','#FFBC00','#FF0000','#8E4C00'],)

# Add a color bar
plt.colorbar(shrink=.62)

plt.title("Confort térmico valido para las: "+tiempo+" (UTC)")

plt.show()