from __future__ import print_function, division

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings("ignore")
sns.set()

nino3 = np.genfromtxt ('enso_900_2002_1.txt', delimiter=",")
ismr = np.genfromtxt ('sasmi_norm_900_2002.txt', delimiter=",")
vrf = np.genfromtxt ('sigl.txt', delimiter=",")
print(nino3.shape)
print(vrf.shape)
def common_time_axis(dismr, verbose=True):
	"""
	Generates common time axis for Nino3 and ISMR time series.
	"""
	# generate the time axis
	Nt = len(dismr)
	time = [dt.datetime(850, 1, 15)]
	for i in range(1, len(dismr)):
		y = time[i - 1].year
		m = time[i - 1].month
		if m == 12:
			y += 1
			m = 0
		time.append(dt.datetime(y, m + 1, 15))
	time = np.array(time)

	return time
def yearly_time_axis(dvolc, verbose=True):
	"""
	Generates time axis for yearly data 
	"""
	Nt = len(dvolc)
	time = [dt.datetime(900, 1, 15)]
	for i in range(1, len(dvolc)):
		y = time[i - 1].year
		y += 1
		time.append(dt.datetime(y, 1, 15))
	time = np.array(time)

	return time
def moving_average_anomaly(dismr,n=360):
	"""
	Generates moving average anomaly of long time series
	"""
	#print(dismr.shape)
	dismr_anom = np.zeros((dismr.shape[0]))
	dismr_std = np.zeros((dismr.shape[0]))
	dismr_anom[0:n/2] = ( dismr[0:n/2] - np.mean(dismr[0:n]) )/np.std(dismr[0:n])
	dismr_anom[dismr.shape[0]-n/2:] = ( dismr[dismr.shape[0]-n/2:] - np.mean(dismr[dismr.shape[0]-n:]) )/np.std(dismr[dismr.shape[0]-n:])
	#print(dismr_anom)
	dismr_std[0:n/2] = np.std(dismr[0:n])
	dismr_std[dismr.shape[0]-n/2:] = np.std(dismr[dismr.shape[0]-n:])
	
	for i in range(np.int(n/2),np.int(dismr.shape[0]-n/2)):
		dismr_anom[i] = (dismr[i] - np.mean(dismr[i-n/2:i+n/2]))/np.std(dismr[i-n/2:i+n/2])
		dismr_std[i] = np.std(dismr[i-n/2:i+n/2])
	return dismr_anom, dismr_std

nino3_900_1850 = nino3[1:952]
ismr_900_1850 = ismr[1:952]
vrf_900_1850 = vrf[50:]
#print(nino3_900_1850.shape)
#print(vrf_900_1850.shape)
#print(nino3_900_1850)
year_time = yearly_time_axis(ismr_900_1850)

import random
import warnings
warnings.filterwarnings('ignore')
#volc_data_mon = np.zeros((1001*12))
#for yyyy in range(1001):
    #print(yyyy)
#    volc_data_mon[yyyy*12:(yyyy+1)*12] = vrf[yyyy]
#print(volc_data_mon[0:120])
#ismr_anom_1550_1750 = ismr_anom[8400:10800]
#nino3_anom_1550_1750 = nino3_anom[8400:10800]
N=10
niter = 0
count_elnino_drought = np.zeros((N))
count_lanina_goodmonsoon  = np.zeros((N))

while niter<N:
	dummy_log_ed = np.zeros((20))
	dummy_log_lg = np.zeros((20))
	rand_year = random.sample(range(11, 938), 1)
	
	dummy_ismr = ismr_900_1850[rand_year[0]-10:rand_year[0]+10]
	dummy_ismr_1 = dummy_ismr
	dummy_nino3 = nino3_900_1850[rand_year[0]-10:rand_year[0]+10]
	dummy_nino3_1 = dummy_nino3
	
	if np.max(vrf_900_1850[rand_year[0]-10:rand_year[0]+10]) < 0.1:
		continue
	print(niter)
	dummy_log_ed[dummy_nino3_1>0.5 and dummy_ismr_1<1.0] = 1.0
	dummy_log_lg[dummy_nino3_1<-0.5 and dummy_ismr_1>1.0] = 1.0
	count_elnino_drought[niter] = np.sum(dummy_log_ed)
	count_lanina_goodmonsoon[niter] = np.sum(dummy_log_lg)
	niter = niter + 1



