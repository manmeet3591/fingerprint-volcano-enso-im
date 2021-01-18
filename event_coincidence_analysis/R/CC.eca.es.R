# Autor: Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.eca.es performes event coincidence analysis including two different significance tests using event time series and some parameters.
CC.eca.es <- function(seriesA,seriesB,spanA,spanB,delT,alpha=0.05,sym=FALSE,tau=0,sigtest="poisson",reps=1000){ 
    # ----------------------------------------------- TEST FOR ERRORS IN FUNCTION CALL  ------------------------------------------------------------------------------  
    # ---- #1: delT or tau negative
    if(tau<0 || delT<0){
        print("|-------------    ERROR #1    -------------|")
        print("|    The offset (tau) or delta T (delT)    |")
        print("|              is negative.                |") 
        print("|------------------------------------------|")
        return()}
    # ---- #2: seriesA is not a vector
    if(!is.vector(seriesA)){
        print("|-------------    ERROR #2    -------------|")
        print("|         series A is not a vector         |")
        print("|------------------------------------------|")
        return()}
    # ---- #3: seriesB is not a vector
    if(!is.vector(seriesB)){
        print("|-------------    ERROR #3    -------------|")
        print("|         series B is not a vector         |")
        print("|------------------------------------------|")
        return()}
    # ---- #4: time spans do not match
    if(spanA[1]>spanB[2] || spanB[1]>spanA[2]){
        print("|-------------    ERROR #4    -------------|")
        print("|         no common time span found        |")
        print("|          for spanA and spanB             |")       
        print("|------------------------------------------|")
        return()} 
    # ---- #6: list format
    if(is.list(seriesA)|| is.list(seriesB)){
        print("|-------------    ERROR #6    -------------|")
        print("|  seriesA or seriesB seems to be a list   |")
        print("|          but has to be a vector          |")       
        print("|------------------------------------------|")
        return()} 

    # ----------------------------------------------- EVENT COINCIDENCE ANALYSIS  ------------------------------------------------------------------------------------  
    # Get Coincidences 
    N_A=length(seriesA) # number of events in seriesA
    N_B=length(seriesB) # number of ecents in seriesB
    span=(max(spanA[1],spanB[1]):min(spanA[2],spanB[2])) # getting common time span of seriesA and B. Will be used for coincidence analysis.
    # Get Precursor Coincidence Rate
        K_prec=0
        for(step_a in 1:N_A){
            if( !is.element(seriesA[step_a],span) ){next} 
            for(step_b in 1:N_B){
                if( !is.element(seriesB[step_b],span) ){next}
                if(sym==FALSE){  if( is.element(((seriesA[step_a]-tau)-seriesB[step_b]),c(0:(delT)))){K_prec=K_prec+1;break} } # end if sym=FALSE
                if(sym==TRUE){   if( is.element(((seriesA[step_a]-tau)-seriesB[step_b]),c(-delT:delT))){K_prec=K_prec+1;break} } # end if sym=TRUE
            } # end for step_b
        } # end for step_a
        CRprec=K_prec/N_A
        
    # Get Trigger Coincidence Rate 
        K_trigg=0
        for(step_b in 1:N_B){
            if( !is.element(seriesB[step_b],span) ){next}
            for(step_a in 1:N_A){
                if( !is.element(seriesA[step_a],span) ){next}
                if(sym==FALSE){  if( is.element(((seriesA[step_a]-tau)-seriesB[step_b]),c(0:(delT)))){K_trigg=K_trigg+1;break} } # end if sym=FALSE
                if(sym==TRUE){   if( is.element(((seriesA[step_a]-tau)-seriesB[step_b]),c(-delT:delT))){K_trigg=K_trigg+1;break} } # end if sym=TRUE
            } # end for step_a
        } # end for step_b
        CRtrigg=K_trigg/N_B      
        
    # ----------------------------------------------- Significance Test ------------------------------------------------------------------------------------------------
    # 
    if(sigtest=="poisson"){
    # Calculate P = the probability, that the given number of coincidences (K) or more coincidences would occur with two random time series, having the same length and numbers of events.
        Tlen=length(span)
    #------------------------------------------
        if(sym==FALSE){
        # Calculation for Precursor Coincidence 
          Pprec=0
          for(Ktmp in K_prec:N_A){
                Ptmp=choose(N_A,Ktmp) * ( (1-((1-(delT/(Tlen-tau)))**N_B)) **Ktmp) * (((1-(delT/(Tlen-tau)))**N_B)**(N_A-Ktmp))
                Pprec=Pprec+Ptmp}  # end for Ktmp
        # Calculation for Trigger Coincidence
            Ptrigg=0
            for(Ktmp in K_trigg:N_B){
                Ptmp=choose(N_B,Ktmp) * ( (1-((1-(delT/(Tlen-tau)))**N_A)) **Ktmp) * (((1-(delT/(Tlen-tau)))**N_A)**(N_B-Ktmp))
                Ptrigg=Ptrigg+Ptmp}  # end for Ktmp
        } # end if sym
    #------------------------------------------
        if(sym==TRUE){
        # Calculation for Precursor Coincidence
            Pprec=0
            delTsym=delT+delT-1
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
        Tlen=length(span)
    # calculate waiting times of seriesA
        seriesA_sort=sort(seriesA)
        wtA=rep(0,N_A)
        wtA[1]=seriesA_sort[1]-spanA[1]
        for(i in 2:N_A){wtA[i]=seriesA_sort[i]-seriesA_sort[i-1]}
    # calculate waiting times of seriesB
        seriesB_sort=sort(seriesB)
        wtB=rep(0,N_B)
        wtB[1]=seriesB_sort[1]-spanB[1]
        for(i in 2:N_B){wtB[i]=seriesB_sort[i]-seriesB_sort[i-1]}
    # create reps times two surrogate event series and perform coincidence analysis
        surdist=matrix(NA,2,reps)
        for(surno in 1:reps){
        # create surrogate for seriesA
            surA=sample(wtA,size=1)
            for(i in 2:length(seriesA)){
                tmp=surA[i-1]+sample(wtA,size=1)
            if(tmp>span[Tlen]){break}else{surA[i]=tmp}}
        # create surrogate for seriesB
            surB=sample(wtB,size=1)
            for(i in 2:length(seriesB)){
                tmp=surB[i-1]+sample(wtB,size=1)
                if(tmp>span[Tlen]){break}else{surB[i]=tmp}}
        # perform event coincidence analysis between the two surrogate event time series as given above:
        # Get surrogate Precursor Coincidence Rate
            K_prec_sur=0
            for(step_a in 1:N_A){
                if( !is.element(surA[step_a],span) ){next} 
                for(step_b in 1:N_B){
                    if( !is.element(surB[step_b],span) ){next} 
                    if(sym==FALSE){
                        if( is.element(((surA[step_a]-tau)-surB[step_b]),c(0:delT))){K_prec_sur=K_prec_sur+1;break} } # end if sym=FALSE
                    if(sym==TRUE){
                        if( is.element(((surA[step_a]-tau)-surB[step_b]),c(-delT:delT))){K_prec_sur=K_prec_sur+1;break} } # end if sym=TRUE
                } # end for step_b
            } # end for step_a
            surdist[1,surno]=K_prec_sur/N_A
        # Get surrogate Trigger Coincidence Rate 
            K_trigg_sur=0
            for(step_b in 1:N_B){
                if( !is.element(surB[step_b],span) ){next}
                for(step_a in 1:N_A){
                    if( !is.element(surA[step_a],span) ){next}
                    if(sym==FALSE){
                        if( is.element(((surA[step_a]-tau)-surB[step_b]),c(0:delT))){K_trigg_sur=K_trigg_sur+1;break} } # end if sym=FALSE
                    if(sym==TRUE){
                        if( is.element(((surA[step_a]-tau)-surB[step_b]),c(-delT:delT))){K_trigg_sur=K_trigg_sur+1;break} } # end if sym=TRUE
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
            Tlen=length(span)
            span=seq(1:Tlen)
            # create reps times two surrogate event series and perform coincidence analysis
            surdist=matrix(NA,2,reps)
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
        
        }# end function CC.eca.es
