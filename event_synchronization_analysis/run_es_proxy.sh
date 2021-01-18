#!/bin/bash
for i in {8501..10000}
do
tmpfile=$(mktemp --suffix=".sh")
echo "python ed_lf_es_proxy_mc.py  $i" >> $tmpfile
bsub -q "cccr-res" -W 240:00 -J "es" -o "es.out" < $tmpfile
done
