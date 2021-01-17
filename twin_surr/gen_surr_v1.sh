#!/bin/bash

#python gen_surr_v1.py test1
for i in {0..5000}
do
tmpfile=$(mktemp --suffix=".sh")

echo "source activate python_2_7" > $tmpfile
#echo "python gen_surr_v1.py tos_hadcm3_surr_${i}.txt" >> $tmpfile
#echo "python gen_surr_v1.py pr_mpi_surr_${i}.txt" >> $tmpfile
#echo "python gen_surr_v1.py tas_ipsl_surr_${i}.txt" >> $tmpfile
#echo "python gen_surr_v1.py pr_ipsl_surr_${i}.txt" >> $tmpfile
#echo "python gen_surr_v1.py tos_giss_surr_${i}.txt" >> $tmpfile
#echo "python gen_surr_v1.py pr_giss_surr_${i}.txt" >> $tmpfile
bsub -q "cccr-res" -W 10:00 -J "surr_${i}" -o "twin_surr.out" -e "twin_surr.err" < $tmpfile
done
