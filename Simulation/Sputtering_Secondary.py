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
    
    
    
    def scattedIonTrajectury(self):
        
        
        Trajectury_Vector = [self.Profile['Grid_X']-self.Beam_Position_X, self.Profile['Grid_Z']-numpy.interp(self.Beam_Position_X,self.Profile['Grid_X'], self.Profile['Grid_Z'])]
        
        Trajectury_Cosine = (self.Grid_Structure['Surface_Normal_Vector'][0]*Trajectury_Vector[0]+self.Grid_Structure['Surface_Normal_Vector'][1]*Trajectury_Vector[1])/numpy.sqrt((numpy.power(self.Grid_Structure['Surface_Normal_Vector'][0],2)+numpy.power(self.Grid_Structure['Surface_Normal_Vector'][1],2))*(numpy.power(Trajectury_Vector[0],2)+numpy.power(Trajectury_Vector[1],2)))
        
        Trajectury_Cosine[Trajectury_Cosine < 0] = 0
        
        Trajectury_Angle = (180/numpy.pi)*numpy.arccos(Trajectury_Cosine)+90
        
        Trajectury_Radian = (numpy.pi/180)*Trajectury_Angle
        
        Scattered_Ion_Trajectury = {'Trajectury_Cosine': Trajectury_Cosine, 'Trajectury_Angle':Trajectury_Angle, 'Trajectury_Radian':Trajectury_Radian}
        
        #print (Redeposition_Trajectury)
        
        return Scattered_Ion_Trajectury 
    
    
    
    
    
    
    
    
        
    def secondaryIonBeamProfile(self):
        
        
        Secondary_Ion_Beam_Profile = self.Physical_Parameters['Ion_Flux']*numpy.exp(-(((self.Profile['Grid_X']-self.Beam_Position_X)**2+(self.Profile['Grid_Y']-self.Beam_Position_Y)**2)/(2*self.Physical_Parameters['Beam_Standard_Deviation']**2)))
        
        Pr_Normalized_Factor = 1/(numpy.sum(Secondary_Ion_Beam_Profile)/self.Physical_Parameters['Ion_Flux'])
    
        Secondary_Ion_Beam_Profile = {'Secondary_Ion_Beam_Profile':Secondary_Ion_Beam_Profile*Pr_Normalized_Factor}
    
        #print (Secondary_Ion_Beam_Profile)
    
        return Secondary_Ion_Beam_Profile    
        
        
        
    def sputteringYield(self):
    
        
        Sputtering_Yield = self.Sputtering_Parameters['Sputtering_Yield_1']*(numpy.power((1/self.Grid_Structure['Incident_Cos'].astype(float)),(self.Sputtering_Parameters['Sputtering_Yield_2'])))*(numpy.exp(-self.Sputtering_Parameters['Sputtering_Yield_3']*((1/self.Grid_Structure['Incident_Cos'].astype(float))-1)))
        
        
        Sputtering_Yield = {'Sputtering_Yield': Sputtering_Yield}
        
        #print ((Sputtering_Yield))
        
        return Sputtering_Yield
    