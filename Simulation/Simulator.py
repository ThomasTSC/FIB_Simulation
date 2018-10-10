'''
Created on 15.05.2018

@author: chou
'''

import Grid_Structure
import Physical_Effect
import Scanning_Strategy
import Surface_Smoothing
import Parameters
import Post_Process
import numpy
import timeit
import matplotlib.pyplot as plt

class FIB:
    '''
    classdocs
    '''

    def __init__(self):
        
        self.Parameters = Parameters.Parameters()
        
        self.Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()
        
        

    def initGrid(self):
        
        Grid_Point = self.Parameters['Grid_Point']*self.Parameters['Step']
        
        Grid_xlim_max = self.Parameters['Full_Pixel_Length']*self.Parameters['Step']
        
        Grid_X = numpy.linspace(0,self.Parameters['Full_Pixel_Length']*self.Parameters['Step'],Grid_Point)
        
        Grid_Space_X = numpy.diff(Grid_X)[0]
        
        Grid_Y = self.Parameters['Beam_Radius']*numpy.ones_like(Grid_X)
        
        Grid_Z = numpy.zeros_like(Grid_X)
    
        
        initGrid_Structure = {'Grid_X': Grid_X, 
                                 'Grid_Y': Grid_Y,
                                 'Grid_Z': Grid_Z, 
                                 'Grid_xlim_max': Grid_xlim_max,
                                 'Grid_Space_X':Grid_Space_X                                
                                 }
        
        return initGrid_Structure     


    def Simulation(self):
        
        Profile = FIB().initGrid()

        start = timeit.default_timer()
        
        for Pass in range(self.Parameters['Pass']):
            
        
            for Step in range(len(self.Scanning_Path['Scanning_Path_X'])):
                
                Time_Interval = 0
                

                Profile['Grid_X'] = Surface_Smoothing.Surface_Smoothing(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_X_Resampling']
                Profile['Grid_Z'] = Surface_Smoothing.Surface_Smoothing(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_Z_Resampling']
                                
                
                while Time_Interval <= self.Parameters['Dwell_Time']:
                
                    Beam_Position = [self.Scanning_Path['Scanning_Path_X'][Step], self.Scanning_Path['Scanning_Path_Y'][Step]]
                    
                    Primary_Sputtering = Physical_Effect.Physical_Effect(Profile).primarySputtering(Beam_Position[0], Beam_Position[1])
                    
                  
           
        
                    print (Primary_Sputtering)
                
                    Profile['Grid_X'] = Profile['Grid_X'] + Primary_Sputtering['Primary_Sputtering_Depth_X']
                    Profile['Grid_Z'] = Profile['Grid_Z'] + Primary_Sputtering['Primary_Sputtering_Depth_Z'] 
                    
                
                    Redeposition = Physical_Effect.Physical_Effect(Profile).reDeposition(Beam_Position[0], Beam_Position[1])
                    
                    Profile['Grid_X'] = Profile['Grid_X'] + Redeposition['Redeposition_X']
                    Profile['Grid_Z'] = Profile['Grid_Z'] + Redeposition['Redeposition_Z'] 
                    
                    print (Redeposition)
                    
                    
                    plt.figure()
                    plt.plot(Profile['Grid_X'],Redeposition['Redeposition_Total'])
                    #plt.plot(self.Profile['Grid_X'],Redeposition_Angular_Distribution['Redeposition_Angular_Distribution'])
                    plt.show()
                    
                    #Secondary_Sputtering = Physical_Effect.Physical_Effect(Profile).secondarySputtering(Beam_Position[0], Beam_Position[1])
                     
                
                    Profile = {'Grid_X': Profile['Grid_X'], 'Grid_Y':Profile['Grid_Y'], 'Grid_Z':Profile['Grid_Z'], 'Grid_Space_X':Profile['Grid_Space_X'] } 
        
                
                    Time_Interval = Time_Interval + self.Parameters['Integration_Time']
            
            
        
        Profile['Grid_X'] = Profile['Grid_X']
        Profile['Grid_Z'] = Surface_Smoothing.Surface_Smoothing(Profile).smoothingTrench(Profile['Grid_Z'])['Smoothing_Grid_Z']
        
        
        
        stop = timeit.default_timer()

        print (stop - start) 
        
        
        Post_Process.Post_Process().ionDoseAmount()
        Post_Process.Post_Process().plotTrench(Profile) 
        
        
        return Profile
    
    
    
    
if __name__ == "__main__":
    
    
    #import pyximport

    #pyximport.install()

    ######

    #import Cython_Loop
    
    #Cython_Loop._Simulation()

    Profile = FIB().Simulation()

    
    print ('done')
    
    