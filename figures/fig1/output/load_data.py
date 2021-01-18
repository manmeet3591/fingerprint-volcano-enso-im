import numpy as np
#delphi_null = np.zeros((5000,12012))
##is_plateau_null = np.zeros((5000,12012))
#for i in range(5000):
#    #is_plateau_null[i,:] = np.genfromtxt("event_synch/delphi_"+str(i)+".csv", delimiter=",")
#    delphi_null[i,:] = np.genfromtxt("event_synch/delphi_"+str(i)+".csv", delimiter=",")
#    #print("Reading ",i)
delphi_null_inst = np.genfromtxt("delphi_surr_inst.csv", delimiter=",").flatten()
delphi_hist_null = np.genfromtxt('delphi_phase_null.csv', delimiter=",", dtype=float).flatten()
#dvolc_source = np.genfromtxt('volc_source_850_1850.csv', delimiter=",", dtype=float).flatten()
