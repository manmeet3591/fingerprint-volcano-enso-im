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
		#fnino = DATPATH + "nino3.csv" # 1871-2000
		fnino = DATPATH + "tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.csv" # 1871-2016
		#fnino = DATPATH + "nino34.long.data"
		#nc_data_nino3 = netCDF4.Dataset(fnino)
		#nino3_load = nc_data_nino3.variables['tas'][:]
		#dnino = nino3_load.flatten()

		dnino = np.genfromtxt(fnino, delimiter=",", dtype=float).flatten()
		#fismr = DATPATH + "ismr.csv" # 1871-2000
		#fismr = DATPATH + "psl_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_1_india_goswami_2002_tseries.csv" # 1871-2016
		fismr = DATPATH + "pr_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_goswami_india_tseries.csv" # 1871-2016
		dismr = np.genfromtxt(fismr, delimiter=",", dtype=float).flatten()
		#fvolc = DATPATH + "robock.txt" # 1871-2000
		fvolc = DATPATH + "sigl.txt" # 1871-2016
		dvolc = np.genfromtxt(fvolc, delimiter=",", dtype=float).flatten()

		fvolc_source = DATPATH + "volc_source_850_1850.csv" # 1871-2016
		dvolc_source = np.genfromtxt(fvolc_source, delimiter=",", dtype=float).flatten()
		# simple check for data consistency
		assert dnino.shape == dismr.shape, "Data sets are unequal!"
		assert int(dismr.shape[0]/12) == dvolc.shape[0], "Data sets are unequal"
		return dnino, dismr, dvolc, dvolc_source


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

def plv_time_axis(dismr, verbose=True):
    """
    Generates common time axis for Nino3 and ISMR time series.
    """
    # generate the time axis
    Nt = len(dismr) - 3 * 12 # 3 year running PLV
    time = [dt.datetime(851, 7, 15)] # 3 year running PLV
    #time = [dt.datetime(1873, 7, 15)] # 5 year running PLV
    for i in range(1, Nt):
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

def climate_anomaly(x, t):
    """
    Returns climate anomaly of 'x' wrt 1/1/1971-31/12/1980 climate normal.
    """
    # climate normal period := January 1971 to December 1980
    #d1 = dt.datetime(1971, 1, 1)
    d1 = dt.datetime(850, 1, 1)
    #d2 = dt.datetime(1980, 12, 31)
    d2 = dt.datetime(1850, 12, 31)
    idx = np.where((t >= d1) * (t <= d2))[0]
    x_clim = x[idx].mean()
    x_anom = x - x_clim

    return _quantile_normalization(x_anom, mode="mean")
    #return x_anom


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

def phase_locking_value(theta1, theta2):
	complex_phase_diff = np.exp(np.complex(0,1)*(theta1 - theta2))
	plv = np.abs(np.sum(complex_phase_diff))/len(theta1)
	return plv

def zero_slope(data, chunksize =4, max_slope = .25):
	is_plateau = np.zeros((data.shape[0]))
	for index in range(0, len(data) - chunksize):
		chunk = data[index : index + chunksize]
    # subtract the endpoints of the chunk
    # if not sufficient, maybe use a linear fit
		#dy_dx = abs(chunk[0] - chunk[-1])/chunksize
		dy_dx = dy_dx = abs(chunk[1:] - chunk[:-1]).sum()/chunksize
    #print(dy_dx)
		if (0 <= dy_dx < max_slope):
			is_plateau[index] = 1.0
	return is_plateau

def func(x, a, b, c):
	return a * np.exp(-b * x) + c
