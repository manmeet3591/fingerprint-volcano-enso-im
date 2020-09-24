import numpy as np
delphi_null = np.zeros((5000,12012))
#is_plateau_null = np.zeros((5000,12012))
for i in range(5000):
    #is_plateau_null[i,:] = np.genfromtxt("event_synch/delphi_"+str(i)+".csv", delimiter=",")
    delphi_null[i,:] = np.genfromtxt("event_synch/delphi_"+str(i)+".csv", delimiter=",")
    #print("Reading ",i)
delphi_null_inst = np.genfromtxt("delphi_surr_inst.csv", delimiter=",").flatten()
