import numpy as np
n_surr = 5000
dummy = np.genfromtxt("nino3_0.csv", delimiter=',')
ismr_surr = np.zeros((n_surr, dummy.shape[0]))
nino3_surr = np.zeros((n_surr, dummy.shape[0]))
for i in range(n_surr):
	ismr_surr[i] = np.genfromtxt("pr_"+str(i)+".csv", delimiter=",")
	nino3_surr[i] = np.genfromtxt("nino3_"+str(i)+".csv", delimiter=",")
	print(i)
np.savetxt('ismr_surr.csv', ismr_surr, delimiter=",")
np.savetxt('nino3_surr.csv', nino3_surr, delimiter=",")
