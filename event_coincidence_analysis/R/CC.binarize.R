# Autor: Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.binarize can be used to binarize a vector referring to a given threshold. This threshold can either be a percentile or an absolute value.

CC.binarize <- function(data,ev.def="percentile",thres=0.90,event="higher"){ 
        # ----------------------------------------------- TEST FOR ERRORS IN FUNCTION CALL  --------------------------------------------------------  
        # ---- #1: Time series not binary 
        if(!is.vector(data)){
            print("|-------------    ERROR #1    -------------|")
            print("|     given 'data' is not a vector         |")
            print("|------------------------------------------|")
            return()}
        # ----------------------------------------------- BINARISATION ------------------------------------------------------------------------------
        
        tmp=data
        if(ev.def=="percentile"){
            if(event=="higher"){
                data[tmp>quantile(tmp,thres,na.rm=TRUE)]=1;data[tmp<quantile(tmp,thres,na.rm=TRUE)]=0
            } # end if higher
            if(event=="lower"){
                data[tmp<quantile(tmp,thres,na.rm=TRUE)]=1;data[tmp>quantile(tmp,thres,na.rm=TRUE)]=0
            } # end if higher
        data[tmp==quantile(tmp,thres,na.rm=TRUE)]=1
        } # end if percentile

        if(ev.def=="absolute"){
            if(event=="higher"){
                data[tmp>thres]=1;data[tmp<thres]=0
            } # end if higher
            if(event=="lower"){
                data[tmp<thres]=1;data[tmp>thres]=0
            } # end if higher
            data[tmp==thres]=1
        } # end if absolute
        return(data)

        
    } # end function CC.binarize