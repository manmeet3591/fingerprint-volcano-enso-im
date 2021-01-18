# Example:
# First we load the two data sets April.Tmean.Niederrimbach and Lilac.Flowering.Niederrimbach, 
# supplied by CoinCalc
library(CoinCalc)
#data("CC.Example.Data1")
data_index_bin_ <- read.table("el_nino_kobb_2003.txt", header = FALSE)
#data_index_bin_ <- read.table("im_drought_sinha_2015.txt", header = FALSE)
#data_index_bin_ <- read.table("drought_sinha_2015.txt", header = FALSE)
#data_index_bin_ <- read.table("drought_cook_2010.txt", header = FALSE)
#data_index_bin_ <- read.table("el_nino_kobb_2003.txt", header = FALSE)
#data_index_bin_ <- read.table("el_nino_moy_2002.txt", header = FALSE)
#data_index_bin_ <- read.table("el_nino_li_2011.txt", header = FALSE)
#data_index_bin_ <- read.table("drought_ipsl.txt", header = FALSE)
#data_index_bin_ <- read.table("drought_giss.txt", header = FALSE)
#data_index_bin_ <- read.table("drought_mpi.txt", header = FALSE)
#data_index_bin_ <- read.table("drought_dandak_2010.txt", header = FALSE)

data_index_bin = t(data_index_bin_)

data_volc_bin_ <- read.table("all_volc_kobb_2003.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_dandak_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_dandak_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_dandak_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_dandak_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_dandak_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_dandak_2010.txt", header = FALSE)



#data_volc_bin_ <- read.table("all_volc_pmip.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_pmip.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_pmip.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_pmip.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_pmip.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_pmip.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_pmip.txt", header = FALSE)


#data_volc_bin_ <- read.table("all_volc.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh.txt", header = FALSE)

#data_volc_bin_ <- read.table("all_volc_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_sinha_2015.txt", header = FALSE)

#data_volc_bin_ <- read.table("all_volc_sinha_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_sinha_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_sinha_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_sinha_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_sinha_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_sinha_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_sinha_2011.txt", header = FALSE)

#data_volc_bin_ <- read.table("all_volc_cook_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_cook_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_cook_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_cook_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_cook_2010.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_sinha_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_cook_2010.txt", header = FALSE)


#data_volc_bin_ <- read.table("all_volc_kobb_2003.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_kobb_2003.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_kobb_2003.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_sinha_2015.txt", header = FALSE)

#data_volc_bin_ <- read.table("all_volc_moy_2002.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_moy_2002.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_moy_2002.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_moy_2002.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_moy_2002.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_moy_2002.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_sinha_2015.txt", header = FALSE)

#data_volc_bin_ <- read.table("all_volc_li_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_volc_li_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_tropical_li_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_tropical_li_2011.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_nh_sinha_2015.txt", header = FALSE)
#data_volc_bin_ <- read.table("strong_nh_moy_2002.txt", header = FALSE)
#data_volc_bin_ <- read.table("all_sh_sinha_2015.txt", header = FALSE)



data_volc_bin = t(data_volc_bin_)
# Then, we binarize both time series:
#Flow_bin=CC.binarize(CC.Example.Data1$DOY_Lilac_Flowering,ev.def="percentile",thres=0.1,event="lower")
#print(Flow_bin)
#Tmean_bin=CC.binarize(CC.Example.Data1$April_Tmean,ev.def="percentile",thres=0.9,event="higher")
#print(Tmean_bin)
yy = 10
prec_rate   <- array(0.0,dim=c(yy))
trig_rate   <- array(0.0,dim=c(yy))
p_prec_rate <- array(0.0,dim=c(yy))
p_trig_rate <- array(0.0,dim=c(yy))

for (i in 1:yy){
#out <- CC.eca.ts(Flow_bin,Tmean_bin,tau=0,delT=i,sigtest="shuffle.surrogate", reps=10000)
#out <- CC.eca.ts(data_index_bin, data_volc_bin,tau=0,delT=i,sigtest="shuffle.surrogate", reps=100)
out <- CC.eca.ts(data_index_bin, data_volc_bin,tau=0,delT=i,sigtest="shuffle.surrogate", reps=100)
p_prec= unname(unlist(out))[3]
p_trig= unname(unlist(out))[4]
prec_coin_r= unname(unlist(out))[5]
trig_coin_r= unname(unlist(out))[6]


prec_rate[i]   = prec_coin_r 
trig_rate[i]   = trig_coin_r
p_prec_rate[i] = p_prec
p_trig_rate[i] = p_trig

message(sprintf("Event Coincidence Analysis for %d years \n",i))
#message(sprintf("p-val precursor coin rate %f %f\n", p_prec, prec_rate[i]))
#message(sprintf("p-val trigger coin rate %f \n", p_trig))
#message(sprintf("precursor coin rate %f \n", prec_coin_r))
#message(sprintf("trigger coin rate %f \n", prec_coin_r))

}

write.table(prec_rate, file = "prec_rate.csv", row.names=FALSE, col.names=FALSE)
write.table(trig_rate, file = "trig_rate.csv", row.names=FALSE, col.names=FALSE)
write.table(p_prec_rate, file = "p_prec_rate.csv", row.names=FALSE, col.names=FALSE)
write.table(p_trig_rate, file = "p_trig_rate.csv", row.names=FALSE, col.names=FALSE)

# sigtest
# Character specifying the type of significance test, default = "poisson".
# "poisson": significance test based on the calculation of the probability that the empirical coincidence rate would occur for two random (poisson-process) time series.
# "wt.surrogate": significance test based on the calculation of event coincidence analysis for a large number of surrogate time series having the same average waiting time between two events.
# "shuffle.surrogate": significance test based on the calculation of event coincidence analysis for a large number of randomly shuffled time series having the same number of events like the original time series.


# output
# NH precursor, Logical, null hypothesis for precursor coincidence rate accepted
# NH trigger, Logical, null hypothesis for trigger coincidence rate accepted
# p-value precursor, Numeric, p-value used for the precursor significance test
# p-value trigger, Numeric, p-value used for the trigger significance test
# precursor coincidence rate, Numeric, precursor coincidence rate
# trigger coincidence rate, Numeric, precursor coincidence rate

# So the series A and B would be A - ENSO, B - Volcanic eruption and see the precursor coincidence rate
# and trigger coincidence rate
