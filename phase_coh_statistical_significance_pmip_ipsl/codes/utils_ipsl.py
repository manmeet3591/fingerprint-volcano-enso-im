#! /usr/bin/env python
"""
Estimate phase synchronization periods between ENSO and AIMRI
=============================================================

"""
# Created: Wed Oct 11, 2017  03:18PM
# Last modified: Fri Nov 17, 2017  08:40AM
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>

import numpy as np
import datetime as dt
from scipy import signal
from scipy.stats import percentileofscore, norm
import csv
import netCDF4

def load_data():
		"""Returns Nino3 and ISMR time series after laoding data from CSV files.
		"""
		# load the data
		DATPATH = "../data/"
		fnino = DATPATH + "tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_1_nino3_tseries.nc"
		#fnino = DATPATH + "nino3_1871_2016.csv"
		#fnino = DATPATH + "nino34.long.data"
		nc_data_nino3 = netCDF4.Dataset(fnino) 
		nino3_load = nc_data_nino3.variables['tas'][:] 
		dnino = nino3_load.flatten()

		fismr = DATPATH + "psl_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_1_india_goswami_2002_tseries.nc"
		nc_data_ismr = netCDF4.Dataset(fismr) 
		ismr_load = nc_data_ismr.variables['psl'][:] 
		dismr = ismr_load.flatten()

		fvolc = DATPATH + "sigl.txt"
		dvolc = np.genfromtxt(fvolc, delimiter=",", dtype=float).flatten()
		# simple check for data consistency
		assert dnino.shape == dismr.shape, "Data sets are unequal!"
		assert int(dismr.shape[0]/12) == dvolc.shape[0], "Data sets are unequal"
		return dnino, dismr, dvolc


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
		time = [dt.datetime(850, 1, 15)]
		for i in range(1, len(dvolc)):
				y = time[i - 1].year
				y += 1
				time.append(dt.datetime(y, 1, 15))
		time = np.array(time)

		return time

#def climate_anomaly(x, t):
#    """
#    Returns climate anomaly of 'x' wrt 1/1/1971-31/12/1980 climate normal.
#    """
#    # climate normal period := January 1971 to December 1980
#    #d1 = dt.datetime(1971, 1, 1)
#    d1 = dt.datetime(1871, 1, 1)
#    #d2 = dt.datetime(1980, 12, 31)
#    d2 = dt.datetime(2000, 12, 31)
#    idx = np.where((t >= d1) * (t <= d2))[0]
#    x_clim = x[idx].mean()
#    x_anom = x - x_clim
#
#    return _quantile_normalization(x_anom, mode="mean")
#    #return x_anom

def climate_anomaly(x, t):
	"""
	Returns climate anomaly of 'x' wrt 1/1/1971-31/12/1980 climate normal.
	"""
	# climate normal period := January 1971 to December 1980
	# Seasonally normalized values w.r.t 30 years running mean  
	# +1 is added to d2.year to include the last year in the analysis  
	d1 = dt.datetime(850, 1, 1)
	d2 = dt.datetime(1850, 12, 31)
	x_anom = np.zeros((x.shape[0]))
	for yy in range(d1.year,d2.year+1):
		lyear = yy-15
		uyear = yy+15
		if yy < d1.year+15:
			lyear = d1.year
			uyear = d1.year+30
		if yy > d2.year+1-15:
			lyear = d2.year+1-30
			uyear = d2.year
		idx1 = lyear - d1.year
		id = yy - d1.year
		#print("for year",yy,"lyear",lyear,"uyear",uyear,"idx1_m")
		for mm in range(12):
			#print("index",id*12+mm,"start_month",idx1*12,"end_month",idx1*12+12*30)
			idx = np.arange(idx1*12+mm,idx1*12+12*30+mm,12)	
			x_anom[id*12+mm] = x[id*12+mm] - x[idx].mean()
			#x_anom[id*12+mm] = (x[id*12+mm] - x[idx].mean())/x[idx].std()
			#print("Mean",x[idx].mean()) 
			#print("Std",x[idx].std()) 
	#print(x_norm) 
	#print(x_norm.shape) 
	#print(idx.shape) 
	#print(x_norm.min()) 
	#print(x_norm.max()) 
	
	return _quantile_normalization(x_anom, mode="mean")
	#return x_norm


def iirfilter(x, N=4, pass_freq=0.7 / 12.):
    """
    Returns the forward-backward filtered signal using a Butterworth filter.
    """
    b, a = signal.butter(N, pass_freq, "low", analog=False)
    return  signal.filtfilt(b, a, x)


def printmsg(msg, verbose):
    """
    Prints info messages to stdout depending on given verbosity.
    """
    if verbose:
        print(msg)

    return None


def _quantile_normalization(arr, mode="mean"):
    """
    Normalizes the data to a Gaussian distribution using quantiles.
    """
    n = len(arr)
    perc = percentileofscore
    arr_ = arr.copy()[~np.isnan(arr)]
    out = np.zeros(n)
    for i in range(n):
        if not np.isnan(arr[i]):
            out[i] = norm.ppf(perc(arr_, arr[i], mode) / 100.)
        else:
            out[i] = np.nan
    return out

def write_defined_phase(ct, te, del_phi_phase_defined):
	"""
	Writes to a file the periods for which the phase is well defined along with the 
	phase difference values 
	"""
	csvfile = "../output/defined_phase.txt"
	with open(csvfile, "w") as output:
		writer = csv.writer(output, lineterminator='\n')
		for val in del_phi_phase_defined:
			writer.writerow([val])   
	csvfile = "../output/defined_phase_time.txt"
	with open(csvfile, "w") as output:
		writer = csv.writer(output, lineterminator='\n')
		for val in te:
			writer.writerow([val])   
	csvfile = "../output/time.txt"
	with open(csvfile, "w") as output:
		writer = csv.writer(output, lineterminator='\n')
		for val in ct:
			writer.writerow([val])   

def yearly_percent_anomalies(dmonsoon):
	aismr = (dmonsoon-8481)/8481
	return aismr*100


