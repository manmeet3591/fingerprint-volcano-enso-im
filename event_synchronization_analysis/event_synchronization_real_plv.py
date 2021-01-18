
# coding: utf-8

# Event Synchronization Analysis following 
# https://github.com/pik-copan/pyunicorn/blob/master/tests/test_funcnet/TestEventSyncronization.py
# and 
# https://vis.caltech.edu/~rodri/papers/event_synchro.pdf

# In[1]:


import sys, string
from matplotlib import rc
import numpy as np
import pylab as pl
import netCDF4
import time as t
import datetime
from dateutil.parser import parse
from pylab import load, meshgrid, title, arange, show
from netcdftime import utime
import scipy.io
import matplotlib as mpl
import argparse
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
import datetime as dt
from netCDF4 import num2date, date2num
import random
from mpi4py import MPI
#import Nio
#from pyhdf.SD import SD


# In[2]:


def EventSync(es1, es2, taumax):
    """
    Compute non-vectorized event synchronization
    :type es1: 1D Numpy array
    :arg es1: Event series containing '0's and '1's
    :type es2: 1D Numpy array
    :arg es2: Event series containing '0's and '1's
    :float return: Event synchronization es2 to es1
    """
    ex = np.arange(len(es1))[es1 == 1]
    ey = np.arange(len(es2))[es2 == 1]
    lx = len(ex)
    ly = len(ey)

    count = 0
    if lx!=0 and ly!=0:
	    for m in range(1, lx-1):
	        for n in range(1, ly-1):
	            dst = ex[m] - ey[n]
	
	            if abs(dst) > taumax:
	                continue
	            elif dst == 0:
	                count += 0.5
	                continue
	
	            # finding the dynamical delay tau
	            tmp = ex[m+1] - ex[m]
	            if tmp > ex[m] - ex[m-1]:
	                tmp = ex[m] - ex[m-1]
	            tau = ey[n+1] - ey[n]
	            if tau > ey[n] - ey[n-1]:
	                tau = ey[n] - ey[n-1]
	            if tau > tmp:
	                tau = tmp
	            tau = tau / 2
	
	            if dst > 0 and dst <= tau:
	                count += 1

    #print("count = ",count) 
    #print("Q = ",np.sqrt((lx-2) * (ly-2))) 
    #print("lx,ly,Q =",lx,ly,count) 
    if lx!=0 and ly!=0: 
    	return count / np.sqrt((lx) * (ly))
    	#return count / np.sqrt((lx-2) * (ly-2))
    else:
    	return 0.0

def common_time_axis(dismr, verbose=True):
    """
    Generates common time axis for Nino3 and ISMR time series.
    """
    # generate the time axis
    Nt = len(dismr)
    time = [dt.datetime(854, 1, 15)]
    for i in range(1, len(dismr)):
        y = time[i - 1].year
        m = time[i - 1].month
        if m == 12:
            y += 1
            m = 0
        time.append(dt.datetime(y, m + 1, 15))
    time = np.array(time)
    
def my_shuffle(array):
    random.shuffle(array)
    return array


# In[3]:


plv_pi = np.genfromtxt ('plv_pi.csv', delimiter=",")
plv_hist = np.genfromtxt ('plv_hist.csv', delimiter=",")[:11964,]
plv_99p_pi = np.genfromtxt('plv_95p_pmip3_ipsl_pi.csv', delimiter=",")
plv_99p_hist = np.genfromtxt('plv_95p_pmip3_ipsl_hist.csv', delimiter=",")[:11964,]
volc_sigl = -1*np.genfromtxt ('sigl.txt', delimiter=",")

volc_data = volc_sigl[1:997]
volc_data_mon = np.zeros((997*12))
volc_data_mon[0:6] = volc_data[0]
volc_data_mon[11958:11964] = volc_data[-1]
for yyyy in range(995):
    #print(yyyy)
    volc_data_mon[6+yyyy*12:18+yyyy*12] = volc_data[1+yyyy]

print(plv_99p_pi.shape)
print(plv_99p_hist.shape)
print(volc_data_mon.shape)


# In[4]:


es_pi = np.zeros((plv_pi.shape[0]))
es_hist = np.zeros((plv_hist.shape[0]))
es_volc =np.zeros((volc_data_mon.shape[0]))

es_pi[plv_pi>=plv_99p_pi] = 1.0
es_hist[plv_hist>=plv_99p_hist] = 1.0
es_volc[volc_data_mon>=3.7] = 1.0

print(np.sum(es_pi))
print(np.sum(es_hist))
print(np.sum(es_volc))

#print(max(plv_hist))
#print(plv_99p_hist)
#Testing random shuffle

#def my_shuffle(array):
#    random.shuffle(array)
#    return array
#test=np.zeros(5)
#for i in range(5):
#    test[i]=i
#import random
#print(test)
#print(my_shuffle(test))


# In[ ]:


taumax = 60
N = 1 
#Q_pi = EventSync(es_pi, es_volc, taumax) + EventSync(es_volc, es_pi, taumax)
#Q_hist = EventSync(es_hist, es_volc, taumax) + EventSync(es_volc, es_hist, taumax)
#print(Q_pi)
#print(Q_hist)

Q_pi = np.zeros((es_pi.shape[0]-taumax))
Q_hist = np.zeros((es_hist.shape[0]-taumax))
Q_pi_mc = np.zeros((es_pi.shape[0]-taumax,N))
Q_hist_mc = np.zeros((es_hist.shape[0]-taumax,N))


es_pi_mc = np.zeros((plv_pi.shape[0]))
es_hist_mc = np.zeros((plv_hist.shape[0]))

for i in range(es_pi.shape[0]-taumax):
#    Q_pi[i] = EventSync(es_pi[i:i+taumax], es_volc[i:i+taumax], taumax) + EventSync(es_volc[i:i+taumax], es_pi[i:i+taumax],taumax)
#    print(EventSync(es_pi[i:i+taumax], es_volc[i:i+taumax], taumax),EventSync(es_volc[i:i+taumax], es_pi[i:i+taumax],taumax))
#    print(EventSync(es_pi[i:i+taumax], es_volc[i:i+taumax], taumax)+EventSync(es_volc[i:i+taumax], es_pi[i:i+taumax],taumax))
    Q_hist_hv = EventSync(es_hist[i:i+taumax], es_volc[i:i+taumax], taumax)
    Q_hist_vh = EventSync(es_volc[i:i+taumax], es_hist[i:i+taumax],taumax)
    Q_hist[i] = Q_hist_hv + Q_hist_vh
    #print(Q_hist_hv,Q_hist_vh)

#np.savetxt("Q_pi"+sys.argv[1] +".csv", Q_pi, delimiter=",")
np.savetxt("Q_hist"+sys.argv[1] +".csv", Q_hist, delimiter=",")
# In[ ]:


mon_time = common_time_axis(es_pi)

