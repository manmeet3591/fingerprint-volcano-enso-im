#!/bin/bash

#python gen_surr_v1.py test1
for i in 1053
do
echo $i
python gen_surr_v2.py tas_ipsl_surr_${i}.txt

done
