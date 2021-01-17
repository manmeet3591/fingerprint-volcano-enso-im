import numpy as np
from pyunicorn.timeseries.surrogates import Surrogates
ts = Surrogates.SmallTestData().original_data
#surrogates = Surrogates.SmallTestData().white_noise_surrogates(ts)
#print(surrogates)
#data = np.genfromtxt("pr_Amon_GISS-E2-R_past1000_r1i1p128_0850_1850_goswami_india_tseries.csv", delimiter=",", dtype=float).flatten()
#data_ = (data - np.mean(data))/(np.std(data))

#ts = data_[np.newaxis,:]
# Twin Surrogates
#  The algorithm proceeds in several steps:
#  1. Embed the original_data time series, using time delay embedding
#     for simplicity. Use the same dimension and time delay delay for
#     all time series for simplicity. Determine delay using time
#     delayed mutual information and dimension using false nearest neighbors
#     methods.
#  2. Use the algorithm proposed in [*] to find twins
#  Two state vectors are said to be twins if they share the same
#  recurrences, i.e., if the corresponding rows or columns in the
#  recurrence plot are identical.
# def twin_surrogates(self, original_data, dimension, delay, threshold, min_dist=7):

surrogates = Surrogates.SmallTestData().twin_surrogates(ts, dimension=1,delay=1,threshold=0.7,min_dist=7)
print(surrogates)
