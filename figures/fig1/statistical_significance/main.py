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


def es(x, y, tau_max=10, time=[], onesided=False):
    """
    Returns the event synchronization count for two time series
    """
    # create arrays for event timings
    t_x = np.where(x)[0]
    t_y = np.where(y)[0]

    # array of all combinations of event timing differences
    t_xy = np.array([[t_[0], t_[1]] for t_ in product(t_x, t_y)])
    t_xy_diff = np.abs(t_xy[:, 1] - t_xy[:, 0])
    if onesided:            # set all pairs of t_y < t_x to infinity
        t_xy_diff[t_xy[:, 1] < t_xy[:, 0]] = int(1E12)

    # dynamic delay
    t_x_diff = np.r_[np.inf, t_x[1:] - t_x[:-1], np.inf]
    t_y_diff = np.r_[np.inf, t_y[1:] - t_y[:-1], np.inf]
    i_x, i_y = range(1, len(t_x) + 1), range(1, len(t_y) + 1)
    tau_dyn = np.array(
                    [
                        np.min(
                            [
                                t_x_diff[j[0] - 1],
                                t_x_diff[j[0]],
                                t_y_diff[j[1] - 1],
                                t_y_diff[j[1]]
                                ]
                            )
                        for j in product(i_x, i_y)
                        ]
                    )

    # implement the two conditions: for dynamic delay and for maximum delay
    c1 = t_xy_diff < tau_dyn
    c2 = t_xy_diff <= tau_max
    i = c1 * c2
    es_c = i.sum()

    # return time instances that contribute to event synchronisation count
    if len(time) > 0:
        out = es_c, time[t_xy[i]]
    else:
        out = es_c, None

    return out


def load_data():
    """Returns Nino3 and ISMR time series after laoding data from CSV files.
    """
    # load the data
    DATPATH = "../data/"
    fnino = DATPATH + "tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.csv"
    dnino = np.genfromtxt(fnino, delimiter=",", dtype=float).flatten()-273.15
    fismr = DATPATH + "pr_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_goswami_india_tseries.csv"
    dismr = np.genfromtxt(fismr, delimiter=",", dtype=float).flatten()*86400

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
    dnino, dismr = load_data()
    time = common_time_axis(dismr)

    # estimate climate anomalies
    print("climate anomalies ...", verbose)
    nino_anom = climate_anomaly(dnino, time)
    ismr_anom = climate_anomaly(dismr, time)

    # vrf data from sigl
    sigl = np.loadtxt("../data/sigl.txt")
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

    # # if there is an artefact from filtering which leads to a drift in the
    # # beginning and end of the filtered time series, mark these points as
    # # "noise" in the *_xi arrays so that they can be removed later when
    # # estimating the phase synchronization event series
    # # NOTE: In the case of the Maraun and Kurths approach to estimating the
    # # derivative of the filtered series, this artefact does not occur
    # nino_xi[:75] = True
    # nino_xi[-25:] = True
    # ismr_xi[:100] = True
    # ismr_xi[-25:] = True

    # # check plot
    # pl.clf()
    # pl.subplot(121)
    # pl.plot(nino_anly.real, nino_anly.imag, "k.-", alpha=0.25)
    # pl.plot(nino_anly.real[nino_xi], nino_anly.imag[nino_xi],
    #         "rx", alpha=0.25)
    # pl.subplot(122)
    # pl.plot(ismr_anly.real, ismr_anly.imag, "r.-", alpha=0.25)
    # pl.plot(ismr_anly.real[ismr_xi], ismr_anly.imag[ismr_xi],
    #         "kx", alpha=0.25)
    # pl.show()
    # sys.exit()

    # use the Hilbert transform to estimate the phase of the signal
    nino_phi = np.unwrap(np.angle(nino_anly))
    ismr_phi = np.unwrap(np.angle(ismr_anly))

    # phase difference
    del_phi = nino_phi - ismr_phi
    np.savetxt('nino_phi.txt',nino_phi)
    np.savetxt('ismr_phi.txt',ismr_phi)
    np.savetxt('del_phi.txt',del_phi)
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
    np.savetxt('psync.txt',psync)
    # event series
    e = psync.astype("int")

    # coarse grain event series to yearly resolution
    ps_yr = np.zeros(sigl.shape)
    for k in range(ps_yr.shape[0]):
        start = 12 * k
        stop = start + 12
        ps_yr[k] = e[start:stop].sum()

    # obtain events from coarse grained phase sync event series
    e_ps0 = (ps_yr >= 3.).astype("int")
    j = np.where(np.diff(e_ps0) == 1.)[0] + 1
    e_ps = np.zeros(e_ps0.shape)
    e_ps[j] = 1

    # # check plot: inter-arrival distributions
    # ia = np.diff(np.where(e_ps)[0])
    # hc, be = np.histogram(ia, bins="fd", density=True)
    # bc = 0.5 * (be[1:] + be[:-1])
    # pl.close(fig)
    # pl.figure()
    # pl.plot(bc, hc, "ko-")
    # pl.show()
    # sys.exit()


    er_sigl = e_sigl.sum() / e_sigl.shape[0] * 100
    print("Event rate of VRF series = %.2f%%" % er_sigl)
    er_ps = e_ps.sum() / e_ps.shape[0] * 100
    print("Event rate of phase synchronization series = %.2f%%" % er_ps)

    # # check plot
    # pl.clf()
    # t_ = time[::12]
    # pl.fill_between(time, e, 0., color="0.5")
    # pl.plot(t_, e_ps, "x-")
    # pl.plot(t_, e_sigl, "^-")
    # pl.show()
    # sys.exit()

    # get event synchronization counts and their p-value
    print("\t\tES count for obs data ...")
    es_c, t_xy = es(e_sigl, e_ps,
                    tau_max=TAUMAX, time=time[::12], onesided=True)
    print("\t\t\t%d" % es_c)
    print("\t\tES count for surr data ...")
    es_c_surr = np.zeros(NSURR)
    e_ps_i, e_sigl_i = [], []
    for k in range(NSURR):
        e_ps_i.append(np.random.permutation(dummy_i))
        e_sigl_i.append(np.random.permutation(dummy_i))

    for k in range(NSURR):
        if k % 10 == 0:
            print("\t\t\tk = ", k)
        es_c_surr[k], _ = es(e_sigl[e_sigl_i[k]], e_ps[e_ps_i[k]],
                             tau_max=TAUMAX, onesided=True)
    pv = 1. - percentileofscore(es_c_surr, es_c, kind="weak") / 100.
    print("\t\tp-value = %.6f" % pv)

    # plot
    #fig = pl.figure(figsize=[18., 10.])
    #ax1 = fig.add_axes([0.05, 0.70, 0.70, 0.225])
    #ax2 = fig.add_axes([0.05, 0.40, 0.70, 0.225])
    #ax3 = fig.add_axes([0.05, 0.10, 0.70, 0.225])
    #axes = [ax1, ax2, ax3]
    #axes[0].plot(time, del_phi, "o-", c="SteelBlue", alpha=0.5, ms=2.,
    #             label="cutoff = %.2f/12; filter order = %d, p-val = %.3f" % (c, N, pv)
    #             )
    #ylo, yhi = axes[0].get_ylim()
    #axes[0].fill_between(time, ylo, yhi,
    #                     where=psync, color="SteelBlue", alpha=0.5)
    #axes[1].plot(time, omega, "o-", c="SteelBlue", alpha=0.5, ms=2.,
    #             label="cutoff = %.2f/12; filter order = %d" % (c, N)
    #             )
    #h = axes[2].hist(omega, bins="fd", color="SteelBlue", alpha=0.5,
    #             histtype="step",
    #             label="cutoff = %.2f/12; filter order = %d" % (c, N)
    #             )
    #axes[2].axvline(lo, c="SteelBlue", ls="--", lw=0.5, alpha=0.5)
    #axes[2].axvline(hi, c="SteelBlue", ls="--", lw=0.5, alpha=0.5)

    ## last touches to plot
    #for ax in fig.axes:
    #    ax.legend(loc="upper right", bbox_to_anchor=[1.35, 1.10])
    #t_ = time[::12]
    #ax_ = axes[0].twinx()
    #ax_.bar(t_[e_sigl_bool], height=1., width=365., bottom=0.,
    #        edgecolor="Black", facecolor="Black", alpha=0.5)
    #ax_.bar(t_[e_ps0.astype("bool")], height=1., width=365., bottom=0.,
    #        edgecolor="LightSalmon", facecolor="Red", alpha=0.5)
    #ax_ = axes[1].twinx()
    #ax_.bar(t_[e_sigl_bool], height=0.0625, width=365., bottom=0.,
    #        edgecolor="Black", facecolor="Black", alpha=0.5)
    #ax_.bar(t_[e_ps0.astype("bool")], height=-0.0625, width=365., bottom=0.,
    #        edgecolor="LightSalmon", facecolor="Red", alpha=0.5)
    #ax_.bar(t_[e_ps.astype("bool")], height=-0.0625, width=365., bottom=0.,
    #        edgecolor="DarkRed", facecolor="Red", alpha=0.5)
    #ax_.bar(t_xy[:, 1], height=-0.0625/2., width=365., bottom=0.,
    #        edgecolor="DarkBlue", facecolor="DarkBlue", alpha=0.5)
    #pl.show()

    return None


if __name__ == "__main__":
    verbose = True
    runmain()
