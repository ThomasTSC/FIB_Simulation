'''
Created on 06.08.2018

@author: chou
'''

import Parameters
import Physical_Effect
import Scanning_Strategy
import numpy
import Grid_Structure
import Post_Process
cimport cython


cdef dict _Parameters = Parameters.Parameters()
cdef dict _Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()
cdef float Time_Interval
cdef int Pass, Step
cdef dict Profile
cdef list Beam_Position
cdef dict Primary_Sputtering




def initGrid():
        
        Grid_Point = _Parameters['Grid_Point']*_Parameters['Step']
        
        Grid_xlim_max = _Parameters['Full_Pixel_Length']*_Parameters['Step']
        
        Grid_X = numpy.linspace(0,_Parameters['Full_Pixel_Length']*_Parameters['Step'],Grid_Point)
        
        Grid_Space_X = numpy.diff(Grid_X)[0]
        
        Grid_Y = _Parameters['Beam_Radius']*numpy.ones_like(Grid_X)
        
        Grid_Z = numpy.zeros_like(Grid_X)
        

        
        initGrid_Structure = {'Grid_X': Grid_X, 
                                 'Grid_Y': Grid_Y,
                                 'Grid_Z': Grid_Z, 
                                 'Grid_xlim_max': Grid_xlim_max,
                                 'Grid_Space_X':Grid_Space_X                                
                                 }
        
        return initGrid_Structure     



def _Simulation():
    
    Profile = initGrid()
    
    for Pass in numpy.nditer(_Parameters['Pass']):
        
        for Step in range(len(_Scanning_Path['Scanning_Path_X'])):
            
            Time_Interval  = 0
            
            
            Profile['Grid_X'] = Grid_Structure.Grid_Structure(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_X_Resampling']
            Profile['Grid_Z'] = Grid_Structure.Grid_Structure(Profile).surfaceResampling(Profile['Grid_X'],Profile['Grid_Z'])['Grid_Z_Resampling']
            
            while Time_Interval <= _Parameters['Dwell_Time']:

                Beam_Position = [_Scanning_Path['Scanning_Path_X'][Step], _Scanning_Path['Scanning_Path_Y'][Step]]
                    
                Primary_Sputtering = Physical_Effect.Physical_Effect(Profile).primarySputtering(Beam_Position[0], Beam_Position[1])
                
                
                Profile['Grid_X'] = Profile['Grid_X'] + Primary_Sputtering['Primary_Sputtering_Depth_X']
                Profile['Grid_Z'] = Profile['Grid_Z'] + Primary_Sputtering['Primary_Sputtering_Depth_Z'] 

                Profile = {'Grid_X': Profile['Grid_X'], 'Grid_Y':Profile['Grid_Y'], 'Grid_Z':Profile['Grid_Z'], 'Grid_Space_X':Profile['Grid_Space_X'] } 

                Time_Interval = Time_Interval + _Parameters['Integration_Time']
                
                
    Profile['Grid_X'] = Profile['Grid_X']
    Profile['Grid_Z'] = Grid_Structure.Grid_Structure(Profile).smoothingTrench(Profile['Grid_Z'])['Smoothing_Grid_Z']           
    
    
    Post_Process.Post_Process().ionDoseAmount()
    Post_Process.Post_Process().plotTrench(Profile) 
    
                
    return Profile            





