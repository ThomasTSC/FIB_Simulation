# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:32:27 2018

@author: thoma
"""
import Parameters
import numpy
import matplotlib.pyplot as plt
import math
import scipy
import Simulator
from scipy.interpolate import spline

import re

import matplotlib.pyplot as plt



class Grid_Structure:
    
    def __init__(self):
        self.Parameters = Parameters.Parameters()

    
    def initialGrid(self):
        
        
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
                
    
    
    def initialSegment(self, Grid):
        
        
        Segment_XCor_Front = Grid['Grid_X'][0:-1]
        Segment_XCor_End = Grid['Grid_X'][1:]
        
        Segment_XCor = 0.5*(Segment_XCor_Front+Segment_XCor_End)
        
        
        Segment_ZCor_Front = Grid['Grid_Z'][0:-1]
        Segment_ZCor_End = Grid['Grid_Z'][1:]
        
        Segment_ZCor = 0.5*(Segment_ZCor_Front+Segment_ZCor_End)
        
        
        Segment_YCor = Grid['Grid_Y'][0]*numpy.ones_like(Segment_XCor)
        
        
        
        initSegment = {'Segment_XCor_Front':Segment_XCor_Front,
                   'Segment_XCor_End':Segment_XCor_End,
                   'Segment_ZCor_Front':Segment_ZCor_Front,
                   'Segment_ZCor_End':Segment_ZCor_End,
                   'Segment_XCor':Segment_XCor,
                   'Segment_ZCor':Segment_ZCor,
                   'Segment_YCor':Segment_YCor}
        
        
       
        
        return initSegment
    
    
    
    def surfaceSlope(self,Segment):
        
        
        Surface_Slope = (Segment['Segment_ZCor_End']-Segment['Segment_ZCor_Front'])/(Segment['Segment_XCor_End']-Segment['Segment_XCor_Front'])
        
        for element in range(len(Surface_Slope)):
            if math.isnan(Surface_Slope[element]) is True:
                Surface_Slope[element] = 0
        
        Surface_Slope = {'Surface_Slope': Surface_Slope}
        
        #print(Surface_Slope)
        
        return Surface_Slope 
    
    
    
    def surfaceNormalVector(self, Segment):
        
        
        Surface_Slope = Grid_Structure.surfaceSlope(self, Segment)
        
        
        Surface_Normal_Vector = [-Surface_Slope['Surface_Slope'], numpy.ones_like(Surface_Slope['Surface_Slope'])]
        
        #Surface_Normal_Vector = {'Surface_Normal_Vector':Surface_Normal_Vector}
        
        return Surface_Normal_Vector
                
                
    def surfaceMovingVector(self,Segment):
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self,Segment)
        
        Surface_Moving_Vector = [ -x for x in Surface_Normal_Vector]
          
        #Surface_Moving_Vector = {'Surface_Moving_Vector':Surface_Moving_Vector}
        
        return Surface_Moving_Vector            
                
    
    def Incident_Vector(self,Segment):
        
        Surface_Slope = Grid_Structure.surfaceSlope(self,Segment)
        
        Incident_Vector = [numpy.zeros_like(Surface_Slope), numpy.ones_like(Surface_Slope['Surface_Slope'])]
        
        return Incident_Vector
        
                
    def Incident_Cos(self,Segment):
        
        Incident_Vector = Grid_Structure.Incident_Vector(self,Segment)
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self,Segment)
        
        
        Incident_Cos = (Incident_Vector[0]*Surface_Normal_Vector[0]+Incident_Vector[1]*Surface_Normal_Vector[1])/(numpy.sqrt(numpy.square(Incident_Vector[0])+numpy.square(Incident_Vector[1]))*numpy.sqrt(numpy.square(Surface_Normal_Vector[0])+numpy.square(Surface_Normal_Vector[1])))
        
        Incident_Cos = {'Incident_Cos':Incident_Cos}
        
        #print (Incident_Cos)
        
        return Incident_Cos
    
    
    def Incident_Angle(self,Segment):
        
        
        Incident_Cos = Grid_Structure.Incident_Cos(self,Segment)
        
        #print(Incident_Cos)
        
        Incident_Angle = (180/numpy.pi)*(numpy.arccos(Incident_Cos['Incident_Cos'].astype(float)))
        
        
        Incident_Angle ={'Incident_Angle':Incident_Angle}
        
        #print (Incident_Angle)
        
        return Incident_Angle            
                
                
    
    
    def gridArea(self,Segment):
        
        
        
        Grid_Length = numpy.sqrt(numpy.power((Segment['Segment_ZCor_End']-Segment['Segment_ZCor_Front']),2)+numpy.power((Segment['Segment_XCor_End']-Segment['Segment_XCor_Front']),2))
        Grid_Width = self.Parameters['Grid_Space']
        
        
        Grid_Area = Grid_Length*Grid_Width
        
        Grid_Area ={'Grid_Area': Grid_Area}
        
        #print((Grid_Area))

        return Grid_Area
    
    
    
    def Surface_Smoothing(self,Segment):
    
        Initial_Grid = Grid_Structure().initialGrid()
        
        Initial_Segment_X = Grid_Structure().initialSegment(Initial_Grid)
        
        
        Segment_Z_interp_Front = spline(Segment['Segment_XCor_Front'], Segment['Segment_ZCor_Front'], Initial_Segment_X['Segment_XCor_Front'], order=0)
        Segment_Z_interp_End = spline(Segment['Segment_XCor_End'], Segment['Segment_ZCor_End'], Initial_Segment_X['Segment_XCor_End'], order=0)
        Segment_Z_interp_Mid = 0.5*(Segment_Z_interp_Front+Segment_Z_interp_End)
        
        Segment_X_interp_Front = Initial_Segment_X['Segment_XCor_Front']
        Segment_X_interp_End = Initial_Segment_X['Segment_XCor_End']
        Segment_X_interp_Mid = 0.5*(Segment_X_interp_Front+Segment_X_interp_End)
        
        
        
        Surface_Smoothing = {'Segment_XCor_Front': Segment_X_interp_Front,
                      'Segment_XCor_End': Segment_X_interp_End,
                      'Segment_XCor': Segment_X_interp_Mid,
                      'Segment_ZCor': Segment_Z_interp_Mid,
                      'Segment_ZCor_Front': Segment_Z_interp_Front,
                      'Segment_ZCor_End': Segment_Z_interp_End ,
                    }
        
        
        
        return Surface_Smoothing 
    

    
    def findSingular_Point(self, Segment):
        
        Surface_Slope = Grid_Structure.surfaceSlope(self, Segment)
    
  
        Singular_Point = []
    
        for i in range(1,len(Surface_Slope['Surface_Slope'])-1):
            
            
            if Surface_Slope['Surface_Slope'][i]*Surface_Slope['Surface_Slope'][i-1]<0 or Surface_Slope['Surface_Slope'][i]*Surface_Slope['Surface_Slope'][i+1]<0:
                
                Singular_Point.append(i-1)
        
        
        Singular_Point = {'Singular_Point':Singular_Point}
        
        return Singular_Point
    
    
    
    def convolution_Smoothing(self,Segment):
        
        Singular_Point = Grid_Structure.findSingular_Point(self, Segment)
        
        Surface_Smoothing = Grid_Structure.Surface_Smoothing(self, Segment)
        
        
        for i in range(len(Singular_Point['Singular_Point'])):
            Adjacent_Point = [Singular_Point['Singular_Point'][i]-1,Singular_Point['Singular_Point'][i],Singular_Point['Singular_Point'][i]+1]

            #print (Adjacent_Point)
            
            Convolution_Smoothing_X_Front = numpy.convolve(Surface_Smoothing['Segment_XCor_Front'][Adjacent_Point], numpy.ones(len(Adjacent_Point))*(1/len(Adjacent_Point)), 'valid')
            Convolution_Smoothing_X_End = numpy.convolve(Surface_Smoothing['Segment_XCor_End'][Adjacent_Point], numpy.ones(len(Adjacent_Point))*(1/len(Adjacent_Point)), 'valid')
            Convolution_Smoothing_Z_Front = numpy.convolve(Surface_Smoothing['Segment_ZCor_Front'][Adjacent_Point], numpy.ones(len(Adjacent_Point))*(1/len(Adjacent_Point)), 'valid')
            Convolution_Smoothing_Z_End = numpy.convolve(Surface_Smoothing['Segment_ZCor_End'][Adjacent_Point], numpy.ones(len(Adjacent_Point))*(1/len(Adjacent_Point)), 'valid')
            
            

            
            #print(Convolution_Smoothing_X_Front)
            
            Surface_Smoothing['Segment_XCor_Front'][Adjacent_Point]= 3*[Convolution_Smoothing_X_Front]
            Surface_Smoothing['Segment_XCor_End'][Adjacent_Point]= 3*[Convolution_Smoothing_X_End]
            Surface_Smoothing['Segment_ZCor_Front'][Adjacent_Point]= 3*[Convolution_Smoothing_Z_Front]
            Surface_Smoothing['Segment_ZCor_End'][Adjacent_Point]= 3*[Convolution_Smoothing_Z_Front]
            
            
            
 
            
        
        
        Convolution_Smoothing = {'Segment_XCor_Front': Surface_Smoothing['Segment_XCor_Front'],
                      'Segment_XCor_End': Surface_Smoothing['Segment_XCor_End'],
                      'Segment_XCor': 0.5*(Surface_Smoothing['Segment_XCor_Front']+Surface_Smoothing['Segment_XCor_End']),
                      'Segment_ZCor': 0.5*(Surface_Smoothing['Segment_ZCor_Front']+Surface_Smoothing['Segment_ZCor_End']),
                      'Segment_ZCor_Front': Surface_Smoothing['Segment_ZCor_Front'],
                      'Segment_ZCor_End': Surface_Smoothing['Segment_ZCor_End'] ,
                    }
        
        
        print (Convolution_Smoothing)
        
        return Convolution_Smoothing
    
    
    
                
                
if __name__ == "__main__":
    
    import Simulator
    
    Segment = Simulator.FIB().Simulation()
    
    #Grid_Structure().surfaceSlope(Segment)
    

    
    #Grid_Structure().gridArea(Segment)
    
    
    
    #Grid = Grid_Structure().initialGrid()

    
    #Grid_Structure().findSingular_Point(Segment)
    Grid_Structure().convolution_Smoothing(Segment)
    #Grid_Structure().Segment(Grid)
     
    
    
    #plt.figure()
    #plt.title('Surface')
   # plt.grid()
    #plt.xticks(Grid_Structure['Grid_X'])
    #plt.yticks(Grid_Structure['Grid_Z'])
    #plt.scatter(Surface_Structure['Grid_X'], Surface_Structure['Grid_Z'], color="red", marker="x")
    
    #plt.xlim(-3e-8,Surface_Structure['Grid_xlim_max']+3e-8)
    
    #plt.show()
             
    #Grid_Structure().surfaceCalculation()
    
    
    
    print ('done')
    
    
    