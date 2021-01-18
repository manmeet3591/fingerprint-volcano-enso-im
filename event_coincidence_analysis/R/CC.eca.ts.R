# Autor: Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.eca.ts performes event coincidence analysis including two different significance tests using time series and some parameters.

CC.eca.ts <- function(seriesA,seriesB,alpha=0.05,delT=0,sym=FALSE,tau=0,sigtest="poisson",reps=1000){ 
    # ----------------------------------------------- TEST FOR ERRORS IN FUNCTION CALL  ------------------------------------------------------------------------------  
    # ---- #1: Time series not binary 
    if(length(table(seriesA))>2){
        print("|-------------    ERROR #1    -------------|")
        print("|       Time seriesA is not binary         |")
        print("|      (or the number of events=0)!        |") 
        print("| Use CC.binarize() to preprocess seriesA  |")
        print("|------------------------------------------|")
        return()}
    if(length(table(seriesB))>2){  
        print("|-------------    ERROR #1    -------------|")
        print("|       Time seriesB is not binary         |")
        print("|      (or the number of events=0)!        |") 
        print("| Use CC.binarize() to preprocess seriesA  |")
        print("|------------------------------------------|")
        return()}
    # ---- #2: delT or tau negative
    if(tau<0 || delT<0){
        print("|-------------    ERROR #2    -------------|")
        print("|    The offset (tau) or delta T (delT)    |")
        print("|              is negative.                |") 
        print("|------------------------------------------|")
        return()}
    # ---- #4: lengths of series A and B differ
    if(length(seriesA)!=length(seriesB)){
        print("|-------------    ERROR #4    -------------|")
        print("|    lengths of series A and B differ      |")
        print("|------------------------------------------|")
        return()} 
    # ---- #5: seriesA or seriesB is not a vector
    if(!is.vector(seriesA) && !is.matrix(seriesA)){
        print("|-------------    ERROR #5    -------------|")
        print("| series A is neither vector nor matrix    |")
        print("|------------------------------------------|")
        return()} 
    # ---- #5: seriesA or seriesB is not a vector
    if(!is.vector(seriesB) && !is.matrix(seriesB)){
        print("|-------------    ERROR #5    -------------|")
        print("| series B is neither vector nor matrix    |")
        print("|------------------------------------------|")
        return()} 
    # ---- #6: seriesA or seriesB contain NAs, surrogate doesnt work
    if(any(is.na(seriesA)) && sigtest=="surrogate"){
        print("|-------------    ERROR #6    -------------|")
        print("|          seriesA contains NAs.           |")
        print("| surrogate test not allowed, use poisson  |")       
        print("|------------------------------------------|")
        return()} 
    if(any(is.na(seriesB)) && sigtest=="surrogate"){
        print("|-------------    ERROR #6    -------------|")
        print("|          seriesB contains NAs.           |")
        print("| surrogate test not allowed, use poisson  |")       
        print("|------------------------------------------|")
        return()} 
    if(any(is.na(seriesB)) && sigtest=="shuffle"){
        print("|-------------    ERROR #6    -------------|")
        print("|    seriesB or seriesA contains NAs.      |")
        print("| shuffle test not allowed, use poisson    |")       
        print("|------------------------------------------|")
        return()} 
    
    # Break function if one of the two series only holds NAs
    if(sum(is.na(seriesA))==length(seriesA) || sum(is.na(seriesB))==length(seriesB)){
        CA_out=list(NA,NA,NA,NA,NA,NA)
        names(CA_out)=c("NH precursor","NH trigger","p-value precursor","p-value trigger","precursor coincidence rate","trigger coincidence rate")
    return(CA_out)}
    
    
    
    # write the two binarized time series to bindata
    seriesA[is.na(seriesB)]=NA
    seriesB[is.na(seriesA)]=NA
    bindata=matrix(NA,2,length(seriesA))
    bindata[1,]=seriesA
    bindata[2,]=seriesB
    rownames(bindata)=c("seriesA","seriesB")


    # ----------------------------------------------- COINCIDENCE ANALYSIS part I ------------------------------------------------------------------  
    # Get Coincidences 
    #  Count number of simultaneous events (Coincicences, K), number of events per series (N_A, N_N) and the maximum number of coincidences (Kmax)
    Tlen=length(bindata[1,!is.na(bindata[1,])])
    steplen=length(seriesA)
    N_A=as.numeric(Tlen-table(bindata[1,]==1)[1])
    N_B=as.numeric(Tlen-table(bindata[2,]==1)[1])
   
    

    # Get Precursor Coincidence Rate
        K_prec=0
        for(step in 1:steplen){    if(is.na(bindata[1,step])){next}
            if(bindata[1,step]==1){
                    start=step-tau-(delT)
                if(sym==TRUE){
                    end=step-tau+(delT)}
                if(sym==FALSE){end=step-tau}
            if(start<1 & end>=1){start=1};if(start<1 & end<1){next}
            if(start>steplen){next};if(end>steplen){end=steplen}
                if( is.element(1,bindata[2,start:end])){K_prec=K_prec+1}
            } # end if bindata[1,]==1
        } # end for step
        CRprec=K_prec/N_A
        
    # Get Trigger Coincidence Rate 
        K_trigg=0
        for(step in 1:steplen){    if(is.na(bindata[2,step])){next}
            if(bindata[2,step]==1){
                if(sym==TRUE){
                    start=step+tau-(delT)}
                if(sym==FALSE){
                    start=step+tau}
                    end=step+tau+(delT)
            if(start<1 & end>=1){start=1};if(start<1 & end<1){next}
            if(start>steplen){next};if(end>steplen){end=steplen}
                if( is.element(1,bindata[1,start:end] )){K_trigg=K_trigg+1}
            } # end if bindata[2,]==1
        } # end for step 
        CRtrigg=K_trigg/N_B     
        
    # ----------------------------------------------- Significance Testing  -------------------------------------------------------------------------------------------    
    if(sigtest=="poisson"){
    # Calculate P= the probability, that the given number of coincidences (K) or more coincidences would occur with two random time series, having the same length and numbers of events.
        if(sym==FALSE){
        # Calculation for Precursor Coincidence 
            Pprec=0
            for(Ktmp in K_prec:N_A){
                Ptmp=choose(N_A,Ktmp) * ( (1-((1-((delT+1)/(Tlen-tau)))**N_B)) **Ktmp) * (((1-((delT+1)/(Tlen-tau)))**N_B)**(N_A-Ktmp))
                Pprec=Pprec+Ptmp}  # end for Ktmp
        # Calculation for Trigger Coincidence 
            Ptrigg=0
            for(Ktmp in K_trigg:N_B){
                Ptmp=choose(N_B,Ktmp) * ( (1-((1-((delT+1)/(Tlen-tau)))**N_A)) **Ktmp) * (((1-((delT+1)/(Tlen-tau)))**N_A)**(N_B-Ktmp))
                Ptrigg=Ptrigg+Ptmp}  # end for Ktmp
        } # end if sym
        if(sym==TRUE){
        # Calculation for Precursor Coincidence 
            Pprec=0
            delTsym=delT+delT+1
            for(Ktmp in K_prec:N_A){
                Ptmp=choose(N_A,Ktmp) * ( (1-((1-(delTsym/(Tlen)))**N_B)) **Ktmp) * (((1-(delTsym/(Tlen)))**N_B)**(N_A-Ktmp))
                Pprec=Pprec+Ptmp}  # end for Ktmp
        # Calculation for Trigger Coincidence 
            Ptrigg=0
            for(Ktmp in K_trigg:N_B){
                Ptmp=choose(N_B,Ktmp) * ( (1-((1-(delTsym/(Tlen)))**N_A)) **Ktmp) * (((1-(delTsym/(Tlen)))**N_A)**(N_B-Ktmp))
                Ptrigg=Ptrigg+Ptmp}  # end for Ktmp
        }  # end if sym     
    } # end if sigtest
        
    if(sigtest=="wt.surrogate"){
    # create 'reps' (standard = 1000) surrogate sime series for seriesA and seriesB, having the same average waiting times between two events. Then performe
    # coincidence analysis as given above for all 1000 pairs of event series. Finally get the percentile of the ampirically found coincidence rate using the 
    # ecdf of the 1000 surrogatecoincidence rates.
        if(delT==0){delT=1}
        seriesA=CC.ts2es(seriesA) # transform time series to event series
        seriesB=CC.ts2es(seriesB)
        span=(max(seriesA$span[1],seriesB$span[1]):min(seriesA$span[2],seriesB$span[2]))
        Tlen=length(span)
        # calculate waiting times of seriesA
        seriesA_sort=sort(seriesA$es)
        wtA=rep(0,N_A)
        wtA[1]=seriesA_sort[1]-seriesA$span[1]
        for(i in 2:N_A){wtA[i]=seriesA_sort[i]-seriesA_sort[i-1]}
        # calculate waiting times of seriesB
        seriesB_sort=sort(seriesB$es)
        wtB=rep(0,N_B)
        wtB[1]=seriesB_sort[1]-seriesB$span[1]
        for(i in 2:N_B){wtB[i]=seriesB_sort[i]-seriesB_sort[i-1]}
        # create reps times two surrogate event series and perform coincidence analysis
        surdist=matrix(NA,2,reps)
        for(surno in 1:reps){
            # create surrogate for seriesA
            surA=sample(wtA,size=1)
            for(i in 2:length(seriesA$es)){
                tmp=surA[i-1]+sample(wtA,size=1)
                if(tmp>span[Tlen]){break}else{surA[i]=tmp}}
            # create surrogate for seriesB
            surB=sample(wtB,size=1)
            for(i in 2:length(seriesB$es)){
                tmp=surB[i-1]+sample(wtB,size=1)
                if(tmp>span[Tlen]){break}else{surB[i]=tmp}}
        # perform event coincidence analysis between the two surrogate event time series as given above:
        # Get surrogate Precursor Coincidence Rate
            K_prec_sur=0
            for(step_a in 1:N_A){
                if( !is.element(surA[step_a],span) ){next}
                for(step_b in 1:N_B){
                    if( !is.element(surB[step_b],span) ){next} 
                    if(sym==FALSE){  if( is.element(((surA[step_a]-tau)-surB[step_b]),c(0:delT))){K_prec_sur=K_prec_sur+1;break} } # end if sym=FALSE
                    if(sym==TRUE){   if( is.element(((surA[step_a]-tau)-surB[step_b]),c(-delT:delT))){K_prec_sur=K_prec_sur+1;break} } # end if sym=TRUE
                } # end for step_b
            } # end for step_a
            surdist[1,surno]=K_prec_sur/N_A
            # Get surrogate Trigger Coincidence Rate 
            K_trigg_sur=0
            for(step_b in 1:N_B){
                if( !is.element(surB[step_b],span) ){next}
                for(step_a in 1:N_A){
                    if( !is.element(surA[step_a],span) ){next} 
                    if(sym==FALSE){   if( is.element(((surA[step_a]-tau)-surB[step_b]),c(0:delT))){K_trigg_sur=K_trigg_sur+1;break} } # end if sym=FALSE
                    if(sym==TRUE){    if( is.element(((surA[step_a]-tau)-surB[step_b]),c(-delT:delT))){K_trigg_sur=K_trigg_sur+1;break} } # end if sym=TRUE
                } # end for step_a
            } # end for step_b
            surdist[2,surno]=K_trigg_sur/N_B  
        }
        Pprec=1-ecdf(surdist[1,])(CRprec)
        Ptrigg=1-ecdf(surdist[2,])(CRtrigg)       
    } # end if sigtest surrogate 
    
        if(sigtest=="shuffle.surrogate"){
            # create 'reps' (standard = 1000) shuffled time series for seriesA and seriesB, having the same number of events. Then performe
            # coincidence analysis as given above for all 1000 pairs of event series. Finally get the percentile of the empirically found coincidence rate using the 
            # ecdf of the 1000 surrogatecoincidence rates.
            # create reps times two surrogate event series and perform coincidence analysis
            surdist=matrix(NA,2,reps)
            span=seq(1:steplen)
            for(surno in 1:reps){
                # create shuffle for seriesA
                surA=sample(span,size=N_A)
                # create shuffle for seriesB
                surB=sample(span,size=N_B)
                # perform event coincidence analysis between the two surrogate event time series as given above:
                # Get surrogate Precursor Coincidence Rate
                K_prec_sur=0
                for(step_a in 1:N_A){
                    for(step_b in 1:N_B){
                        if(sym==FALSE){  if( is.element(((surA[step_a]-tau)-surB[step_b]),c(0:delT))){K_prec_sur=K_prec_sur+1;break} } # end if sym=FALSE
                        if(sym==TRUE){   if( is.element(((surA[step_a]-tau)-surB[step_b]),c(-delT:delT))){K_prec_sur=K_prec_sur+1;break} } # end if sym=TRUE
                    } # end for step_b
                } # end for step_a
                surdist[1,surno]=K_prec_sur/N_A
                # Get surrogate Trigger Coincidence Rate 
                K_trigg_sur=0
                for(step_b in 1:N_B){
                    for(step_a in 1:N_A){
                        if(sym==FALSE){   if( is.element(((surA[step_a]-tau)-surB[step_b]),c(0:delT))){K_trigg_sur=K_trigg_sur+1;break} } # end if sym=FALSE
                        if(sym==TRUE){    if( is.element(((surA[step_a]-tau)-surB[step_b]),c(-delT:delT))){K_trigg_sur=K_trigg_sur+1;break} } # end if sym=TRUE
                    } # end for step_a
                } # end for step_b
                surdist[2,surno]=K_trigg_sur/N_B  
            }
            Pprec=1-ecdf(surdist[1,])(CRprec)
            Ptrigg=1-ecdf(surdist[2,])(CRtrigg)       
        } # end if sigtest shuffle 
        
    # Test whether Pprec<alpha   
        sig_testprec=logical
        if(Pprec>=alpha){sig_testprec=TRUE}else{sig_testprec=FALSE}
    # Test whether Ptrigg<alpha   
        sig_testtrigg=logical
        if(Ptrigg>=alpha){sig_testtrigg=TRUE}else{sig_testtrigg=FALSE}
    
    
        # ----------------------------------------------- WRITE OUTPUT -----------------------------------------------------------------    
        

        CA_out=list(sig_testprec,sig_testtrigg,Pprec,Ptrigg,CRprec,CRtrigg)
        names(CA_out)=c("NH precursor","NH trigger","p-value precursor","p-value trigger","precursor coincidence rate","trigger coincidence rate")
        return(CA_out)
        
        } # end function CC.eca.ts
