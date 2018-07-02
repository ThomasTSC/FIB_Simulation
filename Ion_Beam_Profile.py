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
        self.initGrid = Grid_Structure.Grid_Structure().initialGrid()
        
        
            
    
    def Primary_Ion_Beam_Profile(self, Beam_Position_X, Beam_Position_Y, Segment):
        
        Primary_Ion_Beam_Profile = {}
        
        Primary_Ion_Beam_Profile_Mid = self.Parameters['Ion_Flux']*numpy.exp(-(((Segment['Segment_XCor']-Beam_Position_X)**2+(Segment['Segment_YCor']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
        
        Primary_Ion_Beam_Profile_Front = self.Parameters['Ion_Flux']*numpy.exp(-(((Segment['Segment_XCor_Front']-Beam_Position_X)**2+(Segment['Segment_YCor']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
    
        Primary_Ion_Beam_Profile_End = self.Parameters['Ion_Flux']*numpy.exp(-(((Segment['Segment_XCor_End']-Beam_Position_X)**2+(Segment['Segment_YCor']-Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
        #print (len(Primary_Ion_Beam_Profile))
    
        Primary_Ion_Beam_Profile = {'Primary_Ion_Beam_Profile_Mid':Primary_Ion_Beam_Profile_Mid, 'Primary_Ion_Beam_Profile_Front':Primary_Ion_Beam_Profile_Front, 'Primary_Ion_Beam_Profile_End': Primary_Ion_Beam_Profile_End}
    
        #print (Primary_Ion_Beam_Profile)
    
        return Primary_Ion_Beam_Profile
    
    
    def Integral_Over_Beam_Area(self):
        
        
        
        Beam_Profile_Integral = []
        
        
        return Beam_Profile_Integral
    
    
    
    
    
    
    def Re_Deposition_Profile(self,Segment):
        
        
        Grid_Area = Grid_Structure.Grid_Structure().gridArea(Segment)
        
        Primary_Sputtering = Simulator.FIB().Simulation()['Primary_Sputtering']
        
        Sputtered_Material_Amount = Primary_Sputtering['Primary_Sputtering_Depth_Total_Mid']*Grid_Area['Grid_Area']
        
        print (Sputtered_Material_Amount)
        
        #We need an integration of 360 degree here to estimate the redeposition#
        
        
        Re_Deposition_Profile = []
    
        return Re_Deposition_Profile
    
    
    
    
    
    
    
    def Secondary_Ion_Beam_Profile(self):
        
        
        
        
        
        return Secondary_Ion_Beam_Profile
    
    

        
        
    
if __name__ == "__main__":
    
    import Scanning_Strategy

    import Simulator
    
    Segment = Simulator.FIB().Simulation()
    Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()
    Beam_Position = [Scanning_Path['Scanning_Path_X'][0], Scanning_Path['Scanning_Path_Y'][0]]
    Primary_Ion_Beam = Ion_Beam_Profile().Primary_Ion_Beam_Profile(Beam_Position[0], Beam_Position[1], Segment)
    
    Ion_Beam_Profile().Re_Deposition_Profile(Segment)
    

    
    #Re_Deposition_Profile = Ion_Beam_Profile().Re_Deposition_Profile()
    
    
    print ('done')
