#\name{CC.eca.ts}
#%-------------------------------------------------------------------------------------------------
#\alias{CC.eca.ts}
#%- Also NEED an '\alias' for EACH other topic documented here.
#\title{
#Function: Event Coincidence Analysis for two time series 
#}
#\description{
#This function performs the event coincidence analysis using two data sets of event time series format (ts). NAs are allowed.
#}
#\usage{
#CC.eca.ts(seriesA, seriesB, alpha=0.05, delT=0, sym=FALSE, tau=0, sigtest="poisson", reps=1000)
#}
#%- maybe also 'usage' for other objects documented here.
#\arguments{
#  \item{seriesA}{
#Time series A. Numeric vector or one-row-matrix containing a time series of binary data (0,1) with all time steps of interest, where a '1' denotes a time step with, and a '0' a time step without event.
#SeriesA and seriesB need to be of same length. Both may contain missing values.
#}
#  \item{seriesB}{
#Time series B. Numeric vector or one-row-matrix containing a time series of binary data (0,1) with all time steps of interest, where a '1' denotes a time step with, and a '0' a time step without event.
#SeriesA and seriesB need to be of same length. Both may contain missing values.
#}
#  \item{alpha}{
#Value between [0 1], default=0.05. 
#The significance level 'alpha' of the significance test. null hypothesis: The found coincidence rates result from randomly, independently distributed event time series.
#}
#  \item{delT}{
#Positive value [1 inf], default = 1. 
#Tolerance window delta T. delT describes the temporal tolerance window in which coincidences may occur. 
#If e.g. delT=3, an event in seriesA occurring simultaneously or one, two or three time steps after an event in seriesB
#also counts for a coincidence (K). With delT=0 only simultaneous events are counted for coincidences, for e.g. delT=1 the tolerance window is extended by one time step. 
#}
#  \item{sym}{
#  TRUE or FALSE, default = FALSE.
#  FALSE: non-symmetrically tolerance window. In case of the precursor coincidence, the window starts at t-tau and ends at t-tau-delT, for trigger coincidence, the window starts at t+tau and ends at t+tau+delT.
#  TRUE: symmetrical tolerance window. The tolerance window is symmetrically placed around t-tau and t+tau, respectively. For precursor coincidence, the window starts at t-tau+delT and ends at t-tau-delT, for trigger coincidence the window starts at t+tau-delT and ends at t+tau+delT
# }
#  \item{tau}{
#Positive value [0 inf], default = 0. 
#Time lag parameter tau allows for shifted events to be counted for coincidences (K). If e.g. tau=5, an event
#in seriesA occurring exactly 5 time steps after an event in seriesB also counts for coincidence (K).
#}
#  \item{sigtest}{
#    Character specifying the type of significance test, default = "poisson". 
#    "poisson": significance test based on the calculation of the probability that the empirical coincidence rate would occur for two random (poisson-process) time series.
#    "wt.surrogate": significance test based on the calculation of event coincidence analysis for a large number of surrogate time series having the same average waiting time between two events.
#    "shuffle.surrogate": significance test based on the calculation of event coincidence analysis for a large number of randomly shuffled time series having the same number of events like the original time series.
#}
#  \item{reps}{
#    Positive whole number [100, inf], default = "1000". 
#    Number of surrogate/shuffled time series to be produced for the "surrogate" or "shuffle" significance test. 
#}
#}
#
#\value{
### Output: list, containing seven elements ##
#\item{NH precursor}{                 Logical, null hypothesis for precursor coincidence rate accepted}
#\item{NH trigger}{                Logical, null hypothesis for trigger coincidence rate accepted}
#\item{p-value precursor}{                    Numeric, p-value used for the precursor significance test}
#\item{p-value trigger}{                   Numeric, p-value used for the trigger significance test}
#\item{precursor coincidence rate}{Numeric, precursor coincidence rate}
#\item{trigger coincidence rate}{  Numeric, precursor coincidence rate}
#
#}
#\references{
#Siegmund, J., Seigmund, N. and Donner, R. (2015): CoinCalc - An R package for quantifying simultaneities 
#of events in two event (time) series. Submitted to Computers and Geosciences.
#Donges, J. F., Schleussner, C. F., Siegmund, J. F., and Donner, R. V. (2015): Coincidence analysis
#for quantifying statistical interrelationships between event time series, arXiv:1508.03534.
#}
#\author{
#Jonatan Siegmund, Potsdam Institute for Climate Impact Research
#}
#
#
#\examples{

# Example:
# First we load the two data sets April.Tmean.Niederrimbach and Lilac.Flowering.Niederrimbach, 
# supplied by CoinCalc
library(CoinCalc)
data("CC.Example.Data1")
# Then, we binarize both time series:


Flow_bin=CC.binarize(CC.Example.Data1$DOY_Lilac_Flowering,ev.def="percentile",thres=0.1,event="lower")
Tmean_bin=CC.binarize(CC.Example.Data1$April_Tmean,ev.def="percentile",thres=0.9,event="higher")

print(Tmean_bin)
p_prec = c(0:5)
p_trig = c(0:5)
prec_rate = c(0:5)
trig_rate = c(0:5)

for (i in 0:5){
    out <- CC.eca.ts(Flow_bin,Tmean_bin,tau=0,delT=i,sigtest="shuffle.surrogate")
    p_prec_ = unlist(unname(out))[3]
    p_trig_ = unlist(unname(out))[4]
    prec_rate_ = unlist(unname(out))[5]
    trig_rate_ = unlist(unname(out))[6]
    #print(trig_rate_)
    p_prec[i+1] = p_prec_
    p_trig[i+1] = p_trig_
    prec_rate[i+1] = prec_rate_
    trig_rate[i+1] = trig_rate_
    #print(i)
}
write.table(p_prec, file = "p_prec.csv", row.names=FALSE, col.names=FALSE)
write.table(p_trig, file = "p_trig.csv", row.names=FALSE, col.names=FALSE)
write.table(prec_rate, file = "prec_rate.csv", row.names=FALSE, col.names=FALSE)
write.table(trig_rate, file = "trig_rate.csv", row.names=FALSE, col.names=FALSE)

#print(trig_rate)
# Result: there are significant percursor and trigger coincidence rates for early 
# flowering and high April temperatures.

#}
