clear all
clc
load('plv_hist.csv')
load('plv_pi.csv')
plv_hist_1(plv_hist<0.98)=0.0;
plv_pi_1(plv_pi<0.98)=0.0;
plv_hist_1(plv_hist>0.98)=1.0;
plv_pi_1(plv_pi>0.98)=1.0;
%scatter(plv_pi,plv_hist(1:11964))
