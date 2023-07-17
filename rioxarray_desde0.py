#------------------------------------------------------------------------------------->
#Carga las librerias a utilizar
import rioxarray
import matplotlib.pyplot as plt
import numpy as np
import xarray
#------------------------------------------------------------------------------------->

#------------------------------------------------------------------------------------->
#Carga el archivo NetCDF
nc = xarray.open_dataset("/home/arw/trabajo/nc/rtofs.nc",  decode_coords="all")
#------------------------------------------------------------------------------------->

#------------------------------------------------------------------------------------->
#Prepara la sst para el tiempo 1
sst_f001=nc.sst[1, :, :]
#Roto los datos ya que están al reves
sst_f001 = np.flipud(sst_f001)
#------------------------------------------------------------------------------------->

#------------------------------------------------------------------------------------->
#Preparo las características para la imagen
plt.figure(figsize=(12,12))

plt.imshow(sst_f001, cmap='cool')

plt.show()
#------------------------------------------------------------------------------------->

