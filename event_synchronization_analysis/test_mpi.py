
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

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# Calculating p99 and p95 values using Monte Carlo simulation
print("Hello from proc",rank)

