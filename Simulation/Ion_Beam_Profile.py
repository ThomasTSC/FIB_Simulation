# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:40:03 2018

@author: thoma
"""

import Parameters
import numpy
import Grid_Structure
import Physical_Effect


class Ion_Beam_Profile:
    
    def __init__(self, Profile):
        self.Parameters = Parameters.Parameters()
        self.Profile = Profile
        

    def primaryIonBeamProfile(self, Beam_Position_X, Beam_Position_Y):
        
        
        Primary_Ion_Beam_Profile = self.Parameters['Ion_Flux']*numpy.exp(-(((self.Profile['Grid_X']-Beam_Position_X)**2+(self.Profile['Grid_Y']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
        
    
        Primary_Ion_Beam_Profile = {'Primary_Ion_Beam_Profile':Primary_Ion_Beam_Profile}
    
        #print (Primary_Ion_Beam_Profile)
    
        return Primary_Ion_Beam_Profile
        
    
    
    
    def reDepositionProfile(self, Beam_Position_X, Beam_Position_Y):
        
        Grid_Area = Grid_Structure.Grid_Structure(self.Profile).gridArea()
        
        Primary_Sputtering_Depth = Physical_Effect.Physical_Effect(self.Profile).primarySputtering(Beam_Position_X, Beam_Position_Y)['Primary_Sputtering_Depth_Total']
        
        Redeposition_Amout = Primary_Sputtering_Depth*Grid_Area['Grid_Area']
        
        Re_Deposition_Profile = Redeposition_Amout*numpy.exp(-(((self.Profile['Grid_X']-Beam_Position_X)**2+(self.Profile['Grid_Y']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))

        Re_Deposition_Profile = {'Re_Deposition_Profile':Re_Deposition_Profile}
        
        print (Re_Deposition_Profile)
        
        return Re_Deposition_Profile
    
    
    def secondaryIonBeamProfile(self, Beam_Position_X, Beam_Position_Y):
        
        Primary_Sputtering_Depth = Physical_Effect.Physical_Effect(self.Profile).primarySputtering(Beam_Position_X, Beam_Position_Y)['Primary_Sputtering_Depth_Total']
        
        Secondary_Ion_Beam_Profile = {}
        
        
        return Secondary_Ion_Beam_Profile
    
    
    
if __name__ == "__main__":
    

    
    
    print ('done')
