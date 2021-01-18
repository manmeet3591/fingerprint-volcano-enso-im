# Autor: Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.es2ts can be used to reformat a binary continuous time series (containing 0s ans 1s) to an event time series (containing only the "dates" of the events). 

CC.es2ts <-function(data,span,es.round=0){ 
    # ----------------------------------------------- TEST FOR ERRORS IN FUNCTION CALL  ---------------------------------------------------
    # ---- #1: Time series not binary 
    if(!is.vector(data)){
        print("|-------------    ERROR #1    -------------|")
        print("|     given 'data' is not a vector         |")
        print("|------------------------------------------|")
        return()}
    # ----------------------------------------------- ts2es  ------------------------------------------------------------------------------  
    
    data_out=rep(0,(length(span[1]:span[2])/(10**-es.round)))
    for(i in 1:length(data)){ 
        tmp=as.numeric(data[i])
        tmp=round(tmp,es.round)
        if(is.element(tmp,seq(span[1],span[2],(10**-es.round)))){
        data_out[seq(span[1],span[2],(10**-es.round))==tmp]=1}else{next}
        }

    return(data_out)
    
    } # end function CC.es2ts
