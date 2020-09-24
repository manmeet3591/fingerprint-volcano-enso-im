import numpy as np
def zero_slope(data, chunksize =4, max_slope = .25):
    is_plateau = np.zeros((data.shape[0]))
    for index in range(0, len(data) - chunksize):
        chunk = data[index : index + chunksize]
        dy_dx =  abs(chunk[1:] - chunk[:-1]).sum()/chunksize
        if (0 <= dy_dx < max_slope):
            is_plateau[index] = 1.0
    return is_plateau
