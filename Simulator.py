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



class FIB:
    '''
    classdocs
    '''

    def __init__(self):
        
        self.Parameters = Parameters.Parameters()
        
        self.Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()
        
        

    def __init__Grid(self):
        
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
        
        Profile = FIB().__init__Grid()

        
        
        
        for Pass in range(self.Parameters['Pass']):
        
            for Step in range(len(self.Scanning_Path['Scanning_Path_X'])):
                
                Time_Interval = 0
                

                
                
                while Time_Interval <= self.Parameters['Dwell_Time']:
                
                    Beam_Position = [self.Scanning_Path['Scanning_Path_X'][Step], self.Scanning_Path['Scanning_Path_Y'][Step]]
                    Primary_Ion_Beam = Ion_Beam_Profile.Ion_Beam_Profile(Profile).Primary_Ion_Beam_Profile(Beam_Position[0], Beam_Position[1],Profile_X,Profile_Y, Profile_Z)
                    #Primary_Sputtering = Physical_Effect.Physical_Effect(Profile).primarySputtering(Beam_Position[0], Beam_Position[1])
                
                
                
                    Profile = {'Grid_X': Profile['Grid_X'], 'Grid_Y':Profile['Grid_Y'], 'Grid_Z':Profile['Grid_Z']} 
            
            
                    
                
         
                
                    Time_Interval = Time_Interval + self.Parameters['Integration_Time']
            
            
        
                    
            #Post_Process.Post_Process().plotTrench(Profile)       
        
        
        return Profile
    
    
    
    
if __name__ == "__main__":
    
    Profile = FIB().Simulation()
    
    #print (Result)
    
    #m_to_nm = 1e9
    
    #plt.figure()
    #plt.xlim(0,1e-6)
    #plt.ylim(-1e-7,1e-7)
    #plt.title('Simulated Trench')
    #plt.scatter(Result['Segment_XCor_Front']*m_to_nm,Result['Segment_ZCor_Front']*m_to_nm)
    #plt.scatter(Result['Segment_XCor_End']*m_to_nm,Result['Segment_ZCor_End']*m_to_nm)
    #plt.scatter(Result['Segment_XCor']*m_to_nm,Result['Segment_ZCor']*m_to_nm)
    #plt.show()
    
    print ('done')
    
    