import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import matplotlib as mpl
import matplotlib.colors as colors
import matplotlib.ticker as ticker
import matplotlib.image as image
import shapefile as shp
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import rasterio


#Defino los colores de texto y ejes
#params = {"text.color" : "white","xtick.color" : "white","ytick.color" : "white"}

logo = image.imread("/home/arw/shape/logoMarn.png")
logo = image.imread("/home/arw/shape/logo.png")

#-------------------------------------------------------------------------------------------------------------
#Leo con geopandas el shape para dibujar el mapa
shp = gpd.read_file('/home/arw/shape/TM_WORLD_BORDERS-0.3.shp')
shp_esa = gpd.read_file('/home/arw/shape/ESA_CA_wgs84.shp')


# Abrir el archivo GeoTIFF
with rasterio.open("/home/arw/lluvia_10dias_ago2023.tif") as src:
    # Leer la banda (en este caso, se lee la primera banda)
    banda = src.read(1)
    # Obtener los límites espaciales del GeoTIFF
    xmin, ymin, xmax, ymax = src.bounds
  
# Definir una paleta de colores personalizada
mi_paleta = colors.ListedColormap(['blue', 'green', 'red', 'yellow', 'orange'])

# Definir los niveles personalizados
niveles = [0, 50, 100, 150, 200, 255]  # Ejemplo de niveles personalizados


# Leer el archivo Shapefile con GeoPandas
shapefile = gpd.read_file('/home/arw/shape/TM_WORLD_BORDERS-0.3.shp')

# Visualizar el GeoTIFF y el Shapefile
fig, ax = plt.subplots()

# Mostrar el GeoTIFF
ax.imshow(banda, cmap=mi_paleta, norm=colors.BoundaryNorm(niveles, mi_paleta.N), extent=[xmin, xmax, ymin, ymax])

# Mostrar el Shapefile
shapefile.plot(ax=ax, facecolor='none', edgecolor='red')

# Ajustar los límites del eje al área del GeoTIFF
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

# Mostrar el mapa
plt.show()
















#******************************************************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------
#Genero un plot
#Defino los colores en general
plt.rcParams.update(params)

#Defino la palate de colores
paleta_lluvia=colors.ListedColormap(['#ededed', '#d28c68', '#f5aa67','#fecd67','#ffed67','#e8ff67','#b4ff67','#74ff7d','#83febb','#74fff8','#8ac7fe','#808bff',
               '#a368ff','#d968fe','#fe8cfe','#ffc8ff','#fe6869'])
niveles_lluvia = [10,20,30,40,50,75,100,125,150,175,200,250,300,350,400,450,500]
niveles_lluvia_regional = [25,50,100,150,200,250,300,350,750,800,900,1000,1200,1300,1400,1500]

# Visualizar el GeoTIFF y el Shapefile
fig, ax = plt.subplots()

# Mostrar el GeoTIFF
ax.imshow(banda, cmap=paleta_lluvia, norm=colors.BoundaryNorm(niveles_lluvia_regional, paleta_lluvia.N))
ax.invert_yaxis

# Mostrar el Shapefile
#shp.plot(ax=ax, facecolor='none', edgecolor='red')

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
#plt.savefig('/home/arw/mapas_python/lluvia_'+nombres_mapas[0])
#Se muestra el plot
plt.show()
#-------------------------------------------------------------------------------------------------------------
#******************************************************************************************************************************************************