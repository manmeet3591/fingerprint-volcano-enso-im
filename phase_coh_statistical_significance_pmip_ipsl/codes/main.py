#! /usr/local/opt/python/libexec/bin/python
"""
Use the functions phaselock.py to estimate phase locking between ISMR & NINO3
=============================================================================


"""
# Created: Thu Oct 12, 2017  02:37PM
# Last modified: Fri Nov 17, 2017  09:12AM
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>


import sys
import numpy as np
from scipy import signal
import utils
import figs
from scipy.optimize import curve_fit

max_slope = 0.1
chunksize = 48

verbose = True
# load data and create common time axis array
utils.printmsg("load data ...", verbose)
dnino, dismr, dvolc, dvolc_source = utils.load_data()
time = utils.common_time_axis(dismr)
plv_time = utils.plv_time_axis(dismr)
n_plv_mov = 3
volc_time = utils.yearly_time_axis(dvolc)
plv_99p = np.genfromtxt("../statistical_significance/plv_99p_pmip3_ipsl.csv", delimiter=",", dtype=float) 
plv_95p = np.genfromtxt("../statistical_significance/plv_95p_pmip3_ipsl.csv", delimiter=",", dtype=float) 
delphi_5 = np.genfromtxt("../data/delphi_5.csv", delimiter=",", dtype=float) 
delphi_95 =  np.genfromtxt("../data/delphi_95.csv", delimiter=",", dtype=float) 
print("dvolc_source", dvolc_source[:5])
print(dvolc_source.shape, dvolc.shape)

# estimate climate anomalies
utils.printmsg("climate anomalies ...", verbose)
nino_anom = utils.climate_anomaly(dnino, time)
ismr_anom = utils.climate_anomaly(dismr, time)
print("Test2")

# filter the time series
utils.printmsg("filtered time series ...", verbose)
nino_filt = utils.iirfilter(nino_anom, N=5, pass_freq=8.0 / 12)
#nino_filt = utils.iirfilter(nino_anom, N=5, pass_freq=1.8 / 12)
ismr_filt = utils.iirfilter(ismr_anom, N=5, pass_freq=8.0 / 12)
#ismr_filt = utils.iirfilter(ismr_anom, N=5, pass_freq=1.8 / 12)
print("Test3")

# estimate the derivative of the filtered time series
utils.printmsg("time series derivatives ...", verbose)
nino_grad = np.gradient(nino_filt, 1)
ismr_grad = np.gradient(ismr_filt, 1)
print("Test4")

# use the Hilbert transform to estimate the phase of the signal
utils.printmsg("Hilbert transform ...", verbose)
nino_phi = np.unwrap(np.angle(signal.hilbert(nino_grad)))
ismr_phi = np.unwrap(np.angle(signal.hilbert(ismr_grad)))
print("Test5")

# calculate the instantaneous phase difference
utils.printmsg("instantaneous phase difference ...", verbose)
del_phi = ismr_phi - nino_phi
#del_phi = np.exp(np.complex(0,1)*(ismr_phi - nino_phi))
plv = np.zeros(len(dismr)-n_plv_mov*12)
for i in range(len(dismr)-n_plv_mov*12):
	plv[i] = utils.phase_locking_value(ismr_phi[i:i+n_plv_mov*12],nino_phi[i:i+n_plv_mov*12])
#print("Phase Locking Value ...",plv) 
#plv = np.exp(np.complex(0,1)*(ismr_phi - nino_phi))


delphi_fit = np.zeros((del_phi.shape[0]))  
#win = 60 
win = chunksize
delphi_fit[0:int(win/2)] = np.mean(del_phi[0:int(win/2)])
delphi_fit[del_phi.shape[0]-int(win/2):] = np.mean(del_phi[del_phi.shape[0]-int(win/2):])
for i in range(int(win/2), del_phi.shape[0]-int(win/2)):
	delphi_fit[i] = np.mean(del_phi[i-int(win/2):i+int(win/2)]) 
# compute gradient and get event series for times when gradient << 1

is_plateau = utils.zero_slope(delphi_fit, chunksize = chunksize, max_slope = max_slope) 
for i in range(2,is_plateau.shape[0]-2): 
	if (is_plateau[i-2]==is_plateau[i-1]==is_plateau[i+1]==is_plateau[i+2]):
		is_plateau[i] = is_plateau[i-1]
#print(is_plateau)  
idx = (is_plateau ==1.0)  
utils.printmsg("periods of phase locking ...", verbose)
perc = 10
pclo = 100. - perc
pchi = perc
del_phi_dot = np.gradient(del_phi, 3)
only_neg = del_phi_dot[del_phi_dot < 0.]
lothres = np.percentile(only_neg, pclo)
only_pos = del_phi_dot[del_phi_dot >= 0.]
hithres = np.percentile(only_pos, pchi)
ct = time.copy()
#idx = (del_phi_dot >= lothres) * (del_phi_dot <= hithres)
ampl = np.abs(signal.hilbert(nino_grad))
#idx = ampl*12 >0.8
te = ct[idx]
del_phi_phase_defined = del_phi[idx]
idx_time =plv > plv_95p  
time_coupling = plv_time[idx_time]  
np.savetxt("../output/time_coupling.csv", time_coupling, delimiter=",", fmt="%s")       
np.savetxt("../output/plv.csv", plv, delimiter=",", fmt="%s")       
np.savetxt("../output/delphi.csv", del_phi, delimiter=",", fmt="%s")       
np.savetxt("../output/delphi_fit.csv", delphi_fit, delimiter=",", fmt="%s")       
np.savetxt("../output/is_plateau.csv", is_plateau, delimiter=",", fmt="%s")       

# plot figures
utils.printmsg("output figures ...", verbose)
figs.input_timeseries(time, 
                      {# nino_dat
                         "anom": nino_anom,
                         "filt": nino_filt,
                         "grad": nino_grad,
                      },
                      {# ismr_dat
                         "anom": ismr_anom,
                         "filt": ismr_filt,
                         "grad": ismr_grad,
                      },
                      )
#figs.delphi_timeseries(ct, del_phi, time_coupling, volc_time, dvolc, plv_time, plv, plv_99p, dvolc_source)
figs.delphi_timeseries(ct, del_phi, te, volc_time, dvolc, plv_time, plv, plv_99p, dvolc_source, delphi_5, delphi_95, delphi_fit, max_slope, chunksize)
figs.plv_timeseries(plv_time, plv, te, volc_time, dvolc, plv_99p, plv_95p )
figs.delphi_histogram(del_phi_dot, lothres, hithres)
figs.amplitude_timeseries(ct, ampl, nino_grad,np.imag(signal.hilbert(nino_grad)) )
utils.printmsg("output defined phase ...", verbose)
utils.write_defined_phase(ct, te, del_phi_phase_defined/(2*np.pi))
