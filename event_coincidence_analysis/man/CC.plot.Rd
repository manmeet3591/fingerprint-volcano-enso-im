\name{CC.plot}
%-------------------------------------------------------------------------------------------------
\alias{CC.plot}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
Function: Plots an illustration of the results of a performed coincidence analysis.
}
\description{
This function creates a plot, that shall illustrate the results of an event coincidence analysis for a given pair of binary event time series. CC.plot only works for event time series format (ts).
For a plot with event series format, use CC.es2ts() first.
}

\usage{
CC.plot(seriesA,seriesB,delT=0,sym=FALSE,tau=0,dates=NA,seriesAname="Event Series A",
seriesBname="Event Series B")
}

\arguments{
  \item{seriesA}{
Time series A. Numeric vector or one-row-matrix containing a time series of binary data (0,1) with all time steps of interest, where a '1' denotes a time step with, and a '0' a time step without event.
SeriesA and seriesB need to be of same length. Both may contain missing values.}
  \item{seriesB}{
Time series B. Numeric vector or one-row-matrix containing a time series of binary data (0,1) with all time steps of interest, where a '1' denotes a time step with, and a '0' a time step without event.
SeriesA and seriesB need to be of same length. Both may contain missing values.
}
  \item{delT}{
Positive whole number [1 inf], default = 1. 
Tolerance window delta T. delT describes the temporal tolerance in which coincidences may occur. 
If e.g. delT=3, an event in seriesA occurring simultaneously or one or two time steps after an event in seriesB
also counts for a coincidence (K). With delT=1 only simultaneous events are counted for coincidences.
}
  \item{sym}{
  TRUE or FALSE, default = FALSE.
  FALSE: non-symmetrically tolerance window. In case of the precursor coincidence, the window starts at t-tau and ends at t-tau-delT, for trigger coincidence, the window starts at t+tau and ends at t+tau+delT.
  TRUE: symmetrical tolerance window. The tolerance window is symmetrically placed around t-tau and t+tau, respectively. For precursor coincidence, the window starts at t-tau+delT and ends at t-tau-delT, for trigger coincidence the window starts at t+tau-delT and ends at t+tau+delT
 }
   \item{tau}{
Positive whole number [1 inf], default = 0. 
Time lag parameter tau allows for shifted events to be counted for coincidences (K). If e.g. tau=5, an event
in seriesA occurring exactly 5 time steps after an event in seriesB also counts for coincidence (K).
}
   \item{dates}{
Character vector or numeric vector of length=length(seriesA), default = NA. 
Vector providing date information for the time series. If given, event dates are added to the plot.
}
   \item{seriesAname}{
Name of the Event Series A to be plottet, default = "Event Series A"
}
   \item{seriesBname}{
Name of the Event Series B to be plottet, default = "Event Series B"
}
}

\references{
Siegmund, J., Seigmund, N. and Donner, R. (2015): CoinCalc - An R package for quantifying simultaneities 
of events in two event (time) series. Submitted to Computers and Geosciences.
Donges, J. F., Schleussner, C. F., Siegmund, J. F., and Donner, R. V. (2015): Coincidence analysis
for quantifying statistical interrelationships between event time series, arXiv:1508.03534.
}
\author{
Jonatan Siegmund, Potsdam Institute for Climate Impact Research
}
\examples{

# Example:
# First we load the two data sets April.Tmean.Niederrimbach and Lilac.Flowering.Niederrimbach,
# supplied by CoinCalc and binarize both
library(CoinCalc)
data(CC.Example.Data1)
Flow_bin=CC.binarize(CC.Example.Data1$DOY_Lilac_Flowering,ev.def="percentile",
        thres=0.1,event="lower")
Tmean_bin=CC.binarize(CC.Example.Data1$April_Tmean,ev.def="percentile",thres=0.9,
        event="higher")
CC.plot(Flow_bin,Tmean_bin,tau=0,delT=1,dates=CC.Example.Data1$YEAR,
        seriesAname="Flowering events",seriesBname="Tmean events")

# Note, that here we use data of ts format and thus have to set delT=1 for 
# counting simultaneous coincidences.
# Result: a nice plot, illustrating the coincidences and the years in which they occured.
}
