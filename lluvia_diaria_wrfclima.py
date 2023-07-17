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
