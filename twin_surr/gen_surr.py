import numpy as np
from surrogates import Surrogates 
fdata = "pr_Amon_GISS-E2-R_past1000_r1i1p128_0850_1850_goswami_india_tseries.csv"
data_ = np.genfromtxt(fdata, delimiter=",", dtype=float).flatten()
data = (data_ - np.mean(data_))/(np.std(data_))
ts = data[np.newaxis,:]
#ts = Surrogates.SmallTestData().original_data
N = 2
surrogates = np.zeros((N, ts.shape[1]))
for i in range(N):
    print("Surrogate number ",i)
    # pr GISS
    surr_ = Surrogates.SmallTestData().twin_surrogates(ts, dimension=30,delay=2,threshold=1.0,min_dist=7)
    surr = (surr_ * np.std(data_))+np.mean(data_)
    surrogates[i,:] = surr[0,:]
    print(data_)
    print(surr)
    print(surr.shape)
