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
    
    
    def plotTrench(self,Segment):
    
    
        m_to_nm = 1e9
    
        plt.figure()
        #plt.xlim(0,1e-6)
        #plt.ylim(-1e-7,1e-7)
        plt.title('Simulated Trench')
        plt.scatter(Segment['Segment_XCor_Front']*m_to_nm,Segment['Segment_ZCor_Front']*m_to_nm)
        plt.scatter(Segment['Segment_XCor_End']*m_to_nm,Segment['Segment_ZCor_End']*m_to_nm)
        plt.scatter(Segment['Segment_XCor']*m_to_nm,Segment['Segment_ZCor']*m_to_nm)
        plt.show()
    
    
    
    
if __name__ == "__main__":
    
    
    
    
    Post_Process().countTotalPixel()
    Post_Process().ionDoseAmount()
    Post_Process().plotTrench(Segment)
    
    print ('done')