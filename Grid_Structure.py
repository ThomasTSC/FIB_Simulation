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


from openpyxl.chart import surface_chart


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
                
    
    
    def initSegment(self, Grid):
        
        
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
        
        #Surface_Slope = {'Surface_Slope': Surface_Slope}
        
        #print(Surface_Slope)
        
        return Surface_Slope 
    
    
    
    def surfaceNormalVector(self, Segment):
        
        
        Surface_Slope = Grid_Structure.surfaceSlope(self, Segment)
        
        
        Surface_Normal_Vector = [-Surface_Slope, numpy.ones_like(Surface_Slope)]
        
        #Surface_Normal_Vector = {'Surface_Normal_Vector':Surface_Normal_Vector}
        
        return Surface_Normal_Vector
                
                
    def surfaceMovingVector(self,Segment):
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self,Segment)
        
        Surface_Moving_Vector = [ -x for x in Surface_Normal_Vector]
          
        #Surface_Moving_Vector = {'Surface_Moving_Vector':Surface_Moving_Vector}
        
        return Surface_Moving_Vector            
                
    
    def Incident_Vector(self,Segment):
        
        Surface_Slope = Grid_Structure.surfaceSlope(self,Segment)
        
        Incident_Vector = [numpy.zeros_like(Surface_Slope), numpy.ones_like(Surface_Slope)]
        
        return Incident_Vector
        
                
    def Incident_Cos(self,Segment):
        
        Incident_Vector = Grid_Structure.Incident_Vector(self,Segment)
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self,Segment)
        
        
        Incident_Cos = (Incident_Vector[0]*Surface_Normal_Vector[0]+Incident_Vector[1]*Surface_Normal_Vector[1])/(numpy.sqrt(numpy.square(Incident_Vector[0])+numpy.square(Incident_Vector[1]))*numpy.sqrt(numpy.square(Surface_Normal_Vector[0])+numpy.square(Surface_Normal_Vector[1])))
        
        
        return Incident_Cos
    
    
    def Incident_Angle(self,Segment):
        
        
        Incident_Cos = Grid_Structure.Incident_Cos(self,Segment)
        
        Incident_Angle = (180/numpy.pi)*(numpy.arccos(Incident_Cos))
        
        
        return Incident_Angle            
                
                
                
                
    def surfaceCalculation(self,Segment):
        
        

        Surface_Slope = Grid_Structure.surfaceSlope(self, Segment)

        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self,Segment)
        
        Surface_Moving_Vector = Grid_Structure.surfaceMovingVector(self,Segment)

        Incident_Vector = Grid_Structure.Incident_Vector(self,Segment)
        
        Incident_Cos = Grid_Structure.Incident_Cos(self,Segment)
        
        Incident_Angle = Grid_Structure.Incident_Angle(self,Segment)
        
        
        
        Surface = {'Surface_Normal_Vector':Surface_Normal_Vector,
                   'Surface_Moving_Vector':Surface_Moving_Vector, 
                   'Incident_Vector': Incident_Vector, 
                   'Incident_Cos':Incident_Cos}
        
        
        #print (Surface)
        
        return Surface
                    
    
    
    
    
    
    def gridArea(self,Segment):
        
        
        
        Grid_Length = numpy.sqrt(numpy.power((Segment['Segment_ZCor_End']-Segment['Segment_ZCor_Front']),2)+numpy.power((Segment['Segment_XCor_End']-Segment['Segment_XCor_Front']),2))
        Grid_Width = self.Parameters['Grid_Space']
        
        
        Grid_Area = Grid_Length*Grid_Width
        
        print(len(Grid_Area))

        
        return Grid_Area
    
    
           
    
    def Surface_Smoothing(self):
        
        
        
        Surface = {}
        
        
        return Surface
    
    
                
                
if __name__ == "__main__":
    
    import Simulator
    
    Segment = Simulator.FIB().Simulation()
    
    Grid_Structure().surfaceSlope(Segment)
    
    
    
    #Grid_Structure().gridArea()
    
    #Grid = Grid_Structure().initialGrid()
    
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
    
    
    