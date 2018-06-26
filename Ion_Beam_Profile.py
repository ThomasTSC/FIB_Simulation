# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:40:03 2018

@author: thoma
"""

import Parameters
import numpy
import Grid_Structure
import Simulator


class Ion_Beam_Profile:
    
    def __init__(self):
        self.Parameters = Parameters.Parameters()
        self.initGrid = Grid_Structure.Grid_Structure().initialGrid()
        
        
        self.Ion_Flux = self.Parameters['Beam_Diameter']*(self.Parameters['Beam_Current'])/self.Parameters['Unit_Charge']
    
    
    def Primary_Ion_Beam_Profile(self, Beam_Position_X, Beam_Position_Y, Segment):
        
        Primary_Ion_Beam_Profile = {}

        
        Primary_Ion_Beam_Profile = self.Ion_Flux*(1/(2*(numpy.pi**2)*(self.Parameters['Beam_Standard_Deviation']**2)))*numpy.exp(-(((Segment['Segment_XCor']-Beam_Position_X)**2+(Segment['Segment_YCor']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
    
    
        #print (len(Primary_Ion_Beam_Profile))
    
        return Primary_Ion_Beam_Profile
    
    
    def averagePrimeIonBeam_per_Segment(self):
        
        
        
        
        
        return Average_Prime_Ion_Beam
    
    def Secondary_Ion_Beam_Profile(self):
        
        
        
        
        
        return Secondary_Ion_Beam_Profile
    
    
    def averageSecondaryIonBeam_per_Segment(self):
        
        
        
        return Average_Secondary_Ion_Beam
        
        
    
if __name__ == "__main__":
    
    import Scanning_Strategy

    
    Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()

    Primary_Ion_Beam_Profile= Ion_Beam_Profile().Primary_Ion_Beam_Profile(Scanning_Path['Scanning_Path_X'][0], Scanning_Path['Scanning_Path_Y'][0])


    
    print ('done')
