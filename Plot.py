'''
Created on May 7, 2018

@author: thoma
'''


import Ion_Beam_Profile
import Scanning_Strategy
import Scanning_Strategy
import Grid_Structure
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D





class Plot:
    '''
    classdocs
    '''


    def __init__(self):
        self.Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()
        self.Grid_Structure = Grid_Structure.Grid_Structure().Grid()
    
    
    def Beam_Profile_Plot(self):
        

        
        Ion_Beam_Distribution = Ion_Beam_Profile.Ion_Beam_Profile().Ion_Beam_Profile(self.Scanning_Path['Scanning_Path_X'][0], self.Scanning_Path['Scanning_Path_Y'][0],self.Grid_Structure['Grid_X'],self.Grid_Structure['Grid_Y'])
        
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter3D(self.Grid_Structure['Grid_X'], self.Grid_Structure['Grid_Y'], Ion_Beam_Distribution['Ion_Beam_Profile']);
        plt.show()
        
        
        
        
        
if __name__ == "__main__":
    
    Plot().Beam_Profile_Plot()
    print ('done')