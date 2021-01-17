import numpy as np
ismr_phase = np.zeros((5001,12012))
nino3_phase = np.zeros((5001,12012))
delphi_phase = np.zeros((5001,12012))
for i in range(5001):
	ismr_phase[i,:] = np.genfromtxt('data_ipsl/nino_phi'+str(i)+'.txt')
	nino3_phase[i,:] = np.genfromtxt('data_ipsl/ismr_phi'+str(i)+'.txt')
	delphi_phase[i,:] = np.genfromtxt('data_ipsl/del_phi'+str(i)+'.txt')
np.savetxt('ismr_phase_null.csv',ismr_phase, delimiter=",")
np.savetxt('nino_phase_null.csv',nino3_phase, delimiter=",")
np.savetxt('delphi_phase_null.csv',delphi_phase, delimiter=",")
