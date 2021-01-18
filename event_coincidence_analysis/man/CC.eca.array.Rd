\name{CC.eca.array}
\alias{CC.eca.array}

\title{
Function: Event coincidence analysis for two binarized arrays
}
\description{
Performs event coincidence analysis on two binarized arrays of identical size, stepwise per pixel along time dimension t. The output is a matrix or array of the same x,y dimensions as the input, containing one (matrix) or more (array) of the 6 list outputs of CC.eca.ts (NH precursor, NH trigger, p-value precursor, p-value trigger, precursor coincidence rate or trigger coincidence rate). Information for the coincidence rates is only stored for significant values, all other values are transformed into NA.
}
\usage{
CC.eca.array(arrayA,arrayB,dimsA=c("x","y","t"), dimsB=c("x","y","t"),
alpha=0.05,delT=0,sym=FALSE,tau=0,
sigtest="poisson",reps=1000,output=5,verbose=1)}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{arrayA}{data set to be used for ECA. Three-dimensional binary array of any size.}
  \item{arrayB}{data set to be used for ECA. Three-dimensional binary array of any size.}
 \item{dimsA}{Vector of length 3, default=c("x","y","t").
Defines the position of x, y and t (time) dimensions in arrayA.}
  \item{dimsB}{Vector of length 3, default=c("x","y","t").
Defines the position of x, y and t (time) dimensions in arrayB.}
  \item{alpha}{Value between [0 1], default=0.05. 
The significance level 'alpha' of the significance test. Null hypothesis: The found coincidence rates result from randomly, independently distributed event time series.}
  \item{delT}{
Positive value [1 inf], default = 1. 
Tolerance window delta T. delT describes the temporal tolerance window in which coincidences may occur. 
If e.g. delT=3, an event in seriesA occurring simultaneously or one, two or three time steps after an event in seriesB also counts for a coincidence (K). With delT=0 only simultaneous events are counted for coincidences, for e.g. delT=1 the tolerance window is extended by one time step. }
  \item{sym}{
TRUE or FALSE, default = FALSE.
  FALSE: non-symmetrically tolerance window. In case of the precursor coincidence, the window starts at t-tau and ends at t-tau-delT, for trigger coincidence, the window starts at t+tau and ends at t+tau+delT.
  TRUE: symmetrical tolerance window. The tolerance window is symmetrically placed around t-tau and t+tau, respectively. For precursor coincidence, the window starts at t-tau+delT and ends at t-tau-delT, for trigger coincidence the window starts at t+tau-delT and ends at t+tau+delT
 }
  \item{tau}{
Positive value [0 inf], default = 0. 
Time lag parameter tau allows for shifted events to be counted for coincidences (K). If e.g. tau=5, an event
in seriesA occurring exactly 5 time steps after an event in seriesB also counts for coincidence (K).
}
  \item{sigtest}{
Character specifying the type of significance test, default = "poisson". 
    "poisson": significance test based on the calculation of the probability that the empirical coincidence rate would occur for two random (poisson-process) time series.
    "surrogate": significance test based on the calculation of event coincidence analysis for a large number of surrogate time series having the same average waiting time between two events.
    "shuffle": significance test based on the calculation of event coincidence analysis for a large number of randomly shuffled time series having the same number of events like the original time series.
}
  \item{reps}{
Positive whole number [100, inf], default = "1000". 
Number of surrogate/shuffled time series to be produced for the "surrogate" or "shuffle" significance test. 
}
  \item{output}{Vector of length 1 to 6. Desired output parameter(s) of the event coincidence analysis, default = 5 ('precursor coincidence rate').
Can be one or more of the following: 
1 = 'NH precursor', 
2 = 'NH trigger',
3 = 'p-value precursor', 
4 = 'p-value trigger', 
5 = 'precursor coincidence rate',
6 = 'trigger coincidence rate'. 

If more than one output is given (e.g. by c(5,6)), the arrangement of the output array's third dimension is according to the arrangement of the values given in 'output'.}
  \item{verbose}{1 or 2., default = 1. If 1, no progrss information is printed while running CC.eca.array. If verbose=2, and length(output)>1 the calculation progress of CC.eca.array is printed. 
}
}

\author{
Lukas Baumbach, Jonatan Siegmund, Potsdam Institute for Climate Impact Research
}

\examples{
# Fist load the example data set 3
#data(CC.Example.Data3)
# Then binarize both data sets:
#LST.bin=CC.bin.array(CC.Example.Data3$LST,dims=c("x","y","t"),
#   ev.def = "percentile",thres = 0.9,event = "higher")
#NDVI.bin=CC.bin.array(CC.Example.Data3$NDVI,dims=c("x","y","t"),
#   ev.def = "percentile",thres = 0.1,event = "lower")
# Then perfrom ECA for these two binary event time series arrays
#out=CC.eca.array(LST.bin,NDVI.bin,verbose=2,output=c(5,6))
# out is an array dim=c(131,131,2). 131x131 pixel and the two output
#  variables "precursor coincidence rate", "trigger coincidence rate"
}

