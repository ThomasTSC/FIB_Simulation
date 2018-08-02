'''
Created on May 7, 2018

@author: thoma
'''


import Ion_Beam_Profile
import Scanning_Strategy
import Scanning_Strategy
import Grid_Structure
import numpy
import Parameters
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D





class Post_Process:
    '''
    classdocs
    '''


    def __init__(self):
        
        self.Parameters = Parameters.Parameters()
    
    
    
    def sputteringYieldPlot(self):
        
        
        
        
        return 0 

        
        
        
    def ionDoseAmount(self):    
    
        m2_to_cm2 = 10000

        Square_to_Circle = 1.27

        Dosed_Area = m2_to_cm2*Square_to_Circle*(self.Parameters['Pixel_Distance']*(self.Parameters['Step']-1)+(self.Parameters['Full_Pixel_Length']))*self.Parameters['Full_Pixel_Length']

        Ion_per_Beam =  self.Parameters['Ion_Flux']*self.Parameters['Dwell_Time']*self.Parameters['Pixel_Area'] #per second
        
        
        Ion_Dose_Accumulated = Ion_per_Beam*self.Parameters['Step']*self.Parameters['Pass']/(Dosed_Area)
        
       
        
        print ('Accumulated Ion dose (Ions/cm2):', Ion_Dose_Accumulated)

        return Ion_Dose_Accumulated
    
    
    def plotTrench(self,Profile):
    
        m_to_nm = 1e9
    
        plt.figure()
        plt.title('Simulated Trench')
        plt.xlabel('X-Cor (nm)')
        plt.xlim(0,1500)
        plt.ylabel('Z-Cor (nm)')
        plt.scatter(Profile['Grid_X']*m_to_nm,Profile['Grid_Z']*m_to_nm)
        
        Surface_Slope = Grid_Structure.Grid_Structure(Profile).surfaceSlope()
        plt.scatter(Profile['Grid_X']*m_to_nm,Surface_Slope['Surface_Slope'])
        plt.show()
        
        
        
    def saveProfile(self):
        
        return None
    
    
    
if __name__ == "__main__":
    
    Post_Process().countTotalPixel()
    Post_Process().ionDoseAmount()
    #Post_Process().plotTrench(Segment)
    
    print ('done')