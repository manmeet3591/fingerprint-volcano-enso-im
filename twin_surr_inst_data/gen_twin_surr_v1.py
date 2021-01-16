import numpy as np
from surrogates import Surrogates
import sys
data_ = np.genfromtxt('pr_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_goswami_india_tseries.csv', delimiter = ',').flatten()
i = sys.argv[1]
eps = np.std(data_)/(0.1*(data_.max() - data_.min()))
data = data_[np.newaxis,:]

surrogates = Surrogates.SmallTestData().twin_surrogates(data,dimension=48, delay=4,threshold=eps,min_dist=7)
#surr[i,:] = surrogates
#print("Surrogate ",i)	
#print(data, data.shape)
np.savetxt('pr_ipsl'+str(i)+'.csv', surrogates, delimiter=",") 
#print(eps)
