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
    
    def __init__(self, Profile):
        self.Parameters = Parameters.Parameters()
        self.Profile = Profile
        

    def primaryIonBeamProfile(self, Beam_Position_X, Beam_Position_Y):
        
        Primary_Ion_Beam_Profile = {}
        
        Primary_Ion_Beam_Profile = self.Parameters['Ion_Flux']*numpy.exp(-(((self.Profile['Grid_X']-Beam_Position_X)**2+(self.Profile['Grid_Y']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
        
    
        Primary_Ion_Beam_Profile = {'Primary_Ion_Beam_Profile':Primary_Ion_Beam_Profile}
    
        #print (Primary_Ion_Beam_Profile)
    
        return Primary_Ion_Beam_Profile
        
    
    
    
    def reDepositionProfile(self):
        

        return Re_Deposition_Profile
    
    
    
    def secondaryIonBeamProfile(self):
        
        
        
        
        
        return Secondary_Ion_Beam_Profile
    
    
    
    def dilutedIonBeamEffect(self):
        
        
        return Diluted_Ion_Beam_Effect
    
    
    
        
        
    
if __name__ == "__main__":
    

    
    
    print ('done')
