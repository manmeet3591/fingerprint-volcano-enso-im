# ES estimates for the is_plateau of twin surrogates
from load_data import *
def zero_slope(data, chunksize =4, max_slope = .25):
    is_plateau = np.zeros((data.shape[0]))
    for index in range(0, len(data) - chunksize):
        chunk = data[index : index + chunksize]
        dy_dx =  abs(chunk[1:] - chunk[:-1]).sum()/chunksize
        if (0 <= dy_dx < max_slope):
            is_plateau[index] = 1.0
    return is_plateau

is_plateau_null = np.zeros((5000, is_plateau.shape[0]))


for i in range(5000):
    is_plateau_null[i,:] = zero_slope(delphi_null[i,:], chunksize = chunksize, max_slope = max_slope)
        for j in range(2,is_plateau.shape[0]-2):
            if (is_plateau_null[i,j-2]==is_plateau_null[i,j-1]==is_plateau_null[i,j+1]==is_plateau_null[i,j+2]):
                is_plateau_null[i,j] = is_plateau_null[i,j-1]
        np.savetxt('is_plateau_null_'+str(i)+'.csv', is_plateau_null[i,:], delimiter=',')   # X is an array

