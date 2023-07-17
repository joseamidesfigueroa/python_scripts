import xarray as xr

#******************************************************************************************************************************************************
#Cargo capa CHIRPS para calcular anomalias
#Para intentar operar las anomalias sin geotiff
ds2 = xr.open_dataset("/home/arw/wrfclima/raw/m1_mes1/salida.nc")
ds1 = xr.open_dataset("/home/arw/wrfclima/raw/m1_mes1/chirps-v2.0.monthly-medias.nc")

ds2 = ds2.reindex_like(ds1)

ds2 = ds2.rename(coords={'south_north': 'latitude', 'west_east': 'longitude'})

ds2.coords

#Se definen nuevamente los límites del área total
lat_min=min(df_lat).values+1
lat_max=max(df_lat).values-1

lon_min=min(df_lon).values+1
lon_max=max(df_lon).values-1

lluvia_chirps = ds1['precip'][0,:,:]

lluvia_chirps_comun = lluvia_chirps.sel(latitude=slice(lat_min, lat_maximo), longitude=slice(lon_min, lon_max))

lluvia_wrf = (ds2['RAINC'][fin,:,:])+(ds2['RAINNC'][fin,:,:])

lluvia_wrf_comun = lluvia_wrf.sel(XLAT=slice(lat_min, lat_maximo), XLONG=slice(lon_min, lon_max))

anomalia = (lluvia_wrf - lluvia_chirps_comun)




lat_min=13.1
lat_max=14.5
lon_min=-90.25
lon_max=-87.6

