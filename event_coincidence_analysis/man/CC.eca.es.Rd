\name{CC.eca.es}
%-------------------------------------------------------------------------------------------------
\alias{CC.eca.es}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
Function: Event Coincidence Analysis for two event series
}
\description{
This function performs the event coincidence analysis using two data sets of event series format (es). NAs are not allowed.

}
\usage{
CC.eca.es(seriesA, seriesB, spanA, spanB, delT, alpha=0.05, 
                sym=FALSE, tau=0, sigtest="poisson", reps=1000)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{seriesA}{
Time series A. Numeric vector containing a set of values specifying only the (e.g. time-) steps that denote an event.
SeriesA and seriesB do not need to be of same length. Both may not contain missing values.
}
  \item{seriesB}{
Time series B. Numeric vector containing a set of values specifying only the (e.g. time-) steps that denote an event.
SeriesA and seriesB do not need to be of same length. Both may not contain missing values.
}
  \item{spanA}{
Vector containing two integers. spanA specifies the start and end point of the data set given in seriesA.
}
  \item{spanB}{
Vector containing two integers. spanB specifies the start and end point of the data set given in seriesB.
}
  \item{alpha}{
Value between [0 1], default=0.05. 
The significance level 'alpha' of the significance test. null hypothesis: The found coincidence rates result from randomly, independently distributed event time series.
}
  \item{delT}{
Positive value ]0 inf]. Mandatory. 
Tolerance window delta T. delT describes the temporal tolerance window in which coincidences may occur. 
If e.g. delT=3, an event in seriesA occurring simultaneously or in the period between 0 and 3 after an event in seriesB
also counts for a coincidence (K). If delT equals the minimum resolution (number of digits in seriesA+1), only simultaneous events are counted for coincidences.
}
  \item{sym}{
  TRUE or FALSE, default = FALSE.
  FALSE: non-symmetrically tolerance window. In case of the precursor coincidence, the window starts at t-tau and ends at t-tau-delT, for trigger coincidence, the window starts at t+tau and ends at t+tau+delT.
  TRUE: symmetrical tolerance window. The tolerance window is symmetrically placed around t-tau and t+tau, respectively. For precursor coincidence, the window starts at t-tau+delT and ends at t-tau-delT, for trigger coincidence the window starts at t+tau-delT and ends at t+tau+delT
 }
  \item{tau}{
Positive value [0 inf], default = 0. 
Time lag parameter tau allows for shifted events to be counted for coincidences (K). If e.g. tau=5, an event
in seriesA occurring exactly 5 (time) steps after an event in seriesB also counts for coincidence (K).
}
  \item{sigtest}{
    Character specifying the type of significance test, default = "poisson". 
    "poisson": significance test based on the calculation of the probability that the empirical coincidence rate would occur for two random (poisson-process) time series.
    "wt.surrogate": significance test based on the calculation of event coincidence analysis for a large number of surrogate time series having the same average waiting time between two events.
        "shuffle.surrogate": significance test based on the calculation of event coincidence analysis for a large number of randomly shuffled time series having the same number of events like the original time series.
}
  \item{reps}{
    Positive whole number [100, inf], default = "1000". 
    Number of surrogate/shuffled time series to be produced for the "surrogate" and "shuffle" significance test. 
}
}

\value{
## Output: list, containing seven elements ##
\item{NH precursor}{                 Logical, null hypothesis for precursor coincidence rate accepted}
\item{NH trigger}{                Logical, null hypothesis for trigger coincidence rate accepted}
\item{p-value precursor}{                    Numeric, p-value used for the precursor significance test}
\item{p-value trigger}{                   Numeric, p-value used for the trigger significance test}
\item{precursor coincidence rate}{Numeric, precursor coincidence rate}
\item{trigger coincidence rate}{  Numeric, precursor coincidence rate}

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

# Example: Lets imagine an artificial event series 'artA' of length 100 with 15 events:
library("CoinCalc")
span_artA=c(1,100)
artA=c(5,10,15,20,25,30,35,40,45,50,55,60,65,70,75)

# Additionally, we create an artificial event series 'artB' of length 100 with 7 events,
# each of them following two time steps after one of the artA events .
span_artB=c(1,100)
artB=c(12,22,32,42,52,62,72)

# Lets see if CC.eca.es fill find significant coincidences (of which we already know that they exist!).
# Note, that when executing CC.eca.es for these event series, we need to define delT>=1 in order to find
#  coincidences, since this is the minimum resolution of the given event series (0 digits). 
out <- CC.eca.es(artA,artB,span_artA,span_artB,tau=2,delT=1)
# out$test_prec
# --> [1] FALSE

# Surprise, surprise! CC.eca.es found significant non-random precursor coincidences between events 
# in these two time series.
}