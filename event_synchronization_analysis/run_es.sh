#!/bin/bash
for i in {8001..10000}
do
tmpfile=$(mktemp --suffix=".sh")
echo "python event_synchronization_mc.py $i" >> $tmpfile
bsub -q "cccr-res" -W 240:00 -J "es" -o "es.out" < $tmpfile
done
