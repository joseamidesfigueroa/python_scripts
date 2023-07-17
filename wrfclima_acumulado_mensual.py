#Se importan las librerias necesarias
import pandas as ps
import geopandas as gpd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import xarray as xr
import matplotlib as mpl
import matplotlib.colors as colors
import matplotlib.ticker as ticker
import matplotlib.image as image
import shapefile as shp
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
from netCDF4 import Dataset, num2date
import datetime

#Defino los colores de texto y ejes
params = {"text.color" : "white",
          "xtick.color" : "white",
          "ytick.color" : "white"}

df = xr.open_dataset("/home/arw/wrfclima/raw/m1_mes1/salida.nc")

logo = image.imread("/home/arw/shape/logoMarn.png")
logo = image.imread("/home/arw/shape/logo.png")

titulos_meses = ["julio de 2023", "agosto de 2023", "septiembre de 2023", "octubre de 2023", "noviembre de 2023"]
nombres_mapas = ["julio_2023.png", "agosto_2023.png", "septiembre_2023.png", "octubre_2023.png", "noviembre_2023.png"]

#-------------------------------------------------------------------------------------------------------------
#Extraigo las variables de forma directa
#Acumulo la lluvia de manera mensual

lluvia=0
fin=len(df['RAINC'])-1
lluvia = (df['RAINC'][fin,:,:])+(df['RAINNC'][fin,:,:])
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#Genero el plot de la forma mas directa posible sin usar las herramientas de wrfplot
#Extraigo los vectores de latitud y longitud para luego generar con meshgrid la malla
df_lat = df['XLAT'][0,:,0]
df_lon = df['XLONG'][0,0,:]
X, Y = np.meshgrid(df_lon, df_lat)
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#Leo con geopandas el shape para dibujar el mapa
shp = gpd.read_file('/home/arw/shape/TM_WORLD_BORDERS-0.3.shp')
shp_esa = gpd.read_file('/home/arw/shape/ESA_CA_wgs84.shp')

#-------------------------------------------------------------------------------------------------------------

#******************************************************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------
#Genero un plot
#Defino los colores en general
plt.rcParams.update(params)

#Defino la palate de colores
paleta_lluvia=['#ededed', '#d28c68', '#f5aa67','#fecd67','#ffed67','#e8ff67','#b4ff67','#74ff7d','#83febb','#74fff8','#8ac7fe','#808bff',
               '#a368ff','#d968fe','#fe8cfe','#ffc8ff','#fe6869']
niveles_lluvia = [10,20,30,40,50,75,100,125,150,175,200,250,300,350,400,450,500]
niveles_lluvia_regional = [25,50,100,150,200,250,300,350,750,800,900,1000,1200,1300,1400,1500]

#Creo una figura con subplots de tamaño 12 y 10
fig, ax = plt.subplots(figsize=(12,8),facecolor="#323943")


# Establecer el color de los textos de los ejes a blanco
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Establecer el color de los números de latitud y longitud a blanco
ax.xaxis.set_tick_params(labelcolor='white')
ax.yaxis.set_tick_params(labelcolor='white')


#Creo el contorno usando la malla de puntos de latitudes y longitudes junto con la variable a dibujar
cont = ax.contourf(X,Y, lluvia, colors=paleta_lluvia, extend='both', levels=niveles_lluvia_regional)
ax.set_facecolor("white")

#Se añade un titulo
texto = "Lluvia total para el mes de \n" + titulos_meses[0] +" \n Modelo WRF Clima"
ax.set_title(texto, fontsize=12, color="white")

#Añado la barra de colores al objeto ax de 12 y 10
cbar = fig.colorbar(cont, fraction=0.04, pad=0.04, shrink=0.70 , extendrect=False, orientation='horizontal')

#Le añado una etiqueta
cbar.set_label("Lluvia acumulada del mes en milímetros", labelpad = +1, fontsize=10, color="white")

#Etiqueta para el eje x
ax.set_xlabel("Longitud", fontsize=6, loc='right')
#Etiqueta para el eje y
ax.set_ylabel("Latitud", fontsize=6)
#Se fijan los límites en y con los valores mínimos y máximos de latitud y le resto 1.5 para quitar la zona de ruido

lat_minnimo=min(df_lat).values+1
lat_maximo=max(df_lat).values-1

ax.set_ylim(lat_minnimo,lat_maximo) 

#Se fijan los límites en y con los valores mínimos y máximos de longitud y le resto 1.5 para quitar la zona de ruido
lon_minimo=min(df_lon).values+1
lon_maximo=max(df_lon).values-1
ax.set_xlim(lon_minimo,lon_maximo)
#Se dibuja el grid
plt.grid()
#Se dibuja el layout
plt.tight_layout()
#Se dibuja el shape
shp.plot(ax=ax, linewidth=0.5, facecolor='none', edgecolor='black')
#Se añade el logo
newax = fig.add_axes([0.83, 0.92, 0.13, 0.13], anchor='SE')
newax.imshow(logo)
plt.axis("off")
#plt.imshow(logo)
plt.savefig('/home/arw/mapas_python/lluvia_'+nombres_mapas[0])
#Se muestra el plot
#plt.show()
#-------------------------------------------------------------------------------------------------------------
#******************************************************************************************************************************************************


#******************************************************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------
#Genero un plot El Salvador
#Defino los colores en general
plt.rcParams.update(params)

#Defino la palate de colores
paleta_lluvia=['#ededed', '#d28c68', '#f5aa67','#fecd67','#ffed67','#e8ff67','#b4ff67','#74ff7d','#83febb','#74fff8','#8ac7fe','#808bff',
               '#a368ff','#d968fe','#fe8cfe','#ffc8ff','#fe6869']
niveles_lluvia = [10,20,30,40,50,75,100,125,150,175,200,250,300,350,400,450,500]
niveles_lluvia_regional = [25,50,100,150,200,250,300,350,750,800,900,1000,1200,1300,1400,1500]

#Creo una figura con subplots de tamaño 12 y 10
fig, ax = plt.subplots(figsize=(12,8),facecolor="#323943")


# Establecer el color de los textos de los ejes a blanco
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Establecer el color de los números de latitud y longitud a blanco
ax.xaxis.set_tick_params(labelcolor='white')
ax.yaxis.set_tick_params(labelcolor='white')


#Creo el contorno usando la malla de puntos de latitudes y longitudes junto con la variable a dibujar
cont = ax.contourf(X,Y, lluvia, colors=paleta_lluvia, extend='both', levels=niveles_lluvia)
ax.set_facecolor("white")

#Se añade un titulo
texto = "Lluvia total para el mes de \n" + titulos_meses[0] +" \n Modelo WRF Clima"
ax.set_title(texto, fontsize=12, color="white")

#Añado la barra de colores al objeto ax de 12 y 10
cbar = fig.colorbar(cont, fraction=0.04, pad=0.04, shrink=0.70 , extendrect=False, orientation='horizontal')

#Le añado una etiqueta
cbar.set_label("Lluvia acumulada del mes en milímetros", labelpad = +1, fontsize=10, color="white")

#Etiqueta para el eje x
ax.set_xlabel("Longitud", fontsize=6, loc='right')
#Etiqueta para el eje y
ax.set_ylabel("Latitud", fontsize=6)
#Se fijan los límites en y con los valores mínimos y máximos de latitud y le resto 1.5 para quitar la zona de ruido

lat_minnimo=13.1
lat_maximo=14.5

ax.set_ylim(lat_minnimo,lat_maximo) 

#Se fijan los límites en y con los valores mínimos y máximos de longitud y le resto 1.5 para quitar la zona de ruido
lon_minimo=-90.25
lon_maximo=-87.6

ax.set_xlim(lon_minimo,lon_maximo)
#Se dibuja el grid
plt.grid()
#Se dibuja el layout
plt.tight_layout()
#Se dibuja el shape
shp_esa.plot(ax=ax, linewidth=0.5, facecolor='none', edgecolor='black')
#Se añade el logo
newax = fig.add_axes([0.83, 0.92, 0.13, 0.13], anchor='SE')
newax.imshow(logo)
plt.axis("off")
#plt.imshow(logo)
plt.savefig('/home/arw/mapas_python/lluvia_ESA_'+nombres_mapas[0])
#Se muestra el plot
#plt.show()
#-------------------------------------------------------------------------------------------------------------
#******************************************************************************************************************************************************


