'''
Created on 07.08.2018

@author: chou
'''

import numpy
import matplotlib.pyplot as plt


x=numpy.linspace(-numpy.pi,numpy.pi,1000)

A= (180/numpy.pi)*numpy.arccos(x)

f = (1/(2*numpy.pi))*(1+numpy.cos(x))
print (f)

plt.figure()
plt.plot(A,f)
plt.show()