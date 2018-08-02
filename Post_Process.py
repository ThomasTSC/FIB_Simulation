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


        
    
    def countTotalPixel(self):
        
        
        Total_Pixel_Number = self.Parameters['Pass']*self.Parameters['Step']
        
        print(Total_Pixel_Number)
        
        return Total_Pixel_Number
        
        
        
        
    def ionDoseAmount(self):    
    
        m2_to_cm2 = 10000
        
        Total_Pixel_Number = Post_Process.countTotalPixel(self)
        
        IonDose_per_Second = self.Parameters['Pixel_Area']*self.Parameters['Ion_Flux']*self.Parameters['Unit_Charge']/1e-12
    

        Ion_Dose_Amount = IonDose_per_Second*Total_Pixel_Number*m2_to_cm2*1e-6
        
        print ('Ion Dose (ion/cm2):', Ion_Dose_Amount)

        return Ion_Dose_Amount
    
    
    def plotTrench(self,Profile):
    
        m_to_nm = 1e9
    
        plt.figure()
        plt.title('Simulated Trench')
        plt.xlabel('X-Cor (nm)')
        plt.xlim(0,1e-7)
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
    Post_Process().plotTrench(Segment)
    
    print ('done')