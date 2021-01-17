#! /usr/bin/env python3
"""
Explore the various aspects of Fig 1
====================================


"""
# Created: Thu Oct 12, 2017  02:37PM
# Last modified: Sun Sep 01, 2019  04:46pm
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>


import sys
import numpy as np
from scipy import signal
from scipy.stats import percentileofscore, norm
import datetime as dt
import matplotlib.pyplot as pl
import matplotlib.dates as mdates
from itertools import product

from scipy.ndimage import uniform_filter1d


def load_data(surr):
    """Returns Nino3 and ISMR time series after laoding data from CSV files.
    """
    # load the data
    DATPATH = "data_ipsl_pi/"
    fnino = DATPATH + "tas_Amon_IPSL-CM5A-LR_piControl_r1i1p1_180001-279912_nino3_tseries.csv"
    dnino = np.genfromtxt(fnino, delimiter=",", dtype=float).flatten()-273.15
    fismr = DATPATH + "pr_Amon_IPSL-CM5A-LR_piControl_r1i1p1_180001-279912_goswami_india_tseries.csv"
    dismr = np.genfromtxt(fismr, delimiter=",", dtype=float).flatten()*86400
    print(dismr.shape, dnino.shape)

    # simple check for data consistency
    assert dnino.shape == dismr.shape, "Data sets are unequal!"

    return dnino, dismr


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


def climate_anomaly(x, t):
    """
    Returns climate anomaly of 'x' wrt 1/1/1971-31/12/1980 climate normal.
    """
    # climate normal period := January 1971 to December 1980
    d1 = dt.datetime(850, 1, 1)
    d2 = dt.datetime(1850, 12, 31)
    idx = np.where((t >= d1) * (t <= d2))[0]
    x_clim = x[idx].mean()
    x_anom = x - x_clim

    return _quantile_normalization(x_anom, mode="mean")


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


def iirfilter(x, N=4, cutoff=12., fs=12.):
    """
    Returns the forward-backward filtered signal using a Butterworth filter.
    """
    nyq = 0.5 * fs
    cutoff_normed = cutoff / nyq
    b, a = signal.butter(N, cutoff_normed, "low", analog=False)
    return  signal.filtfilt(b, a, x, padtype=None)


def boxfilter(x, size=5, est="mean"):
    """Returns the box filter of array"""
    n = x.shape[0]
    if est == "mean":
        xf_pre = np.r_[x[0], [x[:i].mean() for i in range(1, size)]]
        xf_post = [np.mean(x[i-size:i]) for i in range(size, n)]
    elif est == "median":
        xf_pre = np.r_[x[0], [np.median(x[:i]) for i in range(1, size)]]
        xf_post = [np.median(x[i-size:i]) for i in range(size, n)]
    elif est == "max":
        xf_pre = np.r_[x[0], [np.max(x[:i]) for i in range(1, size)]]
        xf_post = [np.max(x[i-size:i]) for i in range(size, n)]
    xf = np.r_[xf_pre, xf_post]
    return xf


def runmain():
    """Core part of the script"""
    # load data and create common time axis array
    print("load data ...", verbose)
    surr = sys.argv[1]

    dnino, dismr = load_data(surr)
    time = common_time_axis(dismr)

    # estimate climate anomalies
    print("climate anomalies ...", verbose)
    nino_anom = climate_anomaly(dnino, time)
    ismr_anom = climate_anomaly(dismr, time)

    # vrf data from sigl
    sigl = np.loadtxt("./sigl.txt")
    sigl = sigl[:-1]
    sigl = np.log(1. - sigl)
    vrf_thr = np.percentile(sigl[sigl>0.], 1.)
    e_sigl_bool = sigl > vrf_thr
    e_sigl = e_sigl_bool.astype("int")

    # # check plot
    # pl.hist(sigl[sigl > 0.], bins="fd")
    # pl.axvline(vrf_thr, c="r")
    # pl.title("%.3f" % (1. - np.exp(vrf_thr)))
    # pl.show()
    # sys.exit()

    # dummy time
    dummy_i = np.arange(len(sigl))

    # filter the time series
    print("sensitivity of filtered time series ...", verbose)
    c = 3. / 4.                 # numerator of cutoff freq
    cutoff_den = 12.
    N = 1.                      # filter order of the Butterworth filter
    fs = 12.                    # 12 samples per year
    NSURR = 100
    TAUMAX = 5.
    CI_WD = 25.
    cutoff_num = c
    cut = cutoff_num / cutoff_den
    nino_filt = iirfilter(nino_anom, N=N, cutoff=cut, fs=fs)
    ismr_filt = iirfilter(ismr_anom, N=N, cutoff=cut, fs=fs)

    #### estimate the derivative of the filtered time series
    # based on Maraun and Kurths approach
    nino_diff = np.diff(nino_filt, n=2)
    nino_diff = np.r_[nino_diff[0], nino_diff[0], nino_diff]
    ismr_diff = np.diff(ismr_filt, n=2)
    ismr_diff = np.r_[ismr_diff[0], ismr_diff[0], ismr_diff]
    nino_grad = boxfilter(nino_diff, size=12)
    ismr_grad = boxfilter(ismr_diff, size=12)

    # # check plot
    # pl.subplot(211)
    # pl.plot(time, nino_anom, "c-", alpha=0.5)
    # pl.plot(time, nino_filt, "k-", alpha=0.5)
    # pl.twinx()
    # pl.plot(time, nino_grad, "r-", alpha=0.5)
    # pl.subplot(212)
    # pl.plot(time, ismr_anom, "c-", alpha=0.5)
    # pl.plot(time, ismr_filt, "k-", alpha=0.5)
    # pl.twinx()
    # pl.plot(time, ismr_grad, "r-", alpha=0.5)
    # pl.show()
    # sys.exit()

    # compute the analytical signal using Hilbert transform
    nino_anly = signal.hilbert(nino_grad)
    ismr_anly = signal.hilbert(ismr_grad)
    # nino_xi = np.zeros(nino_anly.shape).astype("bool")
    # ismr_xi = np.zeros(ismr_anly.shape).astype("bool")
    nino_xi = (nino_anly.real ** 2 + nino_anly.imag ** 2) <  0.00007 ** 2
    ismr_xi = (ismr_anly.real ** 2 + ismr_anly.imag ** 2) < 0.00003 ** 2

    
    # use the Hilbert transform to estimate the phase of the signal
    nino_phi = np.unwrap(np.angle(nino_anly))
    ismr_phi = np.unwrap(np.angle(ismr_anly))

    # phase difference
    del_phi = nino_phi - ismr_phi
    np.savetxt('data_ipsl_pi/nino_phi'+str(surr)+'.txt',nino_phi)
    np.savetxt('data_ipsl_pi/ismr_phi'+str(surr)+'.txt',ismr_phi)
    np.savetxt('data_ipsl_pi/del_phi'+str(surr)+'.txt',del_phi)
    # # check plot
    # pl.clf()
    # pl.plot(time, nino_phi, "k.-")
    # pl.plot(time, ismr_phi, "r.-")
    # pl.plot(time, del_phi, "c.-")
    # pl.show()
    # # sys.exit()

    # confidence interval around zero based on phase speeds
    del_phi_diff = np.diff(del_phi, n=2)
    del_phi_diff = np.r_[del_phi_diff[0], del_phi_diff[0], del_phi_diff]
    del_phi_grad = boxfilter(del_phi_diff, size=12)
    omega = del_phi_grad
    omega_pos = omega[omega>=0.]
    hi = np.percentile(omega_pos, CI_WD / 2.)  # upper threshold
    omega_neg = omega[omega<0.]
    lo = np.percentile(omega_neg, (100. - CI_WD / 2.)) # lower threshold
    psync = (omega > lo) * (omega < hi)
    psync = psync * (~nino_xi) * (~ismr_xi)
    np.savetxt('data_ipsl_pi/psync'+str(surr)+'.txt',psync)

if __name__ == "__main__":
    verbose = True
    runmain()
