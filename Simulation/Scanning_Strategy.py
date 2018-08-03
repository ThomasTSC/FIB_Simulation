# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:51:32 2018

@author: thoma
"""

import Parameters




class Scanning_Strategy:
    
    def __init__(self):
        self.Parameters = Parameters.Parameters()
        self.Start_X = 6*self.Parameters['Beam_Radius']
        self.Start_Y = self.Parameters['Beam_Radius']


    def rasterScan(self):
        

        Scanning_Path_X = []
        
        for Step in range(self.Parameters['Step']):
            Scanning_Path_X.append(self.Start_X + Step*self.Parameters['Pixel_Distance'])
            
        Scanning_Path_X = self.Parameters['Pass']*Scanning_Path_X
        Scanning_Path_Y = len(Scanning_Path_X)*[self.Start_Y]
        
        

        
        
        
        Scanning_Path = {'Scanning_Path_X':Scanning_Path_X,
                         'Scanning_Path_Y':Scanning_Path_Y}
        
        
        #print (Scanning_Path)
        
        return Scanning_Path
        
        
        
    def serpentineScan(self):
        
        return
        
   
   
if __name__ == "__main__":
    
    Scanning_Strategy().rasterScan()
    print ('done')