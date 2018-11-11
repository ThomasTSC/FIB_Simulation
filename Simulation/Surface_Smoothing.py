'''
Created on Oct 10, 2018

@author: thoma
'''


import Parameters
import numpy
import Simulator



class Surface_Smoothing:
    '''
    classdocs
    '''


    def __init__(self,Profile):
        self.Parameters = Parameters.Physical_Parameters()
        self.Profile = Profile
     
        
    def surfaceResampling(self, Profile_X, Profile_Z):
    
        Initial_Grid = Simulator.FIB().initGrid()
    
        
        Grid_Z_Resampling = numpy.interp(Initial_Grid['Grid_X'],Profile_X, Profile_Z)
        Grid_X_Resampling = Initial_Grid['Grid_X']
   
    
        Surface_Resampling = {'Grid_Z_Resampling': Grid_Z_Resampling,
                              'Grid_X_Resampling': Grid_X_Resampling,
                              
                 }  
        
        return Surface_Resampling
    

    
    
    def smoothingTrench(self, Profile_Z, box_pts= 7 ):
        
        box = numpy.ones(box_pts)/box_pts
        Smoothing_Grid_Z = numpy.convolve(Profile_Z, box, mode='same')
  
        Smoothing_Trench = {'Smoothing_Grid_Z':Smoothing_Grid_Z}
        
        return Smoothing_Trench