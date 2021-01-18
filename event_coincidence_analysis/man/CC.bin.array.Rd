\name{CC.bin.array}
%-------------------------------------------------------------------------------------------------
\alias{CC.bin.array}

\title{
Function: Binarization of time series stored in an array
}
\description{
This function binarizes a three-dimensional array into binary (event=1 , no event=0) format. The binarization is performed along tine time axis for each pixel seperatly.
}

\usage{
CC.bin.array(data,dims=c("x","y","t"), ev.def="percentile",thres=0.90,event="higher")
}

\arguments{
   \item{data}{Array to be binarized. Three-dimensional numeric array of any size. 
}

   \item{dims}{Character vector of length 3, default=c("x","y","t").
Defines the position of x, y and t (time) dimensions within the given array. The binarization is performend according to the time timension t.
}

  \item{ev.def}{
Character string, default = "percentile". Specifies how an event is to defined. 
If "percentile": events are defined using given "thres" as percentile threshold.
If "absolute": events are defined using given "thres" as absolute value threshold.
}

  \item{thres}{
Threshold value, default = 0.90.
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

\author{
Lukas Baumbach and Jonatan Siegmund, Potsdam Institut for Climate Impact Research}

\examples{
# Load the example dataset
# data(CC.Example.Data3)
# This list contains contains two arrays. Bost of dimension (131,131,96) hold MODIS 
# measurements for Land Surface Temperature and NDVI for the region of 
# Italy from 2000-2015. 14 days-resolution for July-September.
# Binarize each pixel according to its 10th percentile of the time series:
# CC.bin.array(CC.Example.Data3$LST,dims=c("x","y","t"),ev.def = "percentile",
#                       thres = 0.1,event = "lower")
# The resulting array now holds 96 maps, indicating values lower than the 10th 
# percentile of each pixel by 1, others by 0.
}

