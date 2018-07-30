# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:40:03 2018

@author: thoma
"""

import Parameters
import numpy
import Grid_Structure
import Simulator
import scipy
import Physical_Effect



class Ion_Beam_Profile:
    
    def __init__(self):
        self.Parameters = Parameters.Parameters()
        self.Profile = Simulator.FIB().Simulation()
        

    def Primary_Ion_Beam_Profile(self, Beam_Position_X, Beam_Position_Y):
        
        Primary_Ion_Beam_Profile = {}
        
        Primary_Ion_Beam_Profile = self.Parameters['Ion_Flux']*numpy.exp(-(((Segment['Segment_XCor']-Beam_Position_X)**2+(Segment['Segment_YCor']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
        
    
        Primary_Ion_Beam_Profile = {'Primary_Ion_Beam_Profile':Primary_Ion_Beam_Profile}
    
        #print (Primary_Ion_Beam_Profile)
    
        return Primary_Ion_Beam_Profile
        
    
    
    
    def Re_Deposition_Profile(self):
        

        return Re_Deposition_Profile
    
    
    
    def Secondary_Ion_Beam_Profile(self):
        
        
        
        
        
        return Secondary_Ion_Beam_Profile
    
    

        
        
    
if __name__ == "__main__":
    

    
    
    print ('done')
