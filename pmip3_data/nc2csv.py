import netCDF4
import numpy as np
import datetime as dt
from netCDF4 import num2date, date2num

#nc_data = netCDF4.Dataset('tas_Amon_IPSL-CM5A-LR_piControl_r1i1p1_180001-279912_nino3_tseries.nc')
#nc_data = netCDF4.Dataset('tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.nc')
nc_data = netCDF4.Dataset('va_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0865_1835_anom_850m200_hc_jjas_ymean.nc')
data = nc_data.variables['va'][:]
#np.savetxt('tas_Amon_IPSL-CM5A-LR_piControl_r1i1p1_180001-279912_nino3_tseries.csv', nino3[:,0,0], delimiter=',')
#np.savetxt('tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.csv', nino3[:,0,0], delimiter=',')
np.savetxt('va_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0865_1835_anom_850m200_hc_jjas_ymean.csv', data[:,0,0,0], delimiter=',')
#print(nino3.shape)
