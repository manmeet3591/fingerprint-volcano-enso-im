#!/bin/bash
tmpfile=$(mktemp --suffix=".sh")
echo "mpirun -n 100 /iitm2/cccr-res/msingh/anaconda3/envs/py35/bin/python test_mpi.py" >> $tmpfile
bsub -q "cccr-res" -W 240:00 -J "es" -o "test.out" < $tmpfile
