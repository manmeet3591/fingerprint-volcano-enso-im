import numpy as np
from surrogates import Surrogates 
import sys

outname = sys.argv[1]
fdata = "tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.csv"
#fdata = "tos_Omon_GISS-E2-R_past1000_r1i1p128_0850_1850_nino3_tseries.csv"
#fdata = "pr_Amon_GISS-E2-R_past1000_r1i1p128_0850_1850_goswami_india_tseries.csv"
data_ = np.genfromtxt(fdata, delimiter=",", dtype=float).flatten()
data = (data_ - np.mean(data_))/(np.std(data_))
ts = data[np.newaxis,:]
#ts = Surrogates.SmallTestData().original_data
# tas IPSL
surr_ = Surrogates.SmallTestData().twin_surrogates(ts, dimension=12,delay=7,threshold=1.0,min_dist=7)
# tos GISS
#surr_ = Surrogates.SmallTestData().twin_surrogates(ts, dimension=17,delay=9,threshold=1.0,min_dist=7)
# pr GISS
#surr_ = Surrogates.SmallTestData().twin_surrogates(ts, dimension=30,delay=2,threshold=1.0,min_dist=7)
surr = (surr_ * np.std(data_))+np.mean(data_)
print(data_)
print(surr)
print(surr.shape)
np.savetxt(outname, surr, delimiter=",") 
