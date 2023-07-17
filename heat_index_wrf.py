import wrf
import numpy as np
import pandas as pd
from wrf import getvar, interplevel, to_np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as crs

#open the wrf file
wrf_file = xr.open_dataset("/home/arw/nc/wrfout_d03_2023-01-19_13:00:00")
#wrf_file = Dataset("/home/arw/nc/wrfout_d03_2023-01-19_13:00:00")

#calculate the Heat index
# get the temperature and humidity
temp = getvar(wrf_file, 'T2',timeidx=0)
rh = getvar(wrf_file, 'RH',timeidx=0)

# calculate the heat index
heat_index = wrf.heat_index(temp, rh)

#interpolate the data to a specific pressure level
heat_index_int = interplevel(heat_index, 1000)

# Plot the heat index
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=crs.PlateCarree())
ax.coastlines(resolution='50m', color='black', linewidth=1)

#draw the map
wrf.map_util.latlon_coords(heat_index_int)
wrf.map_util.cartopy_xlim(ax, heat_index_int)
wrf.map_util.cartopy_ylim(ax, heat_index_int)

# plotting the data
levels = np.linspace(np.min(heat_index_int), np.max(heat_index_int), 11)
cf = ax.contourf(to_np(heat_index_int), levels=levels,
                 transform=crs.PlateCarree(), cmap='YlOrRd')
cbar = plt.colorbar(cf, ax=ax, orientation='horizontal')
cbar.set_label('Heat Index')

plt.title("Heat Index Map for El Salvador")
plt.show()