'''
Created on 15.05.2018

@author: chou
'''


import Ion_Beam_Profile
import Grid_Structure
import Physical_Effect
import Scanning_Strategy
import matplotlib.pyplot as plt
import Parameters
import Post_Process
import numpy
from scipy.signal import savgol_filter


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
        
        Grid_Y = self.Parameters['Beam_Radius']*numpy.ones_like(Grid_X)
        
        Grid_Z = numpy.zeros_like(Grid_X)
        
        #print (Grid_X, Grid_Y, Grid_Z)
        
        initGrid_Structure = {'Grid_X': Grid_X, 
                                 'Grid_Y': Grid_Y,
                                 'Grid_Z': Grid_Z, 
                                 'Grid_xlim_max': Grid_xlim_max
                                 }
        
        return initGrid_Structure     


    def Simulation(self):
        
        Profile = FIB().initGrid()

        
        
        
        for Pass in range(self.Parameters['Pass']):
            
            
            
            for Step in range(len(self.Scanning_Path['Scanning_Path_X'])):
                
                Time_Interval = 0
                

                Profile['Grid_X'] = Grid_Structure.Grid_Structure(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_X_Resampling']
                Profile['Grid_Z'] = Grid_Structure.Grid_Structure(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_Z_Resampling']
                
                while Time_Interval <= self.Parameters['Dwell_Time']:
                
                    Beam_Position = [self.Scanning_Path['Scanning_Path_X'][Step], self.Scanning_Path['Scanning_Path_Y'][Step]]
                    Primary_Ion_Beam = Ion_Beam_Profile.Ion_Beam_Profile(Profile).Primary_Ion_Beam_Profile(Beam_Position[0], Beam_Position[1])
                    Primary_Sputtering = Physical_Effect.Physical_Effect(Profile).primarySputtering(Beam_Position[0], Beam_Position[1])
                
                
                    Profile['Grid_X'] = Profile['Grid_X'] + Primary_Sputtering['Primary_Sputtering_Depth_X']
                    Profile['Grid_Z'] = Profile['Grid_Z'] + Primary_Sputtering['Primary_Sputtering_Depth_Z'] 
                    
                    
                    
                    
                    Profile = {'Grid_X': Profile['Grid_X'], 'Grid_Y':Profile['Grid_Y'], 'Grid_Z':Profile['Grid_Z']} 
            
            
                    
                
         
                
                    Time_Interval = Time_Interval + self.Parameters['Integration_Time']
            
            
        
                    
            #Post_Process.Post_Process().plotTrench(Profile)       
        
        
        
                    
        return Profile
    
    
    
    
if __name__ == "__main__":
    
    import Grid_Structure
    
    Profile = FIB().Simulation()
    
    print (Profile)
    
    m_to_nm = 1e9
    
    plt.figure()
    #plt.xlim(0,1e-6)
    #plt.ylim(-1e-7,1e-7)
    plt.title('Simulated Trench')
    plt.scatter(Profile['Grid_X']*m_to_nm,Profile['Grid_Z']*m_to_nm)
    
    Surface_Slope = Grid_Structure.Grid_Structure(Profile).surfaceSlope()
    plt.scatter(Profile['Grid_X']*m_to_nm,Surface_Slope['Surface_Slope'])
    plt.show()
    
    print ('done')
    
    