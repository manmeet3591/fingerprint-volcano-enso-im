import numpy
import datetime as dt
import spacepy.seapy as sea
import spacepy.omni as om
import spacepy.toolbox as tb
import spacepy.time as spt
import sys
from dateutil.relativedelta import relativedelta
from monthdelta import monthdelta
# now read the epochs for the analysis (the path specified is the default
# install location on linux, different OS will have this elsewhere)
sasmi = numpy.loadtxt('sasmi_norm_900_2002.txt')
#sasmi = numpy.loadtxt('enso_900_2002_1.txt')
#sasmi = numpy.loadtxt('pdo_993_1996.txt')
epochs = sea.readepochs('/iitm2/cccr-res/msingh/pmip_data_scripts/agu_volcano/paleo_analysis/composite/Superposed_Epoch_Analysis/SEA_epochs.txt')
dates  = []
date_year = dt.datetime(900, 6, 15, 0, 0)
dates.append(date_year)
for n in range(1,1103):
#for n in range(1,1004):
	#date_year.replace(year = date_year.year + n)
	#print(date_year + relativedelta(years=n) )
	#date_year += dt.timedelta(years=1)
	dates.append(date_year + relativedelta(years=n))  
#print(sasmi)
#print(dates)
#print(epochs)
#sys.exit()
#print("epochs = ",epochs)
#ticks = spt.tickrange(dt.datetime(2005,1,1), dt.datetime(2009,1,1), dt.timedelta(hours=1))
#print("ticks = ",ticks)
#omni1hr = om.get_omni(ticks)
#omni1hr.tree(levels=1, verbose=True)
delta = 1
window= 15

#print(delta)
#print(window)
#sys.exit()
#print("velocity = ", omni1hr['velo'])
#print("date= ", omni1hr['UTC'])
sevx = sea.Sea(sasmi, dates, epochs, window, delta)
#rather than quartiles, we calculate the 95% confidence interval on the median
seamean = sevx.sea(ci=85, ci_quan='mean')
print(seamean)
#sevx.sea(ci=True)
sevx.plot()


