
import Ion_Beam_Profile
import Grid_Structure
import Physical_Effect
import Scanning_Strategy
import Parameters
import numpy



def Simulation(int Parameter_Pass, int Parameter_Step):
    
    
    
    
    
    for Pass in range(self.Parameters['Pass']):
            
            
            for Step in range(len(self.Scanning_Path['Scanning_Path_X'])):
                
                Time_Interval = 0
                

                Profile['Grid_X'] = Grid_Structure.Grid_Structure(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_X_Resampling']
                Profile['Grid_Z'] = Grid_Structure.Grid_Structure(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_Z_Resampling']
                                
                
                while Time_Interval <= self.Parameters['Dwell_Time']:
                
                    Beam_Position = [self.Scanning_Path['Scanning_Path_X'][Step], self.Scanning_Path['Scanning_Path_Y'][Step]]
                    
                    Primary_Sputtering = Physical_Effect.Physical_Effect(Profile).primarySputtering(Beam_Position[0], Beam_Position[1])
                
                
                    Profile['Grid_X'] = Profile['Grid_X'] + Primary_Sputtering['Primary_Sputtering_Depth_X']
                    Profile['Grid_Z'] = Profile['Grid_Z'] + Primary_Sputtering['Primary_Sputtering_Depth_Z'] 
                    
                
                    #Redeposition = Physical_Effect.Physical_Effect(Profile).primarySputtering(Beam_Position[0], Beam_Position[1])
                    
                    #Secondary_Sputtering = Physical_Effect.Physical_Effect(Profile).secondarySputtering(Beam_Position[0], Beam_Position[1])
                     
                
                    Profile = {'Grid_X': Profile['Grid_X'], 'Grid_Y':Profile['Grid_Y'], 'Grid_Z':Profile['Grid_Z'], 'Grid_Space_X':Profile['Grid_Space_X'] } 
        
                
                    Time_Interval = Time_Interval + self.Parameters['Integration_Time']
            
            
        
        Profile['Grid_X'] = Profile['Grid_X']
        Profile['Grid_Z'] = Grid_Structure.Grid_Structure(Profile).smoothingTrench(Profile['Grid_Z'])['Smoothing_Grid_Z']