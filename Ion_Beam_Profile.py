# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:40:03 2018

@author: thoma
"""

import Parameters
import numpy
import Grid_Structure


class Ion_Beam_Profile:
    
    def __init__(self):
        self.Parameters = Parameters.Parameters()
        self.Grid_X = Grid_Structure.Grid_Structure().initialGrid()['Grid_X']
        self.Grid_Y = Grid_Structure.Grid_Structure().initialGrid()['Grid_Y']
        self.Grid_Z = Grid_Structure.Grid_Structure().initialGrid()['Grid_Z']
        
        
        
        self.Ion_Flux = self.Parameters['Beam_Diameter']*(self.Parameters['Beam_Current'])/self.Parameters['Unit_Charge']
    
    
    def Primary_Ion_Beam_Profile(self, Scanning_Path_X, Scanning_Path_Y):
        
        Primary_Ion_Beam_Profile = {}

        
        Primary_Ion_Beam_Profile = self.Ion_Flux*(1/(2*(numpy.pi**2)*(self.Parameters['Beam_Standard_Deviation']**2)))*numpy.exp(-(((self.Grid_X-Scanning_Path_X)**2+(self.Grid_Y-Scanning_Path_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
    
    
        #print (len(Primary_Ion_Beam_Profile))
    
        return Primary_Ion_Beam_Profile
    
    
    def averagePrimeIonBeam_per_Grid(self):
        
        
        
        
        
        return Average_Prime_Ion_Beam
    
    def Secondary_Ion_Beam_Profile(self):
        
        
        
        
        
        return Secondary_Ion_Beam_Profile
    
    
    def averageSecondaryIonBeam_per_Grid(self):
        
        
        
        return Average_Secondary_Ion_Beam
        
        
    
if __name__ == "__main__":
    
    import Scanning_Strategy

    
    Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()

    Primary_Ion_Beam_Profile= Ion_Beam_Profile().Primary_Ion_Beam_Profile(Scanning_Path['Scanning_Path_X'][0], Scanning_Path['Scanning_Path_Y'][0])


    
    print ('done')
