\name{CC.es2ts}
%-------------------------------------------------------------------------------------------------
\alias{CC.es2ts}
\title{
Function: Transformation of an event series (es) to a event time series (ts)
}
\description{
This function transforms an event series vector in an event time series vector. The difference between both types:
Event time series: continuous binary vector with 0 denoting step without and 1 denoting a step with event.
Example: (0,0,0,0,1,0,0,1,0,0,0,1)
Event series: vector containing only the timings/steps of the events in the referring time series.
Example: (5,8,12)
}

\usage{
CC.es2ts(data,span,es.round=0)
}

\arguments{
  \item{data}{
Numeric vector. Event series to be transformed into event time series.
}
  \item{span}{
Numeric vector with two elements. span[1]: starting point of the data set, span[2]: end point of data set.
}
    \item{es.round}{ Integer [0 Inf]. Number of decimals for the rounding of the given values in data. es.round additionally defines the number of decimals of the sampling interval (e.g. es.round=3 leads to a sampling interval of 0.001).
    
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

# Example 1
library("CoinCalc")
data.es=c(1954,1963,1999)
span=c(1950,2000)
data.ts <- CC.es2ts(data.es,span)
data.ts
# 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0


}