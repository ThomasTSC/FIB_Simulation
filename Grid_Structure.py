# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:32:27 2018

@author: thoma
"""
import Parameters
import numpy
import matplotlib.pyplot as plt
import math

import Simulator
from scipy.interpolate import spline

import re

import matplotlib.pyplot as plt



class Grid_Structure:
    
    def __init__(self,Profile):
        self.Parameters = Parameters.Parameters()
        self.Profile = Profile

    
    
    def surfaceSlope(self):
        
        
        Surface_Slope = numpy.diff(self.Profile['Grid_Z'])/numpy.diff(self.Profile['Grid_X'])
        
        
        
        Surface_Slope = numpy.append(Surface_Slope,[0])
        
        Surface_Slope[0] = 0
        
        for element in range(len(Surface_Slope)):
            if math.isnan(Surface_Slope[element]) is True:
                Surface_Slope[element] = 0
        
        Surface_Slope = {'Surface_Slope': Surface_Slope}
        
        #print(Surface_Slope)
        
        return Surface_Slope 
    
    
    
    def surfaceNormalVector(self):
        
        
        Surface_Slope = Grid_Structure.surfaceSlope(self)
        
        
        Surface_Normal_Vector = [-Surface_Slope['Surface_Slope'], numpy.ones_like(Surface_Slope['Surface_Slope'])]
        
        Surface_Normal_Vector = {'Surface_Normal_Vector':Surface_Normal_Vector}
        
        #print (Surface_Normal_Vector)
        
        return Surface_Normal_Vector
                
                
    def surfaceMovingVector(self):
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self)
        
        Surface_Moving_Vector = [ -x for x in Surface_Normal_Vector['Surface_Normal_Vector']]
          
        Surface_Moving_Vector = {'Surface_Moving_Vector':Surface_Moving_Vector}
        
        return Surface_Moving_Vector            
                
    
    def incidentVector(self):
        
        Surface_Slope = Grid_Structure.surfaceSlope(self)
        
        Incident_Vector = [numpy.zeros_like(Surface_Slope['Surface_Slope']), numpy.ones_like(Surface_Slope['Surface_Slope'])]
        
        Incident_Vector = {'Incident_Vector':Incident_Vector}
        
        #print (Incident_Vector)
        
        return Incident_Vector
        
                
    def incidentCosine(self):
        
        Incident_Vector = Grid_Structure.incidentVector(self)
        
        Surface_Normal_Vector = Grid_Structure.surfaceNormalVector(self)
        
        Incident_Cos = (Incident_Vector['Incident_Vector'][0]*Surface_Normal_Vector['Surface_Normal_Vector'][0]+Incident_Vector['Incident_Vector'][1]*Surface_Normal_Vector['Surface_Normal_Vector'][1])/(numpy.sqrt(numpy.square(Incident_Vector['Incident_Vector'][0])+numpy.square(Incident_Vector['Incident_Vector'][1]))*numpy.sqrt(numpy.square(Surface_Normal_Vector['Surface_Normal_Vector'][0])+numpy.square(Surface_Normal_Vector['Surface_Normal_Vector'][1])))
        
        Incident_Cos = {'Incident_Cos':Incident_Cos}
        
        #print (Incident_Cos)
        
        return Incident_Cos
    
    
    def incidentAngle(self):
        
        
        Incident_Cos = Grid_Structure.incidentCosine(self)
        
        Incident_Angle = (180/numpy.pi)*(numpy.arccos(Incident_Cos['Incident_Cos'].astype(float)))
        
        
        Incident_Angle ={'Incident_Angle':Incident_Angle}
        
        #print (Incident_Angle)
        
        return Incident_Angle            
                
                
    
    
    def gridArea(self):
        
        
        
        Grid_Length = numpy.sqrt(numpy.power((Segment['Segment_ZCor_End']-Segment['Segment_ZCor_Front']),2)+numpy.power((Segment['Segment_XCor_End']-Segment['Segment_XCor_Front']),2))
        Grid_Width = self.Parameters['Grid_Space']
        
        
        Grid_Area = Grid_Length*Grid_Width
        
        Grid_Area ={'Grid_Area': Grid_Area}
        
        #print((Grid_Area))

        return Grid_Area
    
    
    
    def surfaceResampling(self):
    
        Initial_Grid = Grid_Structure().initialGrid()
        
        
        
        Segment_Z_Resampling = spline(Segment['Segment_XCor_Front'], Segment['Segment_ZCor_Front'], Initial_Segment_X['Segment_XCor_Front'], order=2)
        
    
        Segment_X_Resampling= Initial_Segment_X['Segment_XCor_End']

        
        
        
        Surface_Resampling = {'Segment_Z_Resampling': Segment_Z_Resampling,
                    }
        
        
        
        return Surface_Resampling
    

    
    def findSingularPoint(self):
        
        Surface_Slope = Grid_Structure.surfaceSlope(self)
    
        
  
        Singular_Point = []
    
        for i in range(1,len(Surface_Slope['Surface_Slope'])-1):
            
            
            if Surface_Slope['Surface_Slope'][i]>0 and Surface_Slope['Surface_Slope'][i+1]<0:
                
                Singular_Point.append(i)
        
        
        Singular_Point = {'Singular_Point':Singular_Point}
        
        return Singular_Point
    
    
    
    def averageSmoothing(self,Segment,Segment_ZCor_Front, Segment_ZCor_End,Segment_XCor_Front, Segment_XCor_End):
        
        Singular_Point = Grid_Structure.findSingularPoint(self, Segment)
        
        

        for point in Singular_Point['Singular_Point']:
            
            Near_points = [point-2,point-1 ,point , point+1,point+2]
            
            Average_Surface_ZCor_Front = (1/5)*numpy.sum(Segment_ZCor_Front[Near_points])*numpy.ones(5) 
            
            Segment_ZCor_Front[Near_points] = Average_Surface_ZCor_Front[0]
            
            
            Average_Surface_ZCor_End = (1/5)*numpy.sum(Segment_ZCor_End[Near_points])*numpy.ones(5) 
            
            Segment_ZCor_End[Near_points] = Average_Surface_ZCor_End[0]
            
            
            Average_Surface_XCor_Front = (1/5)*numpy.sum(Segment_XCor_Front[Near_points])*numpy.ones(5) 
            
            Segment_XCor_Front[Near_points] = Average_Surface_XCor_Front[0]
            
            
            Average_Surface_XCor_End = (1/5)*numpy.sum(Segment_XCor_End[Near_points])*numpy.ones(5) 
            
            Segment_XCor_End[Near_points] = Average_Surface_XCor_End[0]            
            
                
        
        Average_Smoothing = {
                      
                      'Segment_ZCor_Front': Segment_ZCor_Front,
                      'Segment_ZCor_End': Segment_ZCor_End ,
                      'Segment_XCor_Front': Segment_XCor_Front,
                      'Segment_XCor_End': Segment_XCor_End
                    }
        

        
        
        #print (Average_Smoothing)
        
        return Average_Smoothing
    
    
    
                
                
if __name__ == "__main__":
    
    import Simulator
    
    Profile = Simulator.FIB().Simulation()

    
    Surface_Slope = Grid_Structure(Profile).surfaceSlope()
    
    Surface_NormalVector = Grid_Structure(Profile).surfaceNormalVector()

    Incident_Angle = Grid_Structure(Profile).incidentAngle()
    
    print ('done')
    
    
    