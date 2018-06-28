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
    
    
    
    def trenchPlot(self):
        
        
        
        
        
        return None
        
    
    def countTotalPixel(self):
        
        
        Total_Pixel_Number = self.Parameters['Pass']*self.Parameters['Step']
        
        print(Total_Pixel_Number)
        
        return Total_Pixel_Number
        
        
        
        
    def ionDoseAmount(self):    
    
        
    

        Ion_Dose_Amount = []

        return Ion_Dose_Amount
    
    
    
    
    
if __name__ == "__main__":
    
    
    
    
    Post_Process().countTotalPixel()
    
    print ('done')