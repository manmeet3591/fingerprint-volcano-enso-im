import numpy as np
import recurrence_v1
import utils
import sys

#IPSL
#data = np.genfromtxt('tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.csv', delimiter = ',').flatten()
#HADCM3
data = np.genfromtxt('tos_Omon_HadCM3_past1000_r1i1p1_085001-185012_nino3_tseries.csv', delimiter = ',').flatten()
#GISS
#data = np.genfromtxt('tos_Omon_GISS-E2-R_past1000_r1i1p128_0850_1850_nino3_tseries.csv', delimiter = ',').flatten()
i = sys.argv[1]

#IPSL
#surr = recurrence_v1.surrogates(data, ns=1, method='twins', m=50, tau=6, e=0.2, norm='euclidean', threshold_by='frr' , verbose=False)
#HADCM3
surr = recurrence_v1.surrogates(data, ns=1, method='twins', m=44, tau=9, e=0.2, norm='euclidean', threshold_by='frr' , verbose=False)
#GISS
#surr = recurrence_v1.surrogates(data, ns=1, method='twins', m=50, tau=6, e=0.2, norm='euclidean', threshold_by='frr' , verbose=False)

np.savetxt('tas_hadcm3'+str(i)+'.csv', surr, delimiter=",")
