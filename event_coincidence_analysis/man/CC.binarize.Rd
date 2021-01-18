\name{CC.binarize}
%-------------------------------------------------------------------------------------------------
\alias{CC.binarize}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
Function: Binarization of a numeric vector using a certain threshold
}
\description{
This function binarizes a numeric vector (e.g. a time series) using a given threshold. This threshold can either be a percentile or an absolute value.

}
\usage{
CC.binarize(data, ev.def="percentile", thres=0.90, event="higher")
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{data}{
Numeric vector. Vector to be binarized.
}
  \item{ev.def}{
Character string, default: "percentile". Specifies how an event is to defined. 
If "percentile": events are defined using given "thres" as percentile threshold.
If "absolute": events are defined using given "thres" as absolute value threshold.
}
  \item{thres}{
  If ev.def="percentile":
Number between [0 1]. Percentile to be used for threshold definition.
  If ev.def="absolute":
Number between [-Inf Inf]. Absolute value to be used for threshold definition.
}
  \item{event}{
Character string, default: "higher"
If "higher": values higher than the given "thres" are to be set as event.
If "lower": values lower than the given "thres" are to be set as event.
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
# Load April temperature data set for the phenological station of Niederrimbach (supplied by Coincalc)
library("CoinCalc")
data("CC.Example.Data1")
# Binarize the temperature time series, for values > the 10th percentile are transformed to 0, 
# and values < to 1, and store in Tmean_bin
Tmean_bin <- CC.binarize(CC.Example.Data1$April.Tmean,ev.def="percentile",thres=0.1,event="lower")


}