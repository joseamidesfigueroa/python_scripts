import numpy as np
import xarray as xr

# Any import of metpy will activate the accessors
import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.units import units

# Open the netCDF file as a xarray Dataset
data1 = xr.open_dataset(get_test_data('irma_gfs_example.nc', False))
data = xr.open_dataset('wrf_prueba.nc')

# View a summary of the Dataset
data

temp = data['T2']
