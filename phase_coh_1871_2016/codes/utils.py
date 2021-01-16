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

def load_data():
		"""Returns Nino3 and ISMR time series after laoding data from CSV files.
		"""
		# load the data
		DATPATH = "../data/"
		fnino = DATPATH + "nino3_1871_2016.csv"
		#fnino = DATPATH + "nino34.long.data"
		dnino = np.genfromtxt(fnino, delimiter=",", dtype=float).flatten()
		fismr = DATPATH + "ismr_1871_2016.csv"
		dismr = np.genfromtxt(fismr, delimiter=",", dtype=float).flatten()
		fvolc = DATPATH + "robock.txt"
		dvolc = np.genfromtxt(fvolc, delimiter=",", dtype=float).flatten()
		fmonsoon = DATPATH + "monsoon.csv"
		dmonsoon = np.genfromtxt(fvolc, delimiter=",", dtype=float).flatten()
		# simple check for data consistency
		assert dnino.shape == dismr.shape, "Data sets are unequal!"
		assert int(dismr.shape[0]/12) == dvolc.shape[0], "Data sets are unequal"
		return dnino, dismr, dvolc, dmonsoon


def common_time_axis(dismr, verbose=True):
    """
    Generates common time axis for Nino3 and ISMR time series.
    """
    # generate the time axis
    Nt = len(dismr)
    time = [dt.datetime(1871, 1, 15)]
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
		time = [dt.datetime(1871, 1, 15)]
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
    d1 = dt.datetime(1871, 1, 1)
    #d2 = dt.datetime(1980, 12, 31)
    d2 = dt.datetime(2000, 12, 31)
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

def yearly_percent_anomalies(dmonsoon):
	aismr = (dmonsoon-8481)/8481
	return aismr*100


