library(dplR)
enso <- read.table("nature14565-s6_sigl2015_v2.csv", header = FALSE)
event.years_ <- as.vector(read.table("yy_strong_tropical.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_strong_nh.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_tropical.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_nh.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_sh.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_strong_tropical_after_en.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_strong_tropical_after_ln.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_strong_tropical_after_nt.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_tropical_after_en.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_tropical_after_ln.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_tropical_after_nt.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_strong_nh_after_en.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_strong_nh_after_ln.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_strong_nh_after_nt.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_nh_after_en.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_nh_after_ln.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_nh_after_nt.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_sh_after_en.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_sh_after_ln.txt", header=FALSE))
#event.years_ <- as.vector(read.table("yy_all_sh_after_nt.txt", header=FALSE))
rownames(enso) <- c(-140:2005) # Mann et al 2009
print(enso)


print(event.years_) # Strong SH after El Nino
#print(event.years_[1:52,]) # All NH after Neutral
#print(event.years_[1:23,]) # All NH after La Nina
#print(event.years_[1:19,]) # All NH after El Nino
#print(event.years_[1:1,]) # Strong NH after Neutral
#print(event.years_[1:3,]) # Strong NH after La Nina
#print(event.years_[1:4,]) # Strong NH after El Nino
#print(event.years_[1:33,]) # All Tropical after Neutral
#print(event.years_[1:10,]) # All Tropical after La Nina
#print(event.years_[1:14,]) # All Tropical after El Nino
#print(event.years_[1:16,]) # Strong Tropical after Neutral
#print(event.years_[1:9,]) # Strong Tropical after La Nina
#print(event.years_[1:8,]) # Strong Tropical after El Nino
#print(event.years_[1:37,]) # All SH
#print(event.years_[1:94,]) # All NH
#print(event.years_[1:51,]) # All Tropical
#print(event.years_[1:8,]) # Strong NH
print(event.years_[1:33,]) # Strong Tropical

event.years = event.years_[1:33,]


enso.sea <- sea(enso, event.years, lag=10, resample=10000)
enso.sea.unscaled <- enso.sea$se.unscaled
names(enso.sea.unscaled) <- enso.sea$lag


write.table(enso.sea.unscaled, file = "sea.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$lag, file = "lag.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.99.upper, file = "ci.99.upper.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.95.upper, file = "ci.95.upper.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.99.lower, file = "ci.99.lower.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.95.lower, file = "ci.95.lower.csv", row.names=FALSE, col.names=FALSE)

