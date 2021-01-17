import numpy as np
N=5000
dummy = np.genfromtxt("delphi_ipsl_4726.csv", delimiter=",", dtype=float).flatten()
data = np.zeros((N,dummy.shape[0]))

for i in range(N):
	print("delphi_ipsl_"+str(i)+".csv")
	data[i,:] = np.genfromtxt("delphi_ipsl_"+str(i)+".csv", delimiter=",", dtype=float).flatten()
np.savetxt('delphi.csv', data, delimiter=",") 
#print(dummy.shape)
