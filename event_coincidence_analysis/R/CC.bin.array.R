# Autor: Lukas Baumbach, Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.bin.array binarizes an array.

CC.bin.array <- function(data,dims=c("x","y","t"),ev.def="percentile",thres=0.90,event="higher"){
  

  
# ----------------------------------------------- TEST FOR ERRORS IN FUNCTION CALL  ------------------------------------------------------------------------------  

  
  # ---- #1: data is not an array
  if(!is.array(data)){
    print("|-------------    ERROR #    -------------|")
    print("|          data  is not an array.           |")
    print("|------------------------------------------|")
    return()} 
 

# rearrange dimensions into sequence x,y,t
  
rearr=aperm(data,c(c(1:3)[dims=="x"],c(1:3)[dims=="y"],c(1:3)[dims=="t"])) 


# ----------------------------------------------- BINARIZE  ------------------------------------------------------------------------------ 

# transform to matrix with columns as time steps
matarr <- matrix(rearr,ncol=length(rearr[1,1,]))

# binarize using CC.binarize (ev.def, thres and event arguments adjustable)
# transpose afterwards
bin_data <- apply(matarr,1,FUN=CC.binarize,ev.def,thres,event)
dim(bin_data)=dim(rearr)[c(3,1,2)]
bin_data=aperm(bin_data,c(2,3,1))
return(bin_data)

} # end of document  





