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
from netCDF4 import Dataset, num2date


from wrf import getvar

#Se abre el netcdf
df = xr.open_dataset('/home/arw/nc/wrfout_d03_2023-01-19_13:00:00')
nc = Dataset('/home/arw/nc/wrfout_d03_2023-01-19_13:00:00')
logo = image.imread("/home/arw/shape/logoMarn.png")
logo = image.imread("/home/arw/shape/logo.png")


#-------------------------------------------------------------------------------------------------------------
#Extraigo las variables de forma directa
#temp = df['T2'][0,:,:]-273.15
#hum = df['RH02'][0,:,:]

#Extraigo la fecha y tiempo como un string
time_stamp = df['XTIME'][:]
ts = ps.to_datetime(time_stamp)
time = ts.strftime('%Y-%m-%d - %H:%M UTC')
tiempo = time[0]
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#Extraigo las variables con WRF-Python
temp = getvar(nc,"tc")[0,:]
hum = getvar(nc,"rh2")[0,:]
vv = getvar(nc,"wspd_wdir10", units="km h-1")[0,:]
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#Calculo la sensación térmica que luego usaré como índice térmico
if temp.all().values < 0 :
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
    CC1 = temp*hum
    D1=d*CC1
    DD1=temp*temp
    E1=e*DD1
    EE1=hum*hum
    F1=f*EE1
    FF1=pow(temp,2)*hum
    G1=g*FF1
    GG1=pow(hum,2)*temp
    H1=h*GG1
    HH1=pow(hum,2)*pow(temp,2)
    I1=i*HH1
    ST=a+B1+C1-D1-E1-F1+G1+H1-I1
else :
    a=13.1267
    b=0.6215
    c=11.37
    d=0.3965
    exp=0.16
    B1=b*temp
    V=pow(vv,exp)
    C1=c*V
    D1=d*temp*V
    ST=(a+B1-C1+D1)
##--------------------------------------------------->

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
shp = gpd.read_file('/home/arw/shape/ESA_CA_wgs84.shp')
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#Genero un plot

#Defino la palate de colores
paleta=['#daeef3', '#c5d9f1', '#538dd5','#78b832','#ffff00','#ffc000','#ff0000','#974706']
niveles = [8,14,20,26,32,38,44]
categorias = ['Frío','Semi Frío','Templado','Agradable','Cálido','Muy Cálido','Cálido Opresivo','Extremo Cálido']
matplotlib.rcParams['hatch.color'] = 'None'
#Creo una figura con subplots de tamaño 12 y 10
fig, ax = plt.subplots(figsize=(12,10),facecolor="#323943")


# Establecer el color de los textos de los ejes a blanco
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Establecer el color de los números de latitud y longitud a blanco
ax.xaxis.set_tick_params(labelcolor='white')
ax.yaxis.set_tick_params(labelcolor='white')


#Creo el contorno usando la malla de puntos de latitudes y longitudes junto con la variable a dibujar
cont = ax.contourf(X,Y, ST, colors=paleta, extend='both', levels=niveles)
ax.set_facecolor("k")
#Añado la barra de colores al objeto ax de 12 y 10
cbar = fig.colorbar(cont, fraction=0.04, pad=0.04, shrink=0.70 , extendrect=False, orientation='horizontal')
cbar.set_ticklabels(categorias)
cbar.ax.set_facecolor("white")
cbar.ax.outline.set_visible(False)
cbar.solids.set_edgecolor("face")

#Le añado una etiqueta
#cbar.set_label("Mapa de prueba", labelpad = +1, fontsize=18)
#Se añade un titulo
texto = "Confort Térmico para: \n" + tiempo + "\n Modelo WRF miembro C"
ax.set_title(texto, fontsize=10, color="white")
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
shp.plot(ax=ax, color='black', linewidth=0.5)
#Se añade el logo
newax = fig.add_axes([0.85, 0.95, 0.12, 0.12], anchor='SE')
newax.imshow(logo)
plt.axis("off")
#plt.imshow(logo)
plt.savefig('mapa.png')
#Se muestra el plot
plt.show()
#-------------------------------------------------------------------------------------------------------------