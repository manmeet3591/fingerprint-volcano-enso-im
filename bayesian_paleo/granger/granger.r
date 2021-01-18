library("lmtest")

# Load Data
pdo_load <- read.csv(file="PDO_1900_2016.txt", header=FALSE, sep=",")
ismr_load <- read.csv(file="ismr.csv", header=FALSE, sep=",")
nino3_load <- read.csv(file="nino3_1900_2016.csv", header=FALSE, sep=",")

# Calculate difference
pdo <- unlist(pdo_load)
pdo_diff <- diff(pdo)
ismr <- unlist(ismr_load)
ismr_diff <- diff(ismr)
nino3 <- unlist(nino3_load)
nino3_diff <- diff(nino3)

## nino3 granger-cause ismr?
grangertest(ismr_diff ~ nino3_diff, order = 1)
grangertest(ismr_diff ~ nino3_diff, order = 2)
grangertest(ismr_diff ~ nino3_diff, order = 3)
grangertest(ismr_diff ~ nino3_diff, order = 4)

## ismr granger-cause nino3?
grangertest(nino3_diff ~ ismr_diff, order = 1)
grangertest(nino3_diff ~ ismr_diff, order = 2)
grangertest(nino3_diff ~ ismr_diff, order = 3)
grangertest(nino3_diff ~ ismr_diff, order = 4)


#print(length(nino3_diff))
#print(length(nino3))

#print(length(ismr_diff))
#print(length(ismr))
#print(length(pdo_diff))
#print(length(pdo))
#/iitm1/cccr/swapna/ALL_FORC/MON
