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


class Grid_Structure:
    
    def __init__(self):
        self.Parameters = Parameters.Parameters()

    
    def initialGrid(self):
        
        
        Grid_Point = self.Parameters['Grid_Point']*self.Parameters['Step']
        
        Grid_xlim_max = self.Parameters['Full_Pixel_Length']*self.Parameters['Step']
        
        Grid_X = numpy.linspace(0,self.Parameters['Full_Pixel_Length']*self.Parameters['Step'],Grid_Point)
        
        Grid_Y = self.Parameters['Beam_Radius']*numpy.ones_like(Grid_X)
        
        
        Grid_Z = numpy.zeros_like(Grid_X)

        
        initialGrid_Structure = {'Grid_X':Grid_X, 'Grid_Y':Grid_Y,'Grid_Z': Grid_Z, 'Grid_xlim_max':Grid_xlim_max}
        
             
             
        return initialGrid_Structure     
                
    
    
    def surfaceSlope(self):
        
        Grid = Simulator.FIB().Simulation()
        
        Surface_Slope = Grid['Grid_Z']/Grid['Grid_X']
        
        #Surface_Slope = {'Surface_Slope': Surface_Slope}
        
        return Surface_Slope 
    
    
    
    def surfaceNormalVector(self):
        
        Grid = Simulator.FIB().Simulation()
        
        Surface_Slope = Grid_Structure.surfaceSlope()
        
        for element in range(len(Surface_Slope)):
            if math.isnan(Surface_Slope[element]) is True:
                Surface_Slope[element] = 0
        
        Surface_Normal_Vector = [-Surface_Slope, numpy.ones_like(Surface_Slope)]
        
        #Surface_Normal_Vector = {'Surface_Normal_Vector':Surface_Normal_Vector}
        
        return Surface_Normal_Vector
                
                
    def surfaceMovingVector(self):
        
        Surface_Moving_Vector = [ -x for x in Surface_Normal_Vector]
          
        #Surface_Moving_Vector = {'Surface_Moving_Vector':Surface_Moving_Vector}
        
        return Surface_Moving_Vector            
                
    
    def Incident_Vector(self):
        
        Surface_Slope = Grid_Structure.surfaceSlope()
        
        Incident_Vector = [numpy.zeros_like(Surface_Slope), numpy.ones_like(Surface_Slope)]
        
        return Incident_Vector
        
                
    def Incident_Cos(self):
        
        Incident_Vector = Grid_Structure.Incident_Vector()
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector()
        
        
        Incident_Cos = (Incident_Vector[0]*Surface_Normal_Vector[0]+Incident_Vector[1]*Surface_Normal_Vector[1])/(numpy.sqrt(numpy.square(Incident_Vector[0])+numpy.square(Incident_Vector[1]))*numpy.sqrt(numpy.square(Surface_Normal_Vector[0])+numpy.square(Surface_Normal_Vector[1])))
        
        
        return Incident_Cos
    
    
    def Inciden_Angle(self):
        
        
        Incident_Cos = Grid_Structure.Incident_Cos()
        
        Incident_Angle = (180/numpy.pi)*(numpy.arccos(Incident_Cos))
        
        
        return Incident_Angle            
                
                
                
                
    def surfaceCalculation(self):
        
        Grid = Simulator.FIB().Simulation()
        

        Surface_Slope = Grid_Structure.surfaceSlope()

        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector()
        
        Surface_Moving_Vector = Grid_Structure.surfaceMovingVector()

        Incident_Vector = Grid_Structure.Incident_Vector()
        
        Incident_Cos = Grid_Structure.Incident_Cos()
        
        Incident_Angle = Grid_Structure.Inciden_Angle()
        
    
        
        Surface = {'Surface_Normal_Vector':Surface_Normal_Vector,'Surface_Moving_Vector':Surface_Moving_Vector, 'Incident_Vector': Incident_Vector, 'Incident_Cos':Incident_Cos}
        
        
        #print (Surface)
        
        return Surface
                    
    
    
    
    def gridArea(self):
        
        
        
        Grid_Area = []
        
        
        return Grid_Area
    
    
    
    
    
    
           
    
    def Surface_Smoothing(self):
        
        
        
        Surface = {}
        
        
        return Surface
    
    
                
                
if __name__ == "__main__":
    
    
    
    Surface_Structure = Grid_Structure().initialGrid()
    
    
    plt.figure()
    plt.title('Surface')
    plt.grid()
    #plt.xticks(Grid_Structure['Grid_X'])
    #plt.yticks(Grid_Structure['Grid_Z'])
    plt.scatter(Surface_Structure['Grid_X'], Surface_Structure['Grid_Z'], color="red", marker="x")
    
    plt.xlim(-3e-8,Surface_Structure['Grid_xlim_max']+3e-8)
    
    plt.show()
             
    Grid_Structure().surfaceCalculation()
    
    
    
    print ('done')
    
    
    