import netCDF4
import numpy as np
import datetime as dt
from netCDF4 import num2date, date2num

nc_data = netCDF4.Dataset('Precon1470-1999_ci_tseries.nc')
d_ = nc_data.variables['pre'][:,0,0]
year = np.arange(1470,2000)
print(year)
data = np.zeros((d_.shape[0],2))
data[:,0] = year
data[:,1] = d_
np.savetxt('Precon1470-1999_ci_tseries.csv', data, delimiter=',')
