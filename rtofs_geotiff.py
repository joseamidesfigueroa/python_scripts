# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from urllib import request
import os
import xarray as xr 
import rioxarray as rio

os.chdir("/home/arw/temporal/")

archivo = "http://192.168.4.28/rtofs/rtofs.nc"

request.urlretrieve(archivo, "rtofs.nc")

nc = "rtofs.nc"

file = netCDF4.Dataset(nc)

