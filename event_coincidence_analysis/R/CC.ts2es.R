# Autor: Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.ts2es can be used to reformat an event time series (containing only the "dates" of the events) to a binary continuous time series (containing 0s ans 1s). 


CC.ts2es <-function(data){ 
    # ----------------------------------------------- TEST FOR ERRORS IN FUNCTION CALL  ------------------------------------------------------------------------------  
    # ---- #1: Time series not binary 
    if(!is.vector(data) && !is.matrix(data)){
        print("|-------------    ERROR #1    -------------|")
        print("|     given 'data' is neither a vector     |")
        print("|               nor a matrix               |")        
        print("|------------------------------------------|")
        return()}
    # ---- #2: NAs found
    if(any(is.na(data))){
        print("|-------------    ERROR #2    --------------|")
        print("| data contains NAs. Vectors with missing   |")
        print("| values cannot be transformed to ts format.|")        
        print("|-------------------------------------------|")
        return()}
    # ----------------------------------------------- ts2es  ------------------------------------------------------------------------------  
    
    if(is.vector(data)){       
        # get starting point    
        for(i in 1:length(data)){if(!is.na(data[i])){span=i;break}} 
        # get end point
        for(j in length(data):1){if(!is.na(data[j])){span[2]=j;break}}
        numbers=seq(1:length(data))
        data_out=numbers[data==1 & !is.na(data)]} # end if is.vector
        
    if(is.matrix(data)){       
        # get starting point    
        for(i in 1:length(data[1,])){if(!is.na(data[1,i])){span=as.numeric(colnames(data)[i]);break}} 
        # get end point
        for(j in length(data[1,]):1){if(!is.na(data[1,j])){span[2]=as.numeric(colnames(data)[j]);break}}
        data_out=as.numeric(colnames(data)[data[1,]==1 & !is.na(data[1,])])} # end if is.matrix    
        
    out=list(data_out,span)
    names(out)=c("es","span")
    return(out)
    
    } # end function CC.ts2es
    