#!/bin/bash
for file in *.nc
do
cdo timmean $file timmean_$file
#echo $file
done
