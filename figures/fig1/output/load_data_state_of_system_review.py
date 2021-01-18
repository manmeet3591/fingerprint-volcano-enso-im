import numpy as np
import datetime as dt
from scipy import signal
import matplotlib.pyplot as pl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings('ignore')
import numbers
import pandas as pd
import netCDF4 as nc
import matplotlib as mpl
import seaborn as sns

#print("Start of script")
# Krakatoa experiments

# Initial conditions - warm phase

dir_ = "/iitm2/cccr-res/msingh/pmip_data_scripts/agu_volcano/state_of_system/data/warm_phase/"

w_ens1  = nc.Dataset(dir_+'sst_ocean_1993_1995_anom_nino3_fldmean.nc')
w_ens2  = nc.Dataset(dir_+'sst_ocean_2079_2081_anom_nino3_fldmean.nc')
w_ens3 = nc.Dataset(dir_+'sst_ocean_2293_2295_anom_nino3_fldmean.nc')
#w_ens4 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2031.nc')
w_ens5 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2032.nc')
#w_ens6 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2067.nc')
w_ens7 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2094.nc')
w_ens8 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2097.nc')
w_ens9 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2100.nc')
w_ens10 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2135.nc')
w_ens11 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2146.nc')
w_ens12 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2150.nc')
w_ens13 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2176.nc')
w_ens14 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2216.nc')
#w_ens15 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2217.nc')
w_ens16 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2227.nc')
w_ens17 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2231.nc')
w_ens18 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2242.nc')
#w_ens19 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2122.nc')
#w_ens20 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2080.nc')
#w_ens21 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1982.nc')
#w_ens22 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2021.nc')
#w_ens23 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2026.nc')
#w_ens24 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2136.nc')
#w_ens25 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2211.nc')
#w_ens26 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2218.nc')
#w_ens27 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2220.nc')
#w_ens28 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2246.nc')


n_ens1  = nc.Dataset(dir_+'sst_ocean_2017_2019_anom_nino3_fldmean.nc')
n_ens2  = nc.Dataset(dir_+'sst_ocean_2145_2147_anom_nino3_fldmean.nc')
n_ens3  = nc.Dataset(dir_+'sst_ocean_2261_2263_anom_nino3_fldmean.nc')
n_ens4 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1971.nc')
n_ens5 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2010.nc')
n_ens6 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2034.nc')
n_ens7 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2059.nc')
n_ens8 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2115.nc')
n_ens9 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2228.nc')
n_ens10 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1959.nc')
n_ens11 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1974.nc')
n_ens12 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2040.nc')
n_ens13 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2172.nc')
n_ens14 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2286.nc')
n_ens15  = nc.Dataset(dir_+'sst_ocean_2004_2006_anom_nino3_fldmean.nc')
n_ens16  = nc.Dataset(dir_+'sst_ocean_2142_2144_anom_nino3_fldmean.nc')
n_ens17 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2131.nc')
n_ens18 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2166.nc')
n_ens19 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2005.nc')
n_ens20 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1999.nc')
n_ens21 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2240.nc')
n_ens22 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2267.nc')
n_ens23 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2164.nc')
n_ens42 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2031.nc')
n_ens43 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2067.nc')
n_ens44 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2217.nc')
n_ens46 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1991.nc')


c_ens1  = nc.Dataset(dir_+'sst_ocean_2256_2258_anom_nino3_fldmean.nc')
#c_ens2 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1991.nc')
c_ens3 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2050.nc')
c_ens4 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2063.nc')
c_ens5 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2077.nc')
c_ens6 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2105.nc')
c_ens7 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2129.nc')
c_ens8 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2201.nc')
c_ens9 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2239.nc')

dir_ = "/iitm2/cccr-res/msingh/pmip_data_scripts/agu_volcano/state_of_system/data/cold_phase/"

w_ens19 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2122.nc')
w_ens20 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2080.nc')
w_ens21 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1982.nc')
w_ens22 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2021.nc')
w_ens23 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2026.nc')
w_ens24 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2136.nc')
#w_ens25 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2211.nc')
w_ens26 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2218.nc')
w_ens27 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2220.nc')
w_ens28 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2246.nc')

c_ens10 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1958.nc')
c_ens11 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1969.nc')
c_ens12 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1988.nc')
c_ens13 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1997.nc')
c_ens14 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2015.nc')
c_ens15 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2023.nc')
c_ens16 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2055.nc')
c_ens17 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2112.nc')
c_ens18 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2117.nc')
c_ens19 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2125.nc')
c_ens20 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2133.nc')
c_ens21 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2140.nc')
c_ens22 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2148.nc')
c_ens23 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2152.nc')
c_ens24 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2159.nc')
c_ens25 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2214.nc')
c_ens26 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2244.nc')
c_ens27 = nc.Dataset(dir_+'sst_ocean_1968_1970_anom_nino3_fldmean.nc')
c_ens28 = nc.Dataset(dir_+'sst_ocean_2061_2063_anom_nino3_fldmean.nc')
#c_ens29 = nc.Dataset(dir_+'sst_ocean_2073_2075_anom_nino3_fldmean.nc')
c_ens30 = nc.Dataset(dir_+'sst_ocean_2104_2106_anom_nino3_fldmean.nc')
c_ens31 = nc.Dataset(dir_+'sst_ocean_2128_2130_anom_nino3_fldmean.nc')

n_ens24 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2001.nc')
n_ens25 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2156.nc')
n_ens26 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2170.nc')
n_ens27 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1964.nc')
n_ens28 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1995.nc')
n_ens29 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2042.nc')
n_ens30 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2110.nc')
n_ens31 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2193.nc')
n_ens32 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2198.nc')
n_ens33 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2224.nc')
n_ens34 = nc.Dataset(dir_+'sst_ocean_2051_2053_anom_nino3_fldmean.nc')
n_ens35 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2253.nc')
n_ens36 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_1977.nc')
n_ens37 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2025.nc')
n_ens38 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2171.nc')
n_ens39 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2013.nc')
n_ens40 = nc.Dataset(dir_+'sst_ocean_1979_1981_anom_nino3_fldmean.nc')
n_ens41 = nc.Dataset(dir_+'sst_ocean_2062_2064_anom_nino3_fldmean.nc')
n_ens45 = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_2211.nc')
n_ens47 = nc.Dataset(dir_+'sst_ocean_2073_2075_anom_nino3_fldmean.nc')



dir_ = "/iitm1/cccr/msingh/state_of_system/data/warm_phase/"

w_ens39_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1959.nc')
w_ens1_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1993.nc')
w_ens12_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1999.nc')
w_ens13_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2005.nc')
w_ens16_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2032.nc')
w_ens19_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2067.nc')
w_ens4_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2079.nc')
w_ens23_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2115.nc')
w_ens24_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2131.nc')
w_ens25_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2135.nc')
w_ens26_4x_ = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2146.nc')
w_ens27_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2150.nc')
w_ens48_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2164.nc')
w_ens28_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2166.nc')
w_ens8_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2097.nc')
c_ens1_4x_  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2256.nc')
c_ens3_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2050.nc')
n_ens2_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2145.nc')
n_ens16_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2142.nc')
#w_ens29_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2167.nc')
#w_ens49_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2172.nc')
#w_ens7_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2219.nc')
#w_ens37_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2247.nc')

# warm phase decrease in vrf

#w_ens11_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1971.nc')
#w_ens40_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1974.nc')
w_ens41_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1991.nc')
w_ens2_025x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2004.nc')
#w_ens14_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2010.nc')
#w_ens3_025x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2017.nc')
#w_ens15_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2031.nc')
w_ens17_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2034.nc')
#w_ens42_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2040.nc')
#w_ens43_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2050.nc')
w_ens18_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2059.nc')
#w_ens44_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2063.nc')
w_ens20_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2094.nc')
w_ens22_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2100.nc')
#w_ens46_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2105.nc')
w_ens47_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2129.nc')
#w_ens5_025x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2142.nc')
#w_ens6_025x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2145.nc')
w_ens30_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2176.nc')
#w_ens50_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2189.nc')
w_ens31_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2216.nc')
w_ens32_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2217.nc')
#w_ens33_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2227.nc'29
w_ens34_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2228.nc')
w_ens35_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2231.nc')
w_ens51_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2239.nc')
#w_ens52_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2240.nc')
#w_ens36_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2242.nc')
#w_ens8_025x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2256.nc')
w_ens9_025x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2261.nc')
w_ens54_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2267.nc')
w_ens55_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2286.nc')
#w_ens10_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2293.nc')

# Change in VRF
# cold phase increase in vrf
dir_ = "/iitm1/cccr/msingh/state_of_system/data/cold_phase/"

c_ens1_4x  = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1958.nc')
c_ens24_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1964.nc')
#c_ens5_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2001.nc')
#c_ens33_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2080.nc')
c_ens10_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2117.nc')
c_ens14_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2140.nc')
c_ens43_4x = nc.Dataset(dir_+'sst_ocean_1968_1970_monmean_4x_volc_anom_nino3_fldmean.nc')
w_ens26_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2218.nc')
c_ens30_4x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2104.nc')

# cold phase decrease in vrfocean_
c_ens45_025x = nc.Dataset(dir_+'sst_ocean_2051_2053_anom_nino3_fldmean.nc')
c_ens50_025x = nc.Dataset(dir_+'sst_ocean_2128_2130_anom_nino3_fldmean.nc')
c_ens2_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1969.nc')
c_ens25_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1977.nc')
#c_ens26_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1982.nc')
c_ens3_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1988.nc')
c_ens27_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_1995.nc')
c_ens28_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2013.nc')
c_ens6_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2015.nc')
c_ens29_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2021.nc')
c_ens7_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2023.nc')
c_ens30_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2025.nc')
c_ens31_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2026.nc')
#c_ens8_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2055.nc')
c_ens34_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2110.nc')
c_ens9_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2112.nc')
#c_ens12_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2125.nc')
c_ens13_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2133.nc')
#c_ens35_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2136.nc')
c_ens15_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2148.nc')
c_ens16_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2152.nc')
c_ens17_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2156.nc')
#c_ens18_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2159.nc')
c_ens20_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2171.nc')
c_ens36_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2193.nc')
c_ens21_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2214.nc')
c_ens41_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2224.nc')
c_ens22_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2244.nc')
c_ens42_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2246.nc')

#print("Data reading done")
#c_ens23_025x = nc.Dataset(dir_+'fldmean_nino3_anom_mon_sst_ocean_2253.nc')
# Initial conditions warm phase imposed with krakatoa
#w_sst = np.zeros((50,36))
w_sst = np.zeros((24,36))
#w_ens = [w_ens1, w_ens2, w_ens3, w_ens4, w_ens5, w_ens6,  w_ens8, w_ens9, w_ens10, \
#        w_ens11, w_ens12, w_ens13, w_ens14, w_ens15, w_ens16, w_ens17, w_ens18, w_ens19, w_ens20, \
#        w_ens21, w_ens22, w_ens23, w_ens24, w_ens25, w_ens26, w_ens27, w_ens28,  w_ens30, \
#        w_ens31, w_ens32, w_ens33, w_ens34, w_ens35, w_ens36,  w_ens38, w_ens39, w_ens40, \
#        w_ens41, w_ens42, w_ens43, w_ens44, w_ens45, w_ens46, w_ens47, w_ens48,  w_ens50, \
#        w_ens51, w_ens52, w_ens54, w_ens55]

w_ens = [w_ens1, w_ens2, w_ens3,  w_ens5,   w_ens7, w_ens8, w_ens9, w_ens10, \
        w_ens11, w_ens12, w_ens13, w_ens14,  w_ens16, w_ens17, w_ens18, w_ens19, w_ens20, \
        w_ens21, w_ens22, w_ens23, w_ens24,  w_ens26, w_ens27, w_ens28]


for i,w_i in enumerate(w_ens):
    w_sst[i,:] = w_i.variables['sst'][0:36,0,0]

# Initial conditions cold phase imposed with krakatoa
c_sst = np.zeros((29,36))
#c_sst = np.zeros((50,36))
#c_ens = [c_ens1, c_ens2, c_ens3, c_ens4, c_ens5, c_ens6, c_ens7, c_ens8, c_ens9, c_ens10, \
#        c_ens11, c_ens12, c_ens13, c_ens14, c_ens15, c_ens16, c_ens17, c_ens18, c_ens19, c_ens20, \
#        c_ens21, c_ens22, c_ens23, c_ens24, c_ens25, c_ens26, c_ens27, c_ens28, c_ens29, c_ens30, \
#        c_ens31, c_ens32, c_ens33, c_ens34, c_ens35, c_ens36, c_ens37, c_ens38, c_ens39, c_ens40, \
#        c_ens41, c_ens42, c_ens43, c_ens44, c_ens45, c_ens46, c_ens47, c_ens48, c_ens49, c_ens50, ]
c_ens = [c_ens1,  c_ens3, c_ens4, c_ens5, c_ens6, c_ens7, c_ens8, c_ens9, c_ens10, \
        c_ens11, c_ens12, c_ens13, c_ens14, c_ens15, c_ens16, c_ens17, c_ens18, c_ens19, c_ens20, \
        c_ens21, c_ens22, c_ens23, c_ens24, c_ens25, c_ens26, c_ens27, c_ens28,  c_ens30, \
        c_ens31]


for i,c_i in enumerate(c_ens):
    c_sst[i,:] = c_i.variables['sst'][0:36,0,0]


n_sst = np.zeros((47,36))
#w_ens = [w_ens1, w_ens2, w_ens3, w_ens4, w_ens5, w_ens6,  w_ens8, w_ens9, w_ens10, \
#        w_ens11, w_ens12, w_ens13, w_ens14, w_ens15, w_ens16, w_ens17, w_ens18, w_ens19, w_ens20, \
#        w_ens21, w_ens22, w_ens23, w_ens24, w_ens25, w_ens26, w_ens27, w_ens28,  w_ens30, \
#        w_ens31, w_ens32, w_ens33, w_ens34, w_ens35, w_ens36,  w_ens38, w_ens39, w_ens40, \
#        w_ens41, w_ens42, w_ens43, w_ens44, w_ens45, w_ens46, w_ens47, w_ens48,  w_ens50, \
#        w_ens51, w_ens52, w_ens54, w_ens55]

n_ens = [n_ens1 , n_ens2,  n_ens3,  n_ens4,  n_ens5,  n_ens6,  n_ens7,  n_ens8,  n_ens9,  n_ens10, \
         n_ens11, n_ens12, n_ens13, n_ens14, n_ens15, n_ens16, n_ens17, n_ens18, n_ens19, n_ens20, \
         n_ens21, n_ens22, n_ens23, n_ens24, n_ens25, n_ens26, n_ens27, n_ens28, n_ens29,n_ens30, \
         n_ens31, n_ens32, n_ens33, n_ens34, n_ens35, n_ens36, n_ens38, n_ens39, n_ens40, \
         n_ens41, n_ens42, n_ens43, n_ens44, n_ens45, n_ens46, n_ens47]


for i,n_i in enumerate(n_ens):
    n_sst[i,:] = n_i.variables['sst'][0:36,0,0]

# Initial conditions warm phase increase in vrf
w_sst_4x = np.zeros((8,36))
w_ens_4x = [ w_ens1_4x,   w_ens16_4x, w_ens4_4x, \
            w_ens25_4x, w_ens26_4x_, w_ens27_4x,  w_ens8_4x, w_ens26_4x]

for i,w_i in enumerate(w_ens_4x):
    w_sst_4x[i,:] = w_i.variables['sst'][0:36,0,0]
#
# Initial conditions warm phase increase in vrf - original
w_sst_4x_o = np.zeros((8,36))
w_ens_4x_o = [w_ens1,  w_ens5,  w_ens2,  \
            w_ens10, w_ens11, w_ens12,  w_ens8, w_ens26]

for i,w_i in enumerate(w_ens_4x_o):
    w_sst_4x_o[i,:] = w_i.variables['sst'][0:36,0,0]

# Initial conditions warm phase decrease in vrf
w_sst_025x = np.zeros((8,36))
w_ens_025x = [  \
                \
              w_ens20_025x, w_ens22_025x, w_ens47_025x, \
              w_ens30_025x, w_ens31_025x,  w_ens35_025x, \
              w_ens51_025x, w_ens9_025x] 


for i,w_i in enumerate(w_ens_025x):
    w_sst_025x[i,:] = w_i.variables['sst'][0:36,0,0]
#
# Initial conditions warm phase decrease in vrf - original - to check the exact correspondence with change in vrf
w_sst_025x_o = np.zeros((8,36))
w_ens_025x_o = [     \
                \
              w_ens7, w_ens9, c_ens7,  \
              w_ens13, w_ens14,  w_ens17, \
              c_ens9, c_ens1] 
for i,w_i in enumerate(w_ens_025x_o):
    w_sst_025x_o[i,:] = w_i.variables['sst'][0:36,0,0]
#print("test")
#
#
# Initial conditions cold phase increase in vrf
c_sst_4x = np.zeros((7,36))
c_ens_4x = [c_ens1_4x_,c_ens1_4x,  c_ens10_4x, c_ens14_4x, c_ens43_4x, c_ens3_4x, c_ens30_4x] 


for i,c_i in enumerate(c_ens_4x):
    c_sst_4x[i,:] = c_i.variables['sst'][0:36,0,0]

# Initial conditions cold phase increase in vrf - original
c_sst_4x_o = np.zeros((7,36))
c_ens_4x_o = [c_ens1, c_ens10, c_ens18, c_ens21, c_ens27, c_ens3, c_ens30] 


for i,c_i in enumerate(c_ens_4x_o):
    c_sst_4x_o[i,:] = c_i.variables['sst'][0:36,0,0]
#
# Initial conditions cold phase decrease in vrf
c_sst_025x = np.zeros((13,36))
c_ens_025x = [ c_ens50_025x, c_ens3_025x, \
                c_ens6_025x, c_ens29_025x, c_ens7_025x, \
              c_ens31_025x,   c_ens9_025x, c_ens13_025x, c_ens15_025x, \
              c_ens16_025x,   c_ens21_025x, \
              c_ens22_025x, c_ens42_025x]#, c_ens2_025x] # c_ens2_025x to be investigated: it has only 30 months

for i,c_i in enumerate(c_ens_025x):
    c_sst_025x[i,:] = c_i.variables['sst'][0:36,0,0]
    
# Initial conditions cold phase decrease in vrf - original
c_sst_025x_o = np.zeros((13,36))
c_ens_025x_o = [ c_ens31, c_ens12, \
               c_ens14, w_ens22, c_ens15, \
              w_ens23,   c_ens17, c_ens20, c_ens22, \
              c_ens23,   c_ens25, \
               c_ens26, w_ens28]#, c_ens11]

for i,c_i in enumerate(c_ens_025x_o):
    c_sst_025x_o[i,:] = c_i.variables['sst'][0:36,0,0]

#
#
# Initial conditions neutral phase increase in vrf
n_sst_4x = np.zeros((11,36))
n_ens_4x = [n_ens2_4x, w_ens23_4x, w_ens39_4x, c_ens24_4x, n_ens16_4x, w_ens24_4x, w_ens28_4x, \
					 w_ens13_4x, w_ens12_4x, w_ens48_4x, w_ens19_4x]


for i,n_i in enumerate(n_ens_4x):
    n_sst_4x[i,:] = n_i.variables['sst'][0:36,0,0]

# Initial conditions cold phase increase in vrf - original
n_sst_4x_o = np.zeros((11,36))
n_ens_4x_o = [n_ens2, n_ens8, n_ens10, n_ens27, n_ens16, n_ens17, n_ens18, \
						 n_ens19, n_ens20, n_ens23, n_ens43]


for i,n_i in enumerate(n_ens_4x_o):
    n_sst_4x_o[i,:] = n_i.variables['sst'][0:36,0,0]

# Initial conditions cold phase decrease in vrf
n_sst_025x = np.zeros((19,36))
n_ens_025x = [w_ens9_025x, w_ens17_025x, w_ens18_025x, w_ens34_025x, w_ens55_025x, \
						 c_ens17_025x, c_ens27_025x, c_ens34_025x, c_ens36_025x, c_ens41_025x, \
						 c_ens45_025x, w_ens2_025x, c_ens25_025x, c_ens30_025x, w_ens54_025x, \
						 c_ens20_025x, c_ens28_025x, w_ens32_025x, w_ens41_025x]

for i,n_i in enumerate(n_ens_025x):
    n_sst_025x[i,:] = n_i.variables['sst'][0:36,0,0]
    
# Initial conditions cold phase decrease in vrf - original
n_sst_025x_o = np.zeros((19,36))
n_ens_025x_o = [n_ens3, n_ens6, n_ens7, n_ens9, n_ens14, \
							 n_ens25, n_ens28, n_ens30, n_ens31, n_ens33, \
							 n_ens34, n_ens15, n_ens36, n_ens37, n_ens22, \
							 n_ens38, n_ens39, n_ens44, n_ens46]

for i,n_i in enumerate(n_ens_025x_o):
    n_sst_025x_o[i,:] = n_i.variables['sst'][0:36,0,0]
