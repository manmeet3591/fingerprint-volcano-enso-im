#! /usr/bin/env python
"""
Use the functions phaselock.py to estimate phase locking between ISMR & NINO3
=============================================================================


"""
# Created: Thu Oct 12, 2017  02:37PM
# Last modified: Sat Feb 23, 2019  09:09pm
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>


import sys
import numpy as np
from scipy import signal
from scipy.stats import percentileofscore, norm
import datetime as dt
import matplotlib.pyplot as pl
import matplotlib.dates as mdates
import utils

def load_data():
    """Returns Nino3 and ISMR time series after laoding data from CSV files.
    """
    # load the data
    DATPATH = "../data/"
    #fnino = DATPATH + "tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.csv"
    fnino = DATPATH + "tas_Amon_IPSL-CM5A-LR_piControl_r1i1p1_180001-279912_nino3_tseries.csv"
    dnino = np.genfromtxt(fnino, delimiter=",", dtype=float).flatten()-273.15
    fismr = DATPATH + "pr_Amon_IPSL-CM5A-LR_piControl_r1i1p1_180001-279912_goswami_india_tseries.csv"
    #fismr = DATPATH + "pr_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_goswami_india_tseries.csv"
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
    #d1 = dt.datetime(850, 1, 1)
    #d2 = dt.datetime(1850, 12, 31)
    #idx = np.where((t >= d1) * (t <= d2))[0]
    #x_clim = x[idx].mean()
    x_clim = np.zeros((x.shape[0]))
    win = 30
    x_clim[0:int(win/2)] = np.mean(x[0:win])
    x_clim[x.shape[0]-int(win/2):x.shape[0]] = np.mean(x[x.shape[0]-win:x.shape[0]])
    for i in range(x.shape[0]-win):
        x_clim[i+int(win/2)] = np.mean(x[i:i+win])

    x_anom = x - x_clim
    print(x_anom,x)

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


def printmsg(msg, verbose):
    """
    Prints info messages to stdout depending on given verbosity.
    """
    if verbose:
        print(msg)

    return None


def plot(time, nino_dat, ismr_dat, c, N):
    """
    Plots input time series, filtered time series, and phase space plots.
    """
    # parse the input data
    nino_anom = nino_dat["anom"]
    nino_filt = nino_dat["filt"]
    nino_grad = nino_dat["grad"]
    ismr_anom = ismr_dat["anom"]
    ismr_filt = ismr_dat["filt"]
    ismr_grad = ismr_dat["grad"]

    # set up figure
    fig = pl.figure(figsize=[7.08, 7.08])
    axlabfs, tiklabfs, splabfs = 11, 9, 13

    # set up first axis and plot the NINO index
    ax1 = fig.add_axes([0.10, 0.700, 0.85, 0.210])
    ax1.plot(time, nino_anom,
             c="SteelBlue", label="Original", linewidth=0.5)
    ax1.plot(time, nino_filt,
             c="Tomato",
             label="Filtered",
             linewidth=0.5)

    # set up second axis and plot the ISMR index
    ax2 = fig.add_axes([0.10, 0.525, 0.85, 0.175])
    ax2.plot(time, ismr_anom,
             c="SteelBlue", label="Original", linewidth=0.5)
    ax2.plot(time, ismr_filt,
             c="Tomato",
             label="Filtered",
             linewidth=0.5)

    # set up third axis and plot the estimated phases from filtered NINO
    ax3 = fig.add_axes([0.125, 0.10, 0.35, 0.35])
    ax3.plot(nino_grad, np.imag(signal.hilbert(nino_grad)),
             c="Tomato", linewidth=0.5)

    # set up fourth axis and plot the estimated phases from filtered ISMR
    ax4 = fig.add_axes([0.625, 0.10, 0.35, 0.35])
    ax4.plot(ismr_grad, np.imag(signal.hilbert(ismr_grad)),
             c="Tomato", linewidth=0.5)

    # prettify ax1 and ax2
    xlo, xhi = dt.datetime(850, 1, 1), dt.datetime(1850, 12, 31)
    for ax in [ax1, ax2]:
        ax.set_xlim(xlo, xhi)
        XMajorLocator = mdates.YearLocator(base=100, month=6, day=15)
        XMinorLocator = mdates.YearLocator(base=10, month=6, day=15)
        # XMinorLocator = mdates.MonthLocator(bymonthday=15, interval=3)
        XMajorFormatter = mdates.DateFormatter("%Y")
        ax.xaxis.set_major_locator(XMajorLocator)
        ax.xaxis.set_minor_locator(XMinorLocator)
        ax.xaxis.set_major_formatter(XMajorFormatter)
        ax.set_ylim(-3.0, 3.0)
        ax.set_yticks(np.arange(-2.0, 2.01, 1.0))
        ax.grid(which="both")
        ax.tick_params(which="major", axis="both", size=8, direction="out")
        ax.tick_params(which="minor", axis="both", size=5, direction="out")
        ax.tick_params(axis="both", labelsize=tiklabfs)
    leg = ax1.legend(loc="upper right")
    for txt in leg.get_texts():
        txt.set_size(tiklabfs)
    ax1.set_ylim(-4., 4.)
    ax1.tick_params(bottom="off", top="on", which="both",
                    labelbottom="off", labeltop="on")
    ax2.set_xlabel("Time", fontsize=axlabfs)
    ax1.set_xlabel("Time", fontsize=axlabfs)
    ax1.xaxis.set_label_position("top")
    ax1.set_ylabel("Nino 3", fontsize=axlabfs)
    ax2.set_ylabel("ISMR", fontsize=axlabfs)

    # prettify ax3 and ax4
    ax3.set_xlabel("Derivative of filtered Nino 3 signal",
                   fontsize=axlabfs)
    ax3.set_ylabel("Hilbert transform",
                   fontsize=axlabfs)
    ax4.set_xlabel("Derivative of filtered ISMR signal",
                   fontsize=axlabfs)
    ax4.set_ylabel("Hilbert transform",
                   fontsize=axlabfs)
    for ax in [ax3, ax4]:
        ax.grid()
        ax.tick_params(axis="both", labelsize=tiklabfs)
        ax.tick_params(which="major", size=8)

    ax1.text(0.01, 1.30,
            "Cutoff Freq. = %d / 12 yrs" % c,
            ha="left", va="center", fontsize=12,
            bbox={"facecolor": "LightCoral", "alpha": 0.5},
            transform=ax1.transAxes,
            )
    ax1.text(0.99, 1.30,
            "Filter order = %d" % N,
            ha="right", va="center", fontsize=12,
            bbox={"facecolor": "LightCoral", "alpha": 0.5},
            transform=ax1.transAxes,
            )

    return fig


def close(fig):
    """Deletes the figure instance"""
    pl.close(fig)
    return None

def runmain():
    """Core part of the script"""
    # load data and create common time axis array
    printmsg("load data ...", verbose)
    dnino, dismr = load_data()
    time = common_time_axis(dismr)

    # estimate climate anomalies
    printmsg("climate anomalies ...", verbose)
    nino_anom = climate_anomaly(dnino, time)
    ismr_anom = climate_anomaly(dismr, time)

    # filter the time series
    printmsg("sensitivity of filtered time series ...", verbose)
    cutoff_num = np.arange(9., 10., 1.)
    cutoff_den = 12.
    filter_order = np.arange(9, 10)
    fs = 12.                    # 12 samples per year
    for c in cutoff_num:
        cut = c / cutoff_den
        for N in filter_order:
            nino_filt = iirfilter(nino_anom, N=N, cutoff=cut, fs=fs)
            ismr_filt = iirfilter(ismr_anom, N=N, cutoff=cut, fs=fs)
            # estimate the derivative of the filtered time series
            nino_grad = np.gradient(nino_filt, 5)
            ismr_grad = np.gradient(ismr_filt, 5)

            # use the Hilbert transform to estimate the phase of the signal
            nino_phi = np.unwrap(np.angle(signal.hilbert(nino_grad)))
            ismr_phi = np.unwrap(np.angle(signal.hilbert(ismr_grad)))
            del_phi = ismr_phi - nino_phi
            delphi_fit = np.zeros((del_phi.shape[0]))
            max_slope = 0.045
            #max_slope = 0.03
            chunksize = 120
            win = chunksize
            delphi_fit[0:int(win/2)] = np.mean(del_phi[0:win])
            delphi_fit[del_phi.shape[0]-int(win/2):] = np.mean(del_phi[del_phi.shape[0]-win:])
            for i in range(int(win/2), del_phi.shape[0]-int(win/2)):
                delphi_fit[i] = np.mean(del_phi[i-int(win/2):i+int(win/2)])
            is_plateau = utils.zero_slope(delphi_fit, chunksize = chunksize, max_slope = max_slope)
            for i in range(2,is_plateau.shape[0]-2):
                if (is_plateau[i-2]==is_plateau[i-1]==is_plateau[i+1]==is_plateau[i+2]):
                    is_plateau[i] = is_plateau[i-1]
                                #print(is_plateau)  
            np.savetxt("../output/delphi.csv", del_phi, delimiter=",", fmt="%s")
            np.savetxt("../output/nino_phi.csv", nino_phi, delimiter=",", fmt="%s")
            np.savetxt("../output/ismr_phi.csv", ismr_phi, delimiter=",", fmt="%s")
            np.savetxt("../output/delphi_fit.csv", delphi_fit, delimiter=",", fmt="%s")
            np.savetxt("../output/is_plateau.csv", is_plateau, delimiter=",", fmt="%s")


            # plot
            fig = plot(time,
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
                       c, N,
                       )

            # save figure
            #FN = "../plots/"
            #FN += "cutoff%dby%d_forder%d.png" % (int(c), int(cutoff_den), N)
            FN = "figure_filtered_timeseries.pdf" 
            fig.savefig(FN, dpi=1000)
            printmsg("figure saved to: %s" %FN, verbose)
            close(fig)

    return None


if __name__ == "__main__":
    verbose = True
    runmain()
