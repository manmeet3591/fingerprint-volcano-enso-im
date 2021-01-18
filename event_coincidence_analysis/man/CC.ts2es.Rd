\name{CC.ts2es}
%-------------------------------------------------------------------------------------------------
\alias{CC.ts2es}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
Function: Transformation of a event time series to a event series
}
\description{
This function transforms an event time series vector into a event series vector. The difference between both types:
Event time series: continuous binary vector with 0 denoting step without and 1 denoting a step with event.
Example: (0,0,0,0,1,0,0,1,0,0,0,1)
Event series: vector containing only the timings/steps of the events in the referring time series.
Example: (5,8,12)
}

\usage{
CC.ts2es(data)
}

\arguments{
  \item{data}{
Numeric vector. Binary continuous event time series to be transformed into event series.
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

# Example
library("CoinCalc")
data.ts=c(0,1,0,0,1,0,0,0,1,0,0,0)
data.es <- CC.ts2es(data.ts)
data.es
# data.es$es:   (2,5,9)
# data.es$span: (1,12)

}