# Autor: Lukas Baumbach, Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.eca.array performs event coincidence analysis on two binarized arrays.

CC.eca.array <- function(arrayA,arrayB,dimsA=c("x","y","t"), dimsB=c("x","y","t"),alpha=0.05,delT=0,sym=FALSE,tau=0,sigtest="poisson",reps=1000,output=5,verbose=1){
  

  
# ----------------------------------------------- TEST FOR ERRORS IN FUNCTION CALL  ------------------------------------------------------------------------------  

 
  # ---- #1: delT or tau negative
  if(tau<0 || delT<0){
    print("|-------------    ERROR #1    -------------|")
    print("|    The offset (tau) or delta T (delT)    |")
    print("|              is negative.                |") 
    print("|------------------------------------------|")
    return()}
 
  # ---- #2: arrayA or arrayB is not an array
  if(!is.array(arrayA)){
    print("|-------------    ERROR #2a   -------------|")
    print("|           arrA is not an array.          |")
    print("|------------------------------------------|")
    return()} 
  if(!is.array(arrayB)){
    print("|-------------    ERROR #2b   -------------|")
    print("|           arrayB is not an array.          |")
    print("|------------------------------------------|")
    return()} 
  
  # ---- #3: binA or binB is not binary
  if(length(levels(factor(arrayA)))>2){
    print("|-------------    ERROR #3a   -------------|")
    print("|            arrayA is not binary            |")
    print("|      (or the number of events=0)!        |") 
    print("|  Use CC.bin.array() to preprocess arrayA   |")
    print("|------------------------------------------|")
    return()}
  if(length(levels(factor(arrayB)))>2){  
    print("|-------------    ERROR #3b   -------------|")
    print("|             arrayB is not binary           |")
    print("|      (or the number of events=0)!        |") 
    print("|  Use CC.bin.array() to preprocess arrayB   |")
    print("|------------------------------------------|")
    return()}  
  
  
# rearrange dimensions into sequence x,y,t
rearrA=aperm(arrayA,c(c(1:3)[dimsA=="x"],c(1:3)[dimsA=="y"],c(1:3)[dimsA=="t"])) 
rearrB=aperm(arrayB,c(c(1:3)[dimsB=="x"],c(1:3)[dimsB=="y"],c(1:3)[dimsB=="t"]))
  
  
  
   # ---- #4: lengths of rearrA and rearrB differ
  if(length(rearrA[,1,1])!=length(rearrB[,1,1])){
    print("|-------------    ERROR #4a   -------------|")
    print("|            x dimensions differ.          |")
    print("|------------------------------------------|")
    return()} 
  if(length(rearrA[1,,1])!=length(rearrB[1,,1])){
    print("|-------------    ERROR #4b   -------------|")
    print("|           y dimensions differ.           |")
    print("|------------------------------------------|")
    return()}   
  if(length(rearrA[1,1,])!=length(rearrB[1,1,])){
    print("|-------------    ERROR #4c   -------------|")
    print("|         time dimensions differ.          |")
    print("|------------------------------------------|")
    return()} 
  

  

  
  
# ----------------------------------------------- COINCIDENCE ANALYSIS  ------------------------------------------------------------------------------ 

    
count <- length(output)  
  itcount=0
if(count == 1){
    # transfrom array input to matrix
    matarrA <- matrix(rearrA,ncol=length(rearrA[1,1,]))
    matarrB <- matrix(rearrB,ncol=length(rearrB[1,1,]))
    # write rows as lists (quasi vector)
    split_binA <- split(matarrA,row(matarrA))
    split_binB <- split(matarrB,row(matarrB))
  # write function for mapply
  CC.eca.ts.tmp<-function(x,y){
    tmp <- CC.eca.ts(x,y,alpha,delT,sym,tau,sigtest,reps)
    return(tmp[[output]])
  } # end CC function
  # apply ECA
    coinlist <- mapply(CC.eca.ts.tmp,split_binA,split_binB)
  # transform back into a matrix of same size as arrayA
    result <- matrix(coinlist, ncol=length(rearrA[1,,1]))
    #result <- apply(t(coinmat), 2, rev)
} # end if count == 1  
else{
    # count number of calculations    
    if(verbose==2){itmax=dim(rearrA)[1]*dim(rearrA)[2]
    printpoints=seq(1000,itmax,1000)}
    
  result <- array(NA,dim=c(dim(rearrA)[1],dim(rearrA)[2],count))
    for (i in 1:dim(rearrA)[1]){
      for (j in 1:dim(rearrA)[2]){
        tmp <- CC.eca.ts(rearrA[i,j,],rearrB[i,j,],alpha,delT,sym,tau,sigtest,reps)
          for (o in 1:count){
          result[i,j,o] <- tmp[[output[o]]]
          } # end o
        if(verbose==2){
            
        # print function progress
        itcount=itcount+1;
        if(is.element(itcount,printpoints)){
        print(paste0("Done gridpoint ", itcount," of ",itmax))}}
        
      } # end j
    } # end i
} # end else

return(result)

} # end of document  
