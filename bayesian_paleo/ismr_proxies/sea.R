library(dplR)
#print("Test")
#print("Test")
#data(cana157)
#print(cana157)
#enso <- read.table("enso_900_2002_1.txt", header = TRUE)
enso <- read.table("sasmi_norm_900_2002.txt", header = TRUE)
#enso <- read.table("pdo_993_1996.txt", header = TRUE)
rownames(enso) <- c(900:2002)
#rownames(enso) <- c(993:1996)
#event.years <- c(5,9,3)
#print(enso[1:1103,1])
print(enso)
#print(900:1103)
#event.years <- c(1108, 1171, 1230, 1345, 1601, 1641, 1783, 1809, 1815, 1991, 1964, 1884, 1862, 1836, 1832, 1695, 1595, 1585, 1458, 1453, 1286, 1276, 1258, 1210, 1191, 1182, 1127, 1028, 1003, 976, 939, 916) # All volcanic events greater than 3.7 W/m2
# Tropical
event.years <- c(1108, 1171, 1230, 1345, 1601, 1641, 1809, 1815, 1991, 1964, 1884, 1862, 1836, 1832, 1695, 1595, 1585, 1458, 1453, 1286, 1276, 1258, 1191, 1127, 1028, 1003, 976, 939, 916) # All volcanic events greater than 3.7 W/m2
# NH
#event.years <- c(1783, 1210, 1182, 939) # All volcanic events greater than 3.7 W/m2
# SH
#event.years <- c(1809, 1815, 1991, 1964, 1884, 1862, 1836, 1832, 1695, 1595, 1585, 1458, 1453, 1286, 1276, 1258, 1210, 1191, 1182, 1127, 1028, 1003, 976, 939, 916) # All volcanic events greater than 3.7 W/m2


##event.years <- c(1108, 1171, 1230, 1345, 1601, 1641, 1783, 1809, 1815)
##event.years <- c(1108, 1171, 1230, 1345, 1601, 1641, 1783, 1809, 1815, 1258, 1458, 1695, 939, 1286)
#event.years <- c(1108, 1171, 1862, 1695, 1458, 1453, 1191) # Volcanic events post which La Nina like conditions evolved
#event.years <- c(1230, 1345, 1601, 1641, 1783, 1809, 1815, 1991, 1964, 1884, 1836, 1832, 1695, 1595, 1585, 1286, 1276, 1258, 1210, 1182, 1127, 1028, 1003, 976, 939, 916) # Volcanic events post which El Nino like conditions evolved
#print(event.years)
#event.years <- c(500,600)
enso.sea <- sea(enso, event.years, lag=15, resample=10000)
enso.sea.unscaled <- enso.sea$se.unscaled
names(enso.sea.unscaled) <- enso.sea$lag
#png(filename = "Rplot.png")
#barplot(enso.sea.unscaled, ylab = "ENSO", xlab = "Time since epoch")
#print(enso.sea$ci.99.upper)
#print(enso.sea$lag)
#par(new=TRUE)
#plot(enso.sea$lag, enso.sea$ci.99.upper, type="l")
write.table(enso.sea.unscaled, file = "sea.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$lag, file = "lag.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.99.upper, file = "ci.99.upper.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.95.upper, file = "ci.95.upper.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.99.lower, file = "ci.99.lower.csv", row.names=FALSE, col.names=FALSE)
write.table(enso.sea$ci.95.lower, file = "ci.95.lower.csv", row.names=FALSE, col.names=FALSE)
#abline(h=c(enso.sea$ci.99.upper,enso.sea$ci.95.upper), col=c("blue", "red"), lty=c(1,2), lwd=c(1, 1))
#par(new=TRUE)
#abline(h=enso.sea$ci.99.lower, lwd=1)
#par(new=TRUE)
#abline(h=enso.sea$ci.95.upper, lwd=2)
#par(new=TRUE)
#abline(h=enso.sea$ci.99.lower)
#barplot(enso.sea.unscaled, col = ifelse(enso.sea$p < 0.1, "grey30", "grey75"), ylab = "ENSO", xlab = "Time since epoch")



