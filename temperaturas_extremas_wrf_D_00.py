#Se importan las librerias necesarias
import os
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
import shapefile
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset, num2date
from datetime import date, timedelta
from wrf import getvar

import xarray as xr
import xwrf

import subprocess

#Defino una función para correr procesos de la terminal
def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

#Leo con geopandas el shape para dibujar el mapa
shp = gpd.read_file('/home/arw/shape/ESA_CA_wgs84.shp')

#Define las fechas
hoy = date.today()
manana= hoy + timedelta(1)
pasado= hoy + timedelta(2)
dia4= hoy + timedelta(3)

#Guardo la fecha en formato string para definir la descarga
hoy_string = hoy.strftime("%Y-%m-%d")
manana_string = manana.strftime("%Y-%m-%d")
pasado_string = pasado.strftime("%Y-%m-%d")
dia4_string = pasado.strftime("%Y-%m-%d")

#Se borran los anteriores
runcmd("rm wrfout*")

#Se descargan los archivos de máximas de hoy
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+hoy_string+"_17:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+hoy_string+"_18:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+hoy_string+"_19:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+hoy_string+"_20:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+hoy_string+"_21:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+hoy_string+"_22:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+hoy_string+"_23:00:00", verbose = True)

#Se descargan los archivos de máximas de manana
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+manana_string+"_17:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+manana_string+"_18:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+manana_string+"_19:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+manana_string+"_20:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+manana_string+"_21:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+manana_string+"_22:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+manana_string+"_23:00:00", verbose = True)

#Se descargan los archivos de máximas de pasado
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+pasado_string+"_17:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+pasado_string+"_18:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+pasado_string+"_19:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+pasado_string+"_20:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+pasado_string+"_21:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+pasado_string+"_22:00:00", verbose = True)
runcmd("wget http://192.168.6.43/datos_wrf/D/00/wrfprd/wrfout_d03_"+pasado_string+"_23:00:00", verbose = True)

#------------------------------------------------------------------------------------------------------------------>
#Se abren los netcdf para hoy
nc1 = xr.open_dataset("wrfout_d03_"+hoy_string+"_17:00:00")
nc2 = xr.open_dataset("wrfout_d03_"+hoy_string+"_18:00:00")
nc3 = xr.open_dataset("wrfout_d03_"+hoy_string+"_19:00:00")
nc4 = xr.open_dataset("wrfout_d03_"+hoy_string+"_20:00:00")
nc5 = xr.open_dataset("wrfout_d03_"+hoy_string+"_21:00:00")
nch1 = xr.open_dataset("wrfout_d03_"+hoy_string+"_22:00:00")
nch2 = xr.open_dataset("wrfout_d03_"+hoy_string+"_23:00:00")
#------------------------------------------------------------------------------------------------------------------>

#------------------------------------------------------------------------------------------------------------------>
#Se abren los netcdf para manana
nc6 = xr.open_dataset("wrfout_d03_"+manana_string+"_17:00:00")
nc7 = xr.open_dataset("wrfout_d03_"+manana_string+"_18:00:00")
nc8 = xr.open_dataset("wrfout_d03_"+manana_string+"_19:00:00")
nc9 = xr.open_dataset("wrfout_d03_"+manana_string+"_20:00:00")
nc10 = xr.open_dataset("wrfout_d03_"+manana_string+"_21:00:00")
ncm1 = xr.open_dataset("wrfout_d03_"+manana_string+"_22:00:00")
ncm2 = xr.open_dataset("wrfout_d03_"+manana_string+"_23:00:00")
#------------------------------------------------------------------------------------------------------------------>

#------------------------------------------------------------------------------------------------------------------>
#Se abren los netcdf para pasado manana
nc11 = xr.open_dataset("wrfout_d03_"+pasado_string+"_17:00:00")
nc12 = xr.open_dataset("wrfout_d03_"+pasado_string+"_18:00:00")
nc13 = xr.open_dataset("wrfout_d03_"+pasado_string+"_19:00:00")
nc14 = xr.open_dataset("wrfout_d03_"+pasado_string+"_20:00:00")
nc15 = xr.open_dataset("wrfout_d03_"+pasado_string+"_21:00:00")
ncp1 = xr.open_dataset("wrfout_d03_"+pasado_string+"_22:00:00")
ncp2 = xr.open_dataset("wrfout_d03_"+pasado_string+"_23:00:00")
#------------------------------------------------------------------------------------------------------------------>

#Defino latitudes y longitudes (Solo se hace con uno ya que es suficiente)
df_lat = nc1['XLAT'][0,:,0]
df_lon = nc1['XLONG'][0,0,:]
X, Y = np.meshgrid(df_lon, df_lat)

#------------------------------------------------------------------------------------------------------------------>
#Extraigo la variable que quiero operar para hoy
t1 = nc1["T02_MAX"][0,:,:]
t2 = nc2["T02_MAX"][0,:,:]
t3 = nc3["T02_MAX"][0,:,:]
t4 = nc4["T02_MAX"][0,:,:]
t5 = nc5["T02_MAX"][0,:,:]
th1 = nch1["T02_MAX"][0,:,:]
th2 = nch2["T02_MAX"][0,:,:]
#------------------------------------------------------------------------------------------------------------------>

#------------------------------------------------------------------------------------------------------------------>
#Extraigo la variable que quiero operar para manana
t6 = nc6["T02_MAX"][0,:,:]
t7 = nc7["T02_MAX"][0,:,:]
t8 = nc8["T02_MAX"][0,:,:]
t9 = nc9["T02_MAX"][0,:,:]
t10 = nc10["T02_MAX"][0,:,:]
tm1 = ncm1["T02_MAX"][0,:,:]
tm2 = ncm2["T02_MAX"][0,:,:]
#------------------------------------------------------------------------------------------------------------------>

#------------------------------------------------------------------------------------------------------------------>
#Extraigo la variable que quiero operar para el pasado
t11 = nc11["T02_MAX"][0,:,:]
t12 = nc12["T02_MAX"][0,:,:]
t13 = nc13["T02_MAX"][0,:,:]
t14 = nc14["T02_MAX"][0,:,:]
t15 = nc15["T02_MAX"][0,:,:]
tp1 = ncp1["T02_MAX"][0,:,:]
tp2 = ncp2["T02_MAX"][0,:,:]
#------------------------------------------------------------------------------------------------------------------>


#Se calcula el máximo de todos los tiempos
maxima_hoy = (np.amax((t1,t2,t3,t4,t5,th1,th2), axis=0)-273.15)*(1.09)
maxima_manana = (np.amax((t6,t7,t8,t9,t10,tm1,tm2), axis=0)-273.15)*(1.09)
maxima_pasado = (np.amax((t11,t12,t13,t14,t15,tp1,tp2), axis=0)-273.15)*(1.09)

#Definimos el estilo
#paleta_tmax=['#C909AB','#B307D9','#6207D9','#3007D9','#071DD9','#0765D9','#0798D9','#07CAD9','#07D9B5','#07D98B','#07D958','#07D926','#1FD907','#6BD907','#F5F600','#F6AD00']

paleta_tmax_continua = colors.LinearSegmentedColormap.from_list('mi_paleta', paleta_tmax)

niveles = [-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44]
len(niveles)
niveles_tmax = np.arange(-4,44+2,2)
norm = colors.Normalize(vmin=-4, vmax=44)

#------------------------------------------------------------------------------------------------------------------>
#Creo un gráfico
fig, ax = plt.subplots(figsize=(12,10))
#cont = ax.contourf(X,Y, maxima_hoy, colors=paleta_tmax, levels=niveles_tmax, norm=norm)
cont = ax.contourf(X,Y, maxima_hoy, cmap='nipy_spectral', levels=niveles)
cbar = fig.colorbar(cont, fraction=0.04, pad=0.04, shrink=0.70 , extendrect=False, orientation='horizontal')
texto = "Temperatura máxima para el día \n" + "Dia " + hoy_string + "\n datos del Modelo WRF a las 00 UTC"
ax.set_title(texto, fontsize=10, color="black")
#Etiqueta para el eje x
ax.set_xlabel("Longitud", fontsize=6, loc='right')
#Etiqueta para el eje y
ax.set_ylabel("Latitud", fontsize=6)
#Se fijan los límites en y con los valores mínimos y máximos de latitud
ax.set_ylim(min(df_lat).values,max(df_lat).values)
#Se fijan los límites en y con los valores mínimos y máximos de longitud
ax.set_xlim(min(df_lon).values,max(df_lon).values)
#Se dibuja el grid
plt.grid()
#Se dibuja el layout
plt.tight_layout()
#Se dibuja el shape
shp.plot(ax=ax, color='black', linewidth=0.8, facecolor='none')
#plt.show()
plt.savefig("temperatura_maxima_hoy.png")
#------------------------------------------------------------------------------------------------------------------>

#------------------------------------------------------------------------------------------------------------------>
#Creo un gráfico
fig, ax = plt.subplots(figsize=(12,10))
cont = ax.contourf(X,Y, maxima_manana, cmap='nipy_spectral', levels=niveles)
#cont = ax.contourf(X,Y, maxima_manana, colors=paleta_tmax, levels=niveles_tmax)
cbar = fig.colorbar(cont, fraction=0.04, pad=0.04, shrink=0.70 , extendrect=False, orientation='horizontal')
texto = "Temperatura máxima para el día \n" + "Dia " + manana_string + "\n datos del Modelo WRF a las 00 UTC"
ax.set_title(texto, fontsize=10, color="black")
#Etiqueta para el eje x
ax.set_xlabel("Longitud", fontsize=6, loc='right')
#Etiqueta para el eje y
ax.set_ylabel("Latitud", fontsize=6)
#Se fijan los límites en y con los valores mínimos y máximos de latitud
ax.set_ylim(min(df_lat).values,max(df_lat).values)
#Se fijan los límites en y con los valores mínimos y máximos de longitud
ax.set_xlim(min(df_lon).values,max(df_lon).values)
#Se dibuja el grid
plt.grid()
#Se dibuja el layout
plt.tight_layout()
#Se dibuja el shape
shp.plot(ax=ax, color='black', linewidth=0.8, facecolor='none')
#plt.show()
plt.savefig("temperatura_maxima_manana.png")
#------------------------------------------------------------------------------------------------------------------>

#------------------------------------------------------------------------------------------------------------------>
#Creo un gráfico
fig, ax = plt.subplots(figsize=(12,10))
cont = ax.contourf(X,Y, maxima_pasado, cmap='nipy_spectral', levels=niveles)
#cont = ax.contourf(X,Y, maxima_pasado, colors=paleta_tmax, levels=niveles_tmax)
cbar = fig.colorbar(cont, fraction=0.04, pad=0.04, shrink=0.70 , extendrect=False, orientation='horizontal')
texto = "Temperatura máxima para el día \n" + "Dia " + pasado_string + "\n datos del Modelo WRF a las 00 UTC"
ax.set_title(texto, fontsize=10, color="black")
#Etiqueta para el eje x
ax.set_xlabel("Longitud", fontsize=6, loc='right')
#Etiqueta para el eje y
ax.set_ylabel("Latitud", fontsize=6)
#Se fijan los límites en y con los valores mínimos y máximos de latitud
ax.set_ylim(min(df_lat).values,max(df_lat).values)
#Se fijan los límites en y con los valores mínimos y máximos de longitud
ax.set_xlim(min(df_lon).values,max(df_lon).values)
#Se dibuja el grid
plt.grid()
#Se dibuja el layout
plt.tight_layout()
#Se dibuja el shape
shp.plot(ax=ax, color='black', linewidth=0.8, facecolor='none')
#plt.show()
plt.savefig("temperatura_maxima_pasado.png")
#------------------------------------------------------------------------------------------------------------------>

runcmd("scp temperatura_maxima* arw@192.168.4.20:/var/www/html/")