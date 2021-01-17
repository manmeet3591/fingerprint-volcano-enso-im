cython _ext/numerics.pyx
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/home/manmeet/anaconda3/envs/py27/include/python2.7 -o numerics.so _ext/numerics.c
cp numerics.so _ext/.
