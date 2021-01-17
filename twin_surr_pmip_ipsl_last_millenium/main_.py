#! /usr/local/opt/python/libexec/bin/python
"""
Use the functions phaselock.py to estimate phase locking between ISMR & NINO3
=============================================================================


"""
# Created: Thu Oct 12, 2017  02:37PM
# Last modified: Fri Nov 17, 2017  09:12AM
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>
# Modified: Manmeet Singh <manmeet.cat@tropmet.res.in>

import sys
import numpy as np
from scipy import signal
import utils
import figs


i = sys.argv[1]
# load data and create common time axis array
print("load data ...")
dismr = np.genfromtxt("pr_ipsl_surr_"+str(i)+".txt", delimiter=",", dtype=float)[0:12000]
dnino = np.genfromtxt("tas_ipsl_surr_"+str(i)+".txt", delimiter=",", dtype=float)[0:12000] 
time = utils.common_time_axis(dismr)

# estimate climate anomalies
print("climate anomalies ...")
nino_anom = utils.climate_anomaly(dnino, time)
ismr_anom = utils.climate_anomaly(dismr, time)
print("Test2")

# filter the time series
print("filtered time series ...")
cut = 8.0 / 12
fs = 12.
N = 5
nino_filt = utils.iirfilter(nino_anom, N=N, cutoff=cut, fs=fs)
ismr_filt = utils.iirfilter(ismr_anom, N=N, cutoff=cut, fs=fs)


# estimate the derivative of the filtered time series
print("time series derivatives ...")
nino_grad = np.gradient(nino_filt, 1)
ismr_grad = np.gradient(ismr_filt, 1)
print("Test4")

# use the Hilbert transform to estimate the phase of the signal
print("Hilbert transform ...")
nino_phi = np.unwrap(np.angle(signal.hilbert(nino_grad)))
ismr_phi = np.unwrap(np.angle(signal.hilbert(ismr_grad)))
print("Surrogate number ...",int(i)+1)

# calculate the instantaneous phase difference
print("instantaneous phase difference ...")
del_phi = ismr_phi - nino_phi

np.savetxt('delphi_ipsl_'+str(i)+'.csv', del_phi, delimiter=',')
