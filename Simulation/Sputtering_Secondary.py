'''
Created on Nov 11, 2018

@author: thoma
'''

import Parameters
import Grid_Structure
import numpy


class SecondarySputtering:
    '''
    classdocs
    '''


    def __init__(self,  Primary_Sputtering, Profile, Beam_Position_X, Beam_Position_Y):
        
        self.Physical_Parameters = Parameters.Physical_Parameters()
        self.Profile = Profile
        self.Grid_Structure = Grid_Structure.Grid_Structure(self.Profile).grid()
        self.Sputtering_Parameters = Parameters.Sputtering_Parameters()
        self.Beam_Position_X = Beam_Position_X
        self.Beam_Position_Y = Beam_Position_Y 
        self.Primary_Sputtering = Primary_Sputtering
        
        
        
        
        
    def sputteringYield(self):
    
        
        Sputtering_Yield = self.Sputtering_Parameters['Sputtering_Yield_1']*(numpy.power((1/self.Grid_Structure['Incident_Cos'].astype(float)),(self.Sputtering_Parameters['Sputtering_Yield_2'])))*(numpy.exp(-self.Sputtering_Parameters['Sputtering_Yield_3']*((1/self.Grid_Structure['Incident_Cos'].astype(float))-1)))
        
        
        Sputtering_Yield = {'Sputtering_Yield': Sputtering_Yield}
        
        #print ((Sputtering_Yield))
        
        return Sputtering_Yield
    