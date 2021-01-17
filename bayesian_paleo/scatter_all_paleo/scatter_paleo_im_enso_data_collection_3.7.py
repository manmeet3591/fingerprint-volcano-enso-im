
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as pl


# In[2]:


# IM
data_sinha_2011 = np.genfromtxt("3.7_ismr_sinha_2011_anom_yy.txt", delimiter = ',')
data_sinha_2015 = np.genfromtxt("3.7_ismr_sinha_2015_anom_yy.txt", delimiter = ',')
data_jhumar_2011 = np.genfromtxt("3.7_ismr_jhumar_ann_yy.txt", delimiter = ',')
data_dandak_2010 = np.genfromtxt("3.7_ismr_dandak_2010_anom_yy.txt", delimiter = ',')
data_cook_2010 = np.genfromtxt("3.7_ismr_cook_anom_yy.txt", delimiter = ',')

# ENSO
data_moy_2002 = np.genfromtxt("3.7_nino3_moy_2002_anom_yy.txt", delimiter = ',')
data_mann_2009 = np.genfromtxt("3.7_nino3_mann_2009_anom_yy.txt", delimiter = ',')
data_li_2013 = np.genfromtxt("3.7_nino3_li_2013_anom_yy.txt", delimiter = ',')
data_li_2011 = np.genfromtxt("3.7_nino3_li_2011_anom_yy.txt", delimiter = ',')


# In[3]:


# IM

yy_sinha_2011 = data_sinha_2011[:,0]
volc_sinha_2011 = data_sinha_2011[:,1]
im_sinha_2011 = data_sinha_2011[:,2]

yy_sinha_2015 = data_sinha_2015[:,0]
volc_sinha_2015 = data_sinha_2015[:,1]
im_sinha_2015 = data_sinha_2015[:,2]

yy_jhumar_2011 = data_jhumar_2011[:,0]
volc_jhumar_2011 = data_jhumar_2011[:,1]
im_jhumar_2011 = data_jhumar_2011[:,2]

yy_dandak_2010 = data_dandak_2010[:,0]
volc_dandak_2010 = data_dandak_2010[:,1]
im_dandak_2010 = data_dandak_2010[:,2]

yy_cook_2010 = data_cook_2010[:,0]
volc_cook_2010 = data_cook_2010[:,1]
im_cook_2010 = data_cook_2010[:,2]

# ENSO

yy_moy_2002 = data_moy_2002[:,0]
volc_moy_2002 = data_moy_2002[:,1]
nino_moy_2002 = data_moy_2002[:,2]

yy_mann_2009 = data_mann_2009[:,0]
volc_mann_2009 = data_mann_2009[:,1]
nino_mann_2009 = data_mann_2009[:,2]

yy_li_2013 = data_li_2013[:,0]
volc_li_2013 = data_li_2013[:,1]
nino_li_2013 = data_li_2013[:,2]

yy_li_2011 = data_li_2011[:,0]
volc_li_2011 = data_li_2011[:,1]
nino_li_2011 = data_li_2011[:,2]


# In[59]:


x = []
y = []
x_volc = []
y_volc = []
win = 15
for i in range(yy_moy_2002.shape[0]):
    for j in range(yy_sinha_2011.shape[0]):
        if yy_moy_2002[i]==yy_sinha_2011[j]:
            if volc_moy_2002[i:].shape[0]>=win and  volc_sinha_2011[j:].shape[0]>=win:
            #print("first if working")
            
                if volc_moy_2002[i]==1.0 or volc_sinha_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_moy_2002[i:i+win])
                #print(x_volc)
                    y_volc.append(im_sinha_2011[j:j+win])
                else:
                    x.append(nino_moy_2002[i:i+win])
                    y.append(im_sinha_2011[j:j+win])
    #print(np.hstack(x).shape)
    #print(np.hstack(y).shape)
                
    for j in range(yy_sinha_2015.shape[0]):
        if yy_moy_2002[i]==yy_sinha_2015[j]:
            #print("first if working")
            if volc_moy_2002[i:].shape[0]>=win and  volc_sinha_2015[j:].shape[0]>=win:
                if volc_moy_2002[i]==1.0 or volc_sinha_2015[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_moy_2002[i:i+win])
                    y_volc.append(im_sinha_2015[j:j+win])
                else:
                    x.append(nino_moy_2002[i:i+win])
                    y.append(im_sinha_2015[j:j+win])
                
    for j in range(yy_jhumar_2011.shape[0]):
        if yy_moy_2002[i]==yy_jhumar_2011[j]:
            #print("first if working")
            if volc_moy_2002[i:].shape[0]>=win and  volc_jhumar_2011[j:].shape[0]>=win:
                if volc_moy_2002[i]==1.0 or volc_jhumar_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_moy_2002[i:i+win])
                    y_volc.append(im_jhumar_2011[j:j+win])
                else:
                    x.append(nino_moy_2002[i:i+win])
                    y.append(im_jhumar_2011[j:j+win])
                
    for j in range(yy_dandak_2010.shape[0]):
        if yy_moy_2002[i]==yy_dandak_2010[j]:
            #print("first if working")
            if volc_moy_2002[i:].shape[0]>=win and  volc_dandak_2010[j:].shape[0]>=win:
                if volc_moy_2002[i]==1.0 or volc_dandak_2010[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_moy_2002[i:i+win])
                    y_volc.append(im_dandak_2010[j:j+win])
                else:
                    x.append(nino_moy_2002[i:i+win])
                    y.append(im_dandak_2010[j:j+win])
                
    for j in range(yy_cook_2010.shape[0]):
        if yy_moy_2002[i]==yy_cook_2010[j]:
            #print("first if working")
            if volc_moy_2002[i:].shape[0]>=win and  volc_cook_2010[j:].shape[0]>=win:
                if volc_moy_2002[i]==1.0 or volc_cook_2010[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_moy_2002[i:i+win])
                    y_volc.append(im_cook_2010[j:j+win])
                else:
                    x.append(nino_moy_2002[i:i+win])
                    y.append(im_cook_2010[j:j+win])
print(np.hstack(x).shape)
print(np.hstack(y).shape)


# In[60]:



for i in range(yy_mann_2009.shape[0]):
    for j in range(yy_sinha_2011.shape[0]):
        if yy_mann_2009[i]==yy_sinha_2011[j]:
            #print("first if working")
            if volc_mann_2009[i:].shape[0]>=win and  volc_sinha_2011[j:].shape[0]>=win:
                if volc_mann_2009[i]==1.0 or volc_sinha_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_mann_2009[i:i+win])
                    y_volc.append(im_sinha_2011[j:j+win])
                else:
                    x.append(nino_mann_2009[i:i+win])
                    y.append(im_sinha_2011[j:j+win])
                
    for j in range(yy_sinha_2015.shape[0]):
        if yy_mann_2009[i]==yy_sinha_2015[j]:
            #print("first if working")
            if volc_mann_2009[i:].shape[0]>=win and  volc_sinha_2015[j:].shape[0]>=win:
                if volc_mann_2009[i]==1.0 or volc_sinha_2015[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_mann_2009[i:i+win])
                    y_volc.append(im_sinha_2015[j:j+win])
                else:
                    x.append(nino_mann_2009[i:i+win])
                    y.append(im_sinha_2015[j:j+win])
                
    for j in range(yy_jhumar_2011.shape[0]):
        if yy_mann_2009[i]==yy_jhumar_2011[j]:
            #print("first if working")
            if volc_mann_2009[i:].shape[0]>=win and  volc_jhumar_2011[j:].shape[0]>=win:
                if volc_mann_2009[i]==1.0 or volc_jhumar_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_mann_2009[i:i+win])
                    y_volc.append(im_jhumar_2011[j:j+win])
                else:
                    x.append(nino_mann_2009[i:i+win])
                    y.append(im_jhumar_2011[j:j+win])
                
    for j in range(yy_dandak_2010.shape[0]):
        if yy_mann_2009[i]==yy_dandak_2010[j]:
            #print("first if working")
            if volc_mann_2009[i:].shape[0]>=win and  volc_dandak_2010[j:].shape[0]>=win:
                if volc_mann_2009[i]==1.0 or volc_sinha_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_mann_2009[i:i+win])
                    y_volc.append(im_dandak_2010[j:j+win])
                else:
                    x.append(nino_mann_2009[i:i+win])
                    y.append(im_dandak_2010[j:j+win])
                
    for j in range(yy_cook_2010.shape[0]):
        if yy_mann_2009[i]==yy_cook_2010[j]:
            #print("first if working")
            if volc_mann_2009[i:].shape[0]>=win and  volc_cook_2010[j:].shape[0]>=win:
                if volc_mann_2009[i]==1.0 or volc_cook_2010[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_mann_2009[i:i+win])
                    y_volc.append(im_cook_2010[j:j+win])
                else:
                    x.append(nino_mann_2009[i:i+win])
                    y.append(im_cook_2010[j:j+win])
print(np.hstack(x).shape)
print(np.hstack(y).shape)


# In[61]:


for i in range(yy_li_2013.shape[0]):
    for j in range(yy_sinha_2011.shape[0]):
        if yy_li_2013[i]==yy_sinha_2011[j]:
            #print("first if working")
            if volc_li_2013[i:].shape[0]>=win and  volc_sinha_2011[j:].shape[0]>=win:
                if volc_li_2013[i]==1.0 or volc_sinha_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2013[i:i+win])
                    y_volc.append(im_sinha_2011[j:j+win])
                else:
                    x.append(nino_li_2013[i:i+win])
                    y.append(im_sinha_2011[j:j+win])
                
    for j in range(yy_sinha_2015.shape[0]):
        if yy_li_2013[i]==yy_sinha_2015[j]:
            #print("first if working")
            if volc_li_2013[i:].shape[0]>=win and  volc_sinha_2015[j:].shape[0]>=win:
                if volc_li_2013[i]==1.0 or volc_sinha_2015[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2013[i:i+win])
                    y_volc.append(im_sinha_2015[j:j+win])
                else:
                    x.append(nino_li_2013[i:i+win])
                    y.append(im_sinha_2015[j:j+win])
                
    for j in range(yy_li_2013.shape[0]):
        if yy_li_2013[i]==yy_jhumar_2011[j]:
            #print("first if working")
            if volc_li_2013[i:].shape[0]>=win and  volc_jhumar_2011[j:].shape[0]>=win:
                if volc_li_2013[i]==1.0 or volc_jhumar_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2013[i:i+win])
                    y_volc.append(im_jhumar_2011[j:j+win])
                else:
                    x.append(nino_li_2013[i:i+win])
                    y.append(im_jhumar_2011[j:j+win])
                
    for j in range(yy_dandak_2010.shape[0]):
        if yy_li_2013[i]==yy_dandak_2010[j]:
            #print("first if working")
            if volc_li_2013[i:].shape[0]>=win and  volc_dandak_2010[j:].shape[0]>=win:
                if volc_li_2013[i]==1.0 or volc_dandak_2010[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2013[i:i+win])
                    y_volc.append(im_dandak_2010[j:j+win])
                else:
                    x.append(nino_li_2013[i:i+win])
                    y.append(im_dandak_2010[j:j+win])
                
    for j in range(yy_cook_2010.shape[0]):
        if yy_li_2013[i]==yy_cook_2010[j]:
            #print("first if working")
            if volc_li_2013[i:].shape[0]>=win and  volc_cook_2010[j:].shape[0]>=win:
                if volc_li_2013[i]==1.0 or volc_cook_2010[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2013[i:i+win])
                    y_volc.append(im_cook_2010[j:j+win])
                else:
                    x.append(nino_li_2013[i:i+win])
                    y.append(im_cook_2010[j:j+win])
print(np.hstack(x).shape)
print(np.hstack(y).shape)


# In[62]:


for i in range(yy_li_2011.shape[0]):
    for j in range(yy_sinha_2011.shape[0]):
        if yy_li_2011[i]==yy_sinha_2011[j]:
            #print("first if working")
            if volc_li_2011[i:].shape[0]>=win and  volc_sinha_2011[j:].shape[0]>=win:
                if volc_li_2011[i]==1.0 or volc_sinha_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2011[i:i+win])
                    y_volc.append(im_sinha_2011[j:j+win])
                else:
                    x.append(nino_li_2011[i:i+win])
                    y.append(im_sinha_2011[j:j+win])
                
    for j in range(yy_sinha_2015.shape[0]):
        if yy_li_2011[i]==yy_sinha_2015[j]:
            #print("first if working")
            if volc_li_2011[i:].shape[0]>=win and  volc_sinha_2015[j:].shape[0]>=win:
                if volc_li_2011[i]==1.0 or volc_sinha_2015[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2011[i:i+win])
                    y_volc.append(im_sinha_2015[j:j+win])
                else:
                    x.append(nino_li_2011[i:i+win])
                    y.append(im_sinha_2015[j:j+win])
                
    for j in range(yy_li_2013.shape[0]):
        if yy_li_2011[i]==yy_jhumar_2011[j]:
            #print("first if working")
            if volc_li_2011[i:].shape[0]>=win and  volc_jhumar_2011[j:].shape[0]>=win:
                if volc_li_2011[i]==1.0 or volc_jhumar_2011[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2011[i:i+win])
                    y_volc.append(im_jhumar_2011[j:j+win])
                else:
                    x.append(nino_li_2011[i:i+win])
                    y.append(im_jhumar_2011[j:j+win])
                
    for j in range(yy_dandak_2010.shape[0]):
        if yy_li_2011[i]==yy_dandak_2010[j]:
            #print("first if working")
            if volc_li_2011[i:].shape[0]>=win and  volc_dandak_2010[j:].shape[0]>=win:
                if volc_li_2011[i]==1.0 or volc_dandak_2010[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2011[i:i+win])
                    y_volc.append(im_dandak_2010[j:j+win])
                else:
                    x.append(nino_li_2011[i:i+win])
                    y.append(im_dandak_2010[j:j+win])
                
    for j in range(yy_cook_2010.shape[0]):
        if yy_li_2011[i]==yy_cook_2010[j]:
            #print("first if working")
            if volc_li_2011[i:].shape[0]>=win and  volc_cook_2010[j:].shape[0]>=win:
                if volc_li_2011[i]==1.0 or volc_cook_2010[j]==1.0:
                #print("second if working")
                    x_volc.append(nino_li_2011[i:i+win])
                    y_volc.append(im_cook_2010[j:j+win])
                else:
                    x.append(nino_li_2011[i:i+win])
                    y.append(im_cook_2010[j:j+win])
                    
print(np.hstack(x).shape)
print(np.hstack(y).shape)


# In[63]:


x_ = np.hstack(x)
y_ = np.hstack(y)

x_volc_ = np.hstack(x_volc)
y_volc_ = np.hstack(y_volc)


# In[53]:


import seaborn as sns


# In[54]:


def _binwidth_fd(arr):
    """
    Returns bin width for given sample as per Freedman-Diaconis' rule.


    As per this rule, bin width h is defined as:
                    h = 2 (IQR) NS ^ (-1/3)
    References
    ----------
    https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule
    """
    n = float(len(arr))
    iqr = np.percentile(arr, 75.) - np.percentile(arr, 25.)
    return 2. * iqr * np.power(n, -1. / 3.)


# In[55]:


def joint_prob_den(s1, s2, xlab="Random variable 1", ylab="Random variable 2", tit="Random plot"):
        ## use numpy.histogram2d to get joint distributions
    ## ------------------------------------------------
    # bin widths
    h1 = _binwidth_fd(s1)
    h2 = _binwidth_fd(s2)
    # range of values
    m1, M1 = s1.min(), s1.max()
    m2, M2 = s2.min(), s2.max()
    # number of bins
    nb1 = (M1 - m1) / h1
    nb2 = (M2 - m2) / h2
    # histogram
    H, be1, be2 = np.histogram2d(x=s1, y=s2, bins=[nb1, nb2], normed=True)
    # bin centers
    bc1 = 0.5 * (be1[1:] + be1[:-1])
    bc2 = 0.5 * (be2[1:] + be2[:-1])

    ## plot the results
    # set up figure and axes
    fig = pl.figure(figsize=[10., 6.])      # 18 in x 6 in figure
    axlabfs = 14                            # axis label font size
    tiklabfs = 12                           # axis tick labels size
    # plot the 2D joint density stored in H as pcolormesh in axes ax2
    xx, yy = np.meshgrid(bc1, bc2)
    im = plt.pcolormesh(xx, yy, H.T, cmap=pl.cm.Blues)
    cb2 = plt.colorbar(im)

    ## prettify axes
    plt.xlabel(xlab, fontsize=axlabfs)
    plt.ylabel(ylab, fontsize=axlabfs)
    plt.title(tit)
    # tick labels
    plt.tick_params(labelsize=tiklabfs)
    cb2.set_label("Joint probability density", fontsize=axlabfs)
    plt.grid()
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axvline(0, color='k', linestyle='solid')
    plt.axhline(0, color='k', linestyle='solid')


# In[12]:


# 3.7 W/m2 threshold
joint_prob_den(s1=x_, s2=y_, xlab="Normalized Nino3", ylab="Normalized IM", tit="All years")
joint_prob_den(s1=x_volc_, s2=y_volc_, xlab="Normalized Nino3", ylab="Normalized IM", tit="10 years after volcanoes")


# In[21]:


# 3.7 W/m2 threshold
joint_prob_den(s1=x_, s2=y_, xlab="Normalized Nino3", ylab="Normalized IM", tit="All years")
joint_prob_den(s1=x_volc_, s2=y_volc_, xlab="Normalized Nino3", ylab="Normalized IM", tit="5 years after volcanoes")


# In[64]:


# 3.7 W/m2 threshold
joint_prob_den(s1=x_, s2=y_, xlab="Normalized Nino3", ylab="Normalized IM", tit="All years")
joint_prob_den(s1=x_volc_, s2=y_volc_, xlab="Normalized Nino3", ylab="Normalized IM", tit="15 years after volcanoes")

