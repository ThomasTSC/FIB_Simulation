# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:32:27 2018

@author: thoma
"""
import Parameters
import numpy
import Simulator
import math




class Grid_Structure:
    
    def __init__(self,Profile):
        self.Parameters = Parameters.Parameters()
        self.Profile = Profile

    
    
    def surfaceSlope(self):
        
        
        Surface_Slope = numpy.diff(self.Profile['Grid_Z'])/numpy.diff(self.Profile['Grid_X'])
    
        Surface_Slope = 0.5*(Surface_Slope[0:-1]+Surface_Slope[1:])
        
        Surface_Slope = numpy.append(Surface_Slope,[0])
       
        Surface_Slope = numpy.insert(Surface_Slope,0,0)
        

        
        for element in range(len(Surface_Slope)):
            if math.isnan(Surface_Slope[element]) is True:
                Surface_Slope[element] = 0
        
        
        return Surface_Slope 
    
    
    
    def surfaceNormalVector(self):
        
        
        Surface_Slope = Grid_Structure.surfaceSlope(self)
        
        
        Surface_Normal_Vector = [-Surface_Slope, numpy.ones_like(Surface_Slope)]
        
        
        #print (Surface_Normal_Vector)
        
        return Surface_Normal_Vector
                
                
    def surfaceMovingVector(self):
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self)
        
        Surface_Moving_Vector = [ -x for x in Surface_Normal_Vector]
          
        
        return Surface_Moving_Vector            
                
    
    def incidentVector(self):
        
        Surface_Slope = Grid_Structure.surfaceSlope(self)
        
        Incident_Vector = [numpy.zeros_like(Surface_Slope), numpy.ones_like(Surface_Slope)]
        
        
        #print (Incident_Vector)
        
        return Incident_Vector
        
                
    def incidentCosine(self):
        
        Incident_Vector = Grid_Structure.incidentVector(self)
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self)
        
        Incident_Cos = (Incident_Vector[0]*Surface_Normal_Vector[0]+Incident_Vector[1]*Surface_Normal_Vector[1])/(numpy.sqrt(numpy.square(Incident_Vector[0])+numpy.square(Incident_Vector[1]))*numpy.sqrt(numpy.square(Surface_Normal_Vector[0])+numpy.square(Surface_Normal_Vector[1])))
        
        
        #print (Incident_Cos)
        
        return Incident_Cos
    
    
    def incidentAngle(self):
        
        Incident_Cos = Grid_Structure.incidentCosine(self)
        
        Incident_Angle = (180/numpy.pi)*(numpy.arccos(Incident_Cos.astype(float)))
        
        
        #print (Incident_Angle)
        
        return Incident_Angle            
                
                
    
    
    def gridArea(self):
        
        
        Grid_Length = numpy.sqrt(numpy.power(numpy.diff(self.Profile['Grid_Z']),2) + numpy.power(numpy.diff(self.Profile['Grid_X']),2))
        
        Grid_Length = 0.5*(Grid_Length[0:-1]+Grid_Length[1:])
        
        Grid_Length = numpy.append(Grid_Length,[self.Profile['Grid_Space_X']])
       
        Grid_Length = numpy.insert(Grid_Length,0,self.Profile['Grid_Space_X'])
        
        Grid_Width = self.Parameters['Grid_Space_Y']
        
        
        Grid_Area = Grid_Length*Grid_Width
        
        
        #print((Grid_Area))

        return Grid_Area

    
    

    def grid(self):
        
        Surface_Slope = Grid_Structure.surfaceSlope(self)
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self)
        
        Surface_Moving_Vector = Grid_Structure.surfaceMovingVector(self)
        
        Incident_Vector = Grid_Structure.incidentVector(self)
        
        Incident_Cosine = Grid_Structure.incidentCosine(self)
        
        Incident_Angle = Grid_Structure.incidentAngle(self)
        
        Grid_Area = Grid_Structure.gridArea(self)
        
        Grid = {'Surface_Slope': Surface_Slope,
                          'Surface_Normal_Vector': Surface_Normal_Vector,
                          'Surface_Moving_Vector': Surface_Moving_Vector,
                          'Incident_Vector': Incident_Vector,
                          'Incident_Cos': Incident_Cosine,
                          'Incident_Angle': Incident_Angle,
                          'Grid_Area': Grid_Area
                          
                          }
        
        print (Grid)
        
        return Grid
    
    

     
if __name__ == "__main__":
    
    
    import Simulator
    
    Profile = Simulator.FIB().Simulation()
    Grid_Structure(Profile).gridStructure()

    print ('done')
    
    
    