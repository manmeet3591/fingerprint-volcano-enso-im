import numpy as np
ismr_phase = np.zeros((5001,12000))
nino3_phase = np.zeros((5001,12000))
delphi_phase = np.zeros((5001,12000))
for i in range(5001):
	ismr_phase[i,:] = np.genfromtxt('data_ipsl_pi/nino_phi'+str(i)+'.txt')
	nino3_phase[i,:] = np.genfromtxt('data_ipsl_pi/ismr_phi'+str(i)+'.txt')
	delphi_phase[i,:] = np.genfromtxt('data_ipsl_pi/del_phi'+str(i)+'.txt')
np.savetxt('ismr_phase_null.csv',ismr_phase, delimiter=",")
np.savetxt('nino_phase_null.csv',nino3_phase, delimiter=",")
np.savetxt('delphi_phase_null.csv',delphi_phase, delimiter=",")
