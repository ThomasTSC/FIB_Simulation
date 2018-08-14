'''
Created on 07.08.2018

@author: chou
'''

import numpy
import matplotlib.pyplot as plt

def referenceCosineDistribution():

    Ref_Radian_Range = numpy.linspace(-numpy.pi,numpy.pi,1000)

    Ref_Cosine_Distribution = (1/(2*numpy.pi))*(1+numpy.cos(Ref_Radian_Range))
    print (Ref_Cosine_Distribution )


    Ref_Cosine_Distribution = {'Ref_Cosine_Distribution': Ref_Cosine_Distribution}

    plt.figure()
    plt.plot(Ref_Radian_Range,Ref_Cosine_Distribution['Ref_Cosine_Distribution'])
    plt.show()
    
    

referenceCosineDistribution()