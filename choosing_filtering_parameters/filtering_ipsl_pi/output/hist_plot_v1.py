
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random
import warnings

delphi = np.genfromtxt('delphi.csv', delimiter=",", dtype=float).flatten()
delphi_995p = np.genfromtxt('delphi_995p_pmip3_ipsl.csv', delimiter=",", dtype=float).flatten()
volc = -np.genfromtxt('sigl.txt', delimiter=",", dtype=float).flatten()
volc_source = np.genfromtxt('volc_source_850_1850.csv', delimiter=",", dtype=float).flatten()


# In[6]:


N=100000
win = 240 # window = 20 years
delphi_dist_1 = np.zeros((N,win))
delphi_995p_dist_1 = np.zeros((N,win))
volc_year = 0
i = 0
while i < N :
    rand_year = random.sample(range(0, delphi.shape[0]-win), 1)
    volc_year = int(np.round(rand_year[0]/12)) 
    if volc_source[volc_year] != 1.0 : # Tropical Eruptions only
        continue
    if volc[volc_year] < 3.7 : # Large Volcanic eruptions
        continue
    delphi_window = delphi[rand_year[0]:rand_year[0]+win]
    delphi_dist_1[i,:] = (delphi_window - np.min(delphi_window))
    i = i + 1

i = 0
while i < N :
    rand_year = random.sample(range(0, delphi.shape[0]-win), 1)
    delphi_995p_window = delphi_995p[rand_year[0]:rand_year[0]+win]
    delphi_995p_dist_1[i,:] = (delphi_995p_window - np.min(delphi_995p_window))
    i = i + 1
    
delphi_dist_2 = delphi_dist_1.flatten()
delphi_995p_dist_2 = delphi_995p_dist_1.flatten()

_, bins, _ = plt.hist(delphi_dist_2, bins=50, range=[0, 2], normed=True)
_ = plt.hist(delphi_995p_dist_2, bins=bins, alpha=0.5, normed=True)
plt.savefig('phase_diff_dist.png', format='png', dpi=1000)

