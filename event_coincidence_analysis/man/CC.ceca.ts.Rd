\name{CC.ceca.ts}
%-------------------------------------------------------------------------------------------------
\alias{CC.ceca.ts}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
Function: Event Coincidence Analysis for three time series 
}
\description{
This function performs the Conditioned Event Coincidence Analysis using three data sets A, B and C of event time series format (ts). NAs are allowed.
CECA is an extension of the Event Coincidence Analysis for three time series, where ECA is performed between series A and B as known from ECA, but events in B only account for coincidences, if they are conditioned by events in C. The conditioning parameters delT.cond and tau.cond work the same way as the parameters delT and tau, but between seriesB and seriesC. The conditionind of C on B is realised in terms of precursor coincidence. Further information and a conceptional illustration can be found at:
Siegmund et al. (2016), Frontiers in Plant Scienes: http://journal.frontiersin.org/article/10.3389/fpls.2016.00733/full
}
\usage{
CC.ceca.ts(seriesA,seriesB,seriesC,alpha=0.05,delT=0,delT.cond=0,sym=FALSE,sym.cond=FALSE,tau=0,tau.cond=0,sigtest="poisson",reps=1000)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{seriesA}{
Time series A. Numeric vector or one-row-matrix containing a time series of binary data (0,1) with all time steps of interest, where a '1' denotes a time step with, and a '0' a time step without event.
SeriesA, series B and seriesC need to be of same length and may contain missing values.
}
  \item{seriesB}{
Time series B. Numeric vector or one-row-matrix containing a time series of binary data (0,1) with all time steps of interest, where a '1' denotes a time step with, and a '0' a time step without event.
SeriesA, series B and seriesC need to be of same length and may contain missing values.
}
  \item{seriesC}{
Time series C. Numeric vector or one-row-matrix containing a time series of binary data (0,1) with all time steps of interest, where a '1' denotes a time step with, and a '0' a time step without event.
SeriesA, series B and seriesC need to be of same length and may contain missing values.
}
  \item{alpha}{
Value between [0 1], default=0.05. 
The significance level 'alpha' of the significance test. null hypothesis: The found coincidence rates result from randomly, independently distributed event time series.
}
  \item{delT}{
Positive value [1 inf], default = 1. 
Tolerance window delta T. delT describes the temporal tolerance window in which coincidences may occur. 
If e.g. delT=3, an event in seriesA occurring simultaneously or one, two or three time steps after an event in seriesB
also counts for a coincidence (K). With delT=0 only simultaneous events are counted for coincidences, for e.g. delT=1 the tolerance window is extended by one time step. 
}
  \item{delT.cond}{
Positive value [1 inf], default = 1. 
Tolerance window delta T for the conditioning between seriesC and seriesB. delT describes the temporal tolerance window in which coincidences may occur. 
If e.g. delT=3, an event in seriesC occurring simultaneously or one, two or three time steps before an event in seriesB
counts for conditioning of the event in B. With delT=0, only simultaneous events are counted for conditioning. 
}
  \item{sym}{
  TRUE or FALSE, default = FALSE.
  FALSE: non-symmetrical tolerance window. In case of the precursor coincidence, the window starts at t-tau and ends at t-tau-delT, for trigger coincidence, the window starts at t+tau and ends at t+tau+delT.
  TRUE: symmetrical tolerance window. The tolerance window is symmetrically placed around t-tau and t+tau, respectively. For precursor coincidence, the window starts at t-tau+delT and ends at t-tau-delT, for trigger coincidence the window starts at t+tau-delT and ends at t+tau+delT
 }
   \item{sym.cond}{
  TRUE or FALSE, default = FALSE.
  FALSE: non-symmetrical tolerance window for the conditioning of B events by C events.
  TRUE:      symmetrical tolerance window for the conditioning of B events by C events. The tolerance window is symmetrically placed around t-tau.cond and t+tau.cond, respectively.
 }
  \item{tau}{
Positive value [0 inf], default = 0. 
Time lag parameter tau allows for shifted events to be counted for coincidences (K). If e.g. tau=5, an event
in seriesA occurring exactly 5 time steps after an event in seriesB also counts for coincidence (K).
}
  \item{tau.cond}{
Positive value [0 inf], default = 0. 
Time lag parameter tau.cond allows for shifted events to be counted for the conditioning. If e.g. tau=5, an event
in seriesC occurring exactly 5 time steps before an event in seriesB counts for the conditioning.
}
  \item{sigtest}{
    Character specifying the type of significance test, default = "poisson". 
    "poisson": significance test based on the calculation of the probability that the empirical coincidence rate would occur for two random (poisson-process) time series.
    "wt.surrogate": significance test based on the calculation of event coincidence analysis for a large number of surrogate time series having the same average waiting time between two events.
    "shuffle.surrogate": significance test based on the calculation of event coincidence analysis for a large number of randomly shuffled time series having the same number of events like the original time series.
}
  \item{reps}{
    Positive whole number [100, inf], default = "1000". 
    Number of surrogate/shuffled time series to be produced for the "surrogate" or "shuffle" significance test. 
}
}

\value{
## Output: list, containing seven elements ##
\item{NH precursor}{                 Logical, null hypothesis for precursor coincidence rate accepted}
\item{NH trigger}{                Logical, null hypothesis for trigger coincidence rate accepted}
\item{p-value precursor}{                    Numeric, p-value used for the precursor significance test}
\item{p-value trigger}{                   Numeric, p-value used for the trigger significance test}
\item{conditional precursor coincidence rate}{Numeric, precursor coincidence rate}
\item{conditional trigger coincidence rate}{  Numeric, precursor coincidence rate}

}
\references{
Siegmund, J. et al. (2016): Meteorological Drivers of Extremes in Daily Stem Radius Variations of Beech, Oak, and Pine in Northeastern Germany: An Event Coincidence Analysis. Frontiers in Plant Sciences, 7 , 733. http://journal.frontiersin.org/article/10.3389/fpls.2016.00733/full
}
\author{
Jonatan Siegmund, Potsdam Institute for Climate Impact Research
}

