#!/bin/bash

#python gen_surr_v1.py test1
for i in {0..5000}
do
tmpfile=$(mktemp --suffix=".sh")

echo "source activate py35" > $tmpfile
echo "python main.py $i" >> $tmpfile
bsub -q "cccr-res" -W 10:00 -J "surr_${i}" -o "twin_surr.out" -e "twin_surr.err" < $tmpfile
done
