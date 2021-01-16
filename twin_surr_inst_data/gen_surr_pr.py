import numpy as np
import recurrence_v1
import utils
import sys
# IPSL
#data = np.genfromtxt('pr_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_goswami_india_tseries.csv', delimiter = ',').flatten()
#HADCM3
data = np.genfromtxt('ismr_1871_2016.csv', delimiter = ',').flatten()
#GISS
#data = np.genfromtxt('pr_Amon_GISS-E2-R_past1000_r1i1p128_0850_1850_goswami_india_tseries.csv', delimiter = ',').flatten()


i = sys.argv[1]
#IPSL
#surr = recurrence_v1.surrogates(data, ns=1, method='twins', m=48, tau=4, e=0.2, norm='euclidean', threshold_by='frr' , verbose=False)
#HADCM3
surr = recurrence_v1.surrogates(data, ns=1, method='twins', m=46, tau=34, e=0.2, norm='euclidean', threshold_by='frr' , verbose=False)
#GISS
##surr = recurrence_v1.surrogates(data, ns=1, method='twins', m=48, tau=4, e=0.2, norm='euclidean', threshold_by='frr' , verbose=False)

#np.savetxt('pr_ipsl'+str(i)+'.csv', surr, delimiter=",")
np.savetxt('pr_'+str(i)+'.csv', surr, delimiter=",")
