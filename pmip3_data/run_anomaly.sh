#!/bin/bash
#for var in "evspsbl"  "tauu" "tauv" "rlds" "rlus" "rsds" "rsus" "rsdscs" "rsuscs" "rldscs" "rsdt" "rsut" "rlut" "rlutcs" "rsutcs" "rtmt" "ua" "va" "wap" "zg" "tro3"
#for var in "rsdscs" "rsuscs" "rldscs" "rsdt" "rsut" "rlut" "rlutcs" "rsutcs" "rtmt" "ua" "va" "wap" "zg" "tro3"
#for var in "zg" "tro3"
for var in "tro3"
do
./anomaly.sh $var
#echo $var
done
