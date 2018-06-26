'''
Created on 15.05.2018

@author: chou
'''


import Ion_Beam_Profile
import Grid_Structure
import Physical_Effect
import Scanning_Strategy
import matplotlib.pyplot as plt



class FIB:
    '''
    classdocs
    '''


    def __init__(self):
        
        self.Grid_X = Grid_Structure.Grid_Structure().initialGrid()['Grid_X']
        self.Grid_Y = Grid_Structure.Grid_Structure().initialGrid()['Grid_Y']
        self.Grid_Z = Grid_Structure.Grid_Structure().initialGrid()['Grid_Z']
        
        
        self.Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()



    def Simulation(self):
        
        
        
        for Step in range(len(self.Scanning_Path['Scanning_Path_X'])):
            Beam_Position = [self.Scanning_Path['Scanning_Path_X'][Step], self.Scanning_Path['Scanning_Path_Y'][Step]]
            Primary_Ion_Beam = Ion_Beam_Profile.Ion_Beam_Profile().Primary_Ion_Beam_Profile(Beam_Position[0], Beam_Position[1])
            plt.figure()
            plt.plot(self.Grid_X,Primary_Ion_Beam)
            #plt.show()
            
            
        Result = {'Grid_X': self.Grid_X,
                  'Grid_Y': self.Grid_Y,
                  'Grid_Z': self.Grid_Z,
                  'Beam_Position':Beam_Position}
        
        return Result
    
    
    
    
if __name__ == "__main__":
    
    FIB().Simulation()
    
    print ('done')
    
    