# Autor: Jonatan Siegmund, Potsdam Institute for Climate Impact Research, 2015
# This function is part of the R package CoinCalc().
# CC.plot generates a plot that illustrates the results of a coincidence analysis for a given pair of event time series.

CC.plot <- function(seriesA,seriesB,delT=0,sym=FALSE,tau=0,dates=NA,seriesAname="Event Series A",seriesBname="Event Series B"){ 

    # write the two binarized time series to bindata
    seriesA[is.na(seriesB)]=NA
    seriesB[is.na(seriesA)]=NA
    bindata=matrix(NA,2,length(seriesA))
    bindata[1,]=seriesA
    bindata[2,]=seriesB
    rownames(bindata)=c("seriesA","seriesB")

    
    # ----------------------------------------------- COINCIDENCE ANALYSIS ------------------------------------------------------------------  
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
            start=step-tau-delT
            if(sym==TRUE){
                end=step-tau+delT}
            if(sym==FALSE){end=step-tau}
            if(start<1){start=1};if(end<1){end=1}
            if(start>steplen){start=steplen};if(end>steplen){end=steplen}
            if( is.element(1,bindata[2,start:end])){K_prec=K_prec+1}
        } # end if bindata[1,]==1
    } # end for step
    CRprec=K_prec/N_A
    
    # Get Trigger Coincidence Rate 
    K_trigg=0
    for(step in 1:steplen){    if(is.na(bindata[2,step])){next}
        if(bindata[2,step]==1){
            if(sym==TRUE){
                start=step+tau-delT}
            if(sym==FALSE){
                start=step+tau}
            end=step+tau+delT
            if(start<1){start=1};if(end<1){end=1}
            if(start>steplen){start=steplen};if(end>steplen){end=steplen}
            if( is.element(1,bindata[1,start:end] )){K_trigg=K_trigg+1}
        } # end if bindata[2,]==1
    } # end for step 
    CRtrigg=K_trigg/N_B      

    
        # ----------------------------------------------- CREATE PLOT ----------------------------------------------------------------- 

        plotlen=length(seriesA)
        par(mfrow=c(2,1))
        # scale plot lwd
        if(plotlen<200){lwd.tmp=8}
        if(plotlen>200 && plotlen<1000){lwd.tmp=round((8/plotlen)*150,digits=1)}
        if(plotlen>1000){lwd.tmp=2}
        # Define plot colors
        lred=rgb(252,187,161,maxColorValue=255);dred=rgb(251,106,74,maxColorValue=255)
        lblue=rgb(189,201,225,maxColorValue=255);dblue=rgb(4,90,141,maxColorValue=255)
        
        # plot precursor coincidence
        # plot seriesA
        lineser1=rep(0.2,plotlen);lineser1[seriesA==1]=NA;lineser1[is.na(seriesA)]=NA
        plot(lineser1,xlim=c(0,plotlen+plotlen/30),ylim=c(-1,1),axes=FALSE,col="white",ylab="",xlab="",pch=3,asp=(plotlen/10)) # prepare plot
        arrows(x0=0,x1=(plotlen+(plotlen/30)),y0=0.2,y1=0.2,lwd=9,col=lred,angle=50);arrows(x0=0,x1=(plotlen+(plotlen/30)),y0=-0.2,y1=-0.2,lwd=9,col=lblue,angle=50) # time line arrows
        if(plotlen<1000){points(lineser1,pch=3)}else{points(lineser1,pch=3,cex=0.1)}
        
        text(x=plotlen,y=-0.7,"Time",cex=1.8,col="lightgrey",font=2)
        title(main=paste0("Precursor Coincidence Rate : ",round(CRprec,digits=3)),cex=1.8,font=2)
        text(x=plotlen-plotlen*0.9,y= 0.8,seriesAname,cex=1.8,col=dred,font=2)
        text(x=plotlen-plotlen*0.9,y=-0.8,seriesBname,cex=1.8,col=dblue,font=2)
        # plot all events in seriesA
        for(i in 1:plotlen){if(is.na(seriesA[i])){next};if(seriesA[i]==1){polygon(x=c(i,i),y=c(0.2,0.5),border=lred,lwd=lwd.tmp)}}
        # plot tau + delT for every event
        for(step in 1:plotlen){if(is.na(seriesA[step])){next}
            if(seriesA[step]==1){start=step-tau-delT
            if(length(dates)==length(seriesA)){text(x=step,y=0.6,labels=as.character(dates[step]))} # plot date of event
            if(sym==TRUE){end=step+delT};if(sym==FALSE){end=step-tau}
            if(start<1 & end>=1){start=1};if(end<1){next};if(start>steplen){next};if(end>steplen){end=steplen}
            polygon(x=c(start-0.4,end+0.4,end+0.4,step,start-0.4,start-0.4),y=c(-0.6,-0.6,-0.2,0.2,-0.2,-0.6),col=lred,border=FALSE,lwd=1.5)}}
        # plot tau + delT for coinciding events
        for(step in 1:plotlen){if(is.na(seriesA[step])){next}
            if(seriesA[step]==1){start=step-tau-delT
            if(sym==TRUE){end=step+delT};if(sym==FALSE){end=step-tau}
            if(start<1 & end>=1){start=1};if(end<1){next};if(start>steplen){next};if(end>steplen){end=steplen}
            if( is.element(1,seriesB[start:end] )){
                polygon(x=c(step,step),y=c(0.2,0.5),border=dred,lwd=lwd.tmp)
                polygon(x=c(start-0.4,end+0.4,end+0.4,step,start-0.4,start-0.4),y=c(-0.6,-0.6,-0.2,0.2,-0.2,-0.6),col=dred,border=FALSE,lwd=1.5)}}}
        # plot all events in seriesB 
        lineser2=rep(-0.2,plotlen);lineser2[seriesB==1]=NA;lineser2[is.na(seriesB)]=NA  
        if(plotlen<1000){points(lineser2,ylim=c(0,2),pch=3)}else{points(lineser2,ylim=c(0,2),pch=3,cex=0.1)}
        for(i in 1:plotlen){if(is.na(seriesB[i])){next};if(seriesB[i]==1){polygon(x=c(i,i),y=c(-0.5,-0.2),border=dblue,lwd=lwd.tmp)}}
        
        # plot trigger coincidence
        # plot seriesA
        lineser1=rep(0.2,plotlen);lineser1[seriesA==1]=NA;lineser1[is.na(seriesA)]=NA
        plot(lineser1,xlim=c(0,plotlen+plotlen/30),ylim=c(-1,1),axes=FALSE,col="white",ylab="",xlab="",pch=3,asp=(plotlen/10)) # prepare plot
        arrows(x0=0,x1=(plotlen+(plotlen/30)),y0=0.2,y1=0.2,lwd=9,col=lred,angle=50);arrows(x0=0,x1=(plotlen+(plotlen/30)),y0=-0.2,y1=-0.2,lwd=9,col=lblue,angle=50) # time line arrows
        
        text(x=plotlen,y=0.7,"Time",cex=1.8,col="lightgrey",font=2)
        title(main=paste0("Trigger Coincidence Rate : ",round(CRtrigg,digits=3)),cex=1.8,font=2)
        text(x=plotlen-plotlen*0.9,y= 0.8,seriesAname,cex=1.8,col=dred,font=2)
        text(x=plotlen-plotlen*0.9,y=-0.8,seriesBname,cex=1.8,col=dblue,font=2)
        # plot all events in seriesB 
        lineser2=rep(-0.2,plotlen);lineser2[seriesB==1]=NA;lineser2[is.na(seriesB)]=NA  
        if(plotlen<1000){points(lineser2,ylim=c(0,2),pch=3)}else{points(lineser2,ylim=c(0,2),pch=3,cex=0.1)}
        for(i in 1:plotlen){if(is.na(seriesB[i])){next};if(seriesB[i]==1){polygon(x=c(i,i),y=c(-0.5,-0.2),border=lblue,lwd=lwd.tmp)}} 
        # plot tau + delT for every event
        for(step in 1:plotlen){if(is.na(seriesB[step])){next}
            if(seriesB[step]==1){end=step+tau+delT
            if(length(dates)==length(seriesA)){text(x=step,y=-0.6,labels=as.character(dates[step]))} # plot date of event
            if(sym==TRUE){start=step-delT};if(sym==FALSE){start=step+tau}
            if(start<1 & end>=1){start=1};if(end<1){next};if(start>steplen){next};if(end>steplen){end=steplen}
            polygon(x=c(start-0.4,end+0.4,end+0.4,step,start-0.4,start-0.4),y=c(0.6,0.6,0.2,-0.2,0.2,0.6),col=lblue,border=FALSE,lwd=1.5)}}
        # plot tau + delT for coinciding events
        for(step in 1:plotlen){if(is.na(seriesB[step])){next}
            if(seriesB[step]==1){end=step+tau+delT
            if(sym==TRUE){start=step-delT};if(sym==FALSE){start=step+tau}
            if(start<1 & end>=1){start=1};if(end<1){next};if(start>steplen){next};if(end>steplen){end=steplen}
            if( is.element(1,seriesA[start:end] )){
                polygon(x=c(step,step),y=c(-0.2,-0.5),border=dblue,lwd=lwd.tmp)
                polygon(x=c(start-0.4,end+0.4,end+0.4,step,start-0.4,start-0.4),y=c(0.6,0.6,0.2,-0.2,0.2,0.6),col=dblue,border=FALSE,lwd=1.5)}}}
        # plot all events in seriesA
        for(i in 1:plotlen){if(is.na(seriesA[i])){next};if(seriesA[i]==1){polygon(x=c(i,i),y=c(0.2,0.5),border=dred,lwd=lwd.tmp)}} 
        if(plotlen<1000){points(lineser1,pch=3)}else{points(lineser1,pch=3,cex=0.1)}
        
        return()}
