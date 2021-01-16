import sys, string
from matplotlib import rc, gridspec
import numpy as np
import matplotlib as mpl
mpl.use('agg')
import pylab as pl
import netCDF4
import time as t
from datetime import datetime, timedelta, date
from dateutil.parser import parse
from pylab import load, meshgrid, title, arange, show
from netcdftime import utime
import scipy.io
import argparse
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
import datetime as dt
import pandas as pd
from scipy.signal import butter, lfilter, freqz, hilbert
from sklearn import preprocessing
#from seapy import Sea

def addYears(date, years):
	result = date + timedelta(366 * years)
	if years > 0:
		while result.year - date.year > years or date.month < result.month or date.day < result.day:
			result += datetime.timedelta(-1)
	elif years < 0:
		while result.year - date.year < years or date.month > result.month or date.day > result.day:
			result += timedelta(1)
	print("input: ",  date)
	print("output: ", result)
	return result

def writeFile(nlat,nlon):
	file_name = ('temp_cook_800_2009.nc')
	dataset = netCDF4.Dataset(file_name,'w',format='NETCDF4')
	return dataset

# Load data

df_temp = pd.read_csv('asia2k-jja-temp-anom.txt',sep='\t',header=None)
df_latlon = pd.read_csv('asia2k-cru-xy.txt',sep=',',header=None)
latlon_load = df_latlon.values
temp_load = df_temp.values

year = temp_load[:,0]
temp_in = temp_load[:,1:temp_load.shape[1]]
lon_in = latlon_load[:,0]
lat_in = latlon_load[:,1]

# Create data in the format to be written to netcdf files
#	Northernmost_Latitude: 54.0
#	Southernmost_Latitude: -10.0
#	Easternmost_Longitude: 148.0
#	Westernmost_Longitude: 60.0
# 54.25 to -9.75 create data series for latitude
# 148.25 to 60.25 create data series for longitude 

lat = np.arange(54.25,-10,-2)
lon = np.arange(148.25,60,-2)
temp = np.zeros((year.shape[0], lat.shape[0], lon.shape[0]))
temp[:,:,:] = -99.999

#print(temp.shape)
#print(lon.shape[0])
#print(lat.shape[0])
#l=0
for y in range(year.shape[0]):
	for i in range(lon.shape[0]):
		for j in range(lat.shape[0]):
			for k in range(lon_in.shape[0]):
				if (lon[i] == lon_in[k]) and (lat[j] == lat_in[k]):
					temp[y, j, i] = temp_in[y, k]
					# If condition checks, working properly
					# l = l+1
					# print("If condition working")
					# print(lon[i], lon_in[k], lat[j], lat_in[k])
					# print(l)
# write data to file
print("writing data to file ...")
dataset = writeFile(lat.shape[0], lon.shape[0])

time_v = dataset.createDimension('time', None)
lat_v  = dataset.createDimension('lat', lat.shape[0] )
lon_v  = dataset.createDimension('lon', lon.shape[0])

time_v = dataset.createVariable('time','f8',('time'))
lat_v  = dataset.createVariable('lat', 'f4',('lat'))
lon_v  = dataset.createVariable('lon', 'f4',('lon'))
t_temp = dataset.createVariable('tsurf', np.float32,('time', 'lat', 'lon'), fill_value=-99.999)

t_temp.long_name = 'Surface Temperature, Jun-Aug'
t_temp.short_name = 'TEMP_JJA'
t_temp.units = "K"

time_v.standard_name = 'time'
time_v.long_name = 'time'
time_v.units = 'days since 800-06-15 00:00:00'
time_v.calendar = 'standard'

lat_v.standard_name = 'latitude'
lat_v.long_name = 'latitude'
lat_v.units = 'degrees_north'
lat_v.axis = 'Y'

lon_v.standard_name = 'longitude'
lon_v.long_name = 'longitude'
lon_v.units = 'degrees_east'
lon_v.axis = ' X'

dataset.description = "Asia 1200 Year Gridded Summer Temperature Reconstructions"
dataset.history = "Created " + t.ctime(t.time())
dataset.source = "Cook Anchukaitis et al Climate Dyamics 2013"

dates = []
startdate = datetime(800, 6, 15)
enddate = startdate.replace(startdate.year + 1)
print(startdate,enddate)
for n in range(year.shape[0]):
	enddate = startdate.replace(startdate.year + n)
	dates.append(enddate)
	#print(enddate)
#print(dates)
time_v[:] = netCDF4.date2num(dates, units = time_v.units, calendar = time_v.calendar)
#
#time_v[:] = year
lat_v[:] = lat
lon_v[:] = lon
#print(t_temp.shape, temp.shape)
t_temp[:] = temp
#
#
#
#




   
