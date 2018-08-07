import timeit

import pyximport

pyximport.install()

######

import Cython_Loop


start = timeit.default_timer()

Cython_Loop._Simulation()

stop = timeit.default_timer()

print (stop - start) 




