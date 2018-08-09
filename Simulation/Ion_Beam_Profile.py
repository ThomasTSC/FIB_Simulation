# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:40:03 2018

@author: thoma
"""

import Parameters
import numpy
import Grid_Structure
import Physical_Effect
import matplotlib.pyplot as plt

class Ion_Beam_Profile:
    
    def __init__(self, Profile, Beam_Position_X, Beam_Position_Y):
        self.Parameters = Parameters.Parameters()
        self.Profile = Profile
        self.Beam_Position_X = Beam_Position_X
        self.Beam_Position_Y = Beam_Position_Y 
    

    def primaryIonBeamProfile(self):
        
        
        Primary_Ion_Beam_Profile = self.Parameters['Ion_Flux']*numpy.exp(-(((self.Profile['Grid_X']-self.Beam_Position_X)**2+(self.Profile['Grid_Y']-self.Beam_Position_Y)**2)/(2*self.Parameters['Beam_Standard_Deviation']**2)))
        
        Pr_Normalized_Factor = 1/(numpy.sum(Primary_Ion_Beam_Profile)/self.Parameters['Ion_Flux'])
    
        Primary_Ion_Beam_Profile = {'Primary_Ion_Beam_Profile':Primary_Ion_Beam_Profile*Pr_Normalized_Factor}
    
        #print (Primary_Ion_Beam_Profile)
    
        return Primary_Ion_Beam_Profile
        
    
    def reDepositionTrajectury(self):
        
        Surface_Slope = Grid_Structure.Grid_Structure(self.Profile).surfaceSlope()
        
        Surface_Normal_Vector = [-numpy.interp(self.Beam_Position_X,self.Profile['Grid_X'], Surface_Slope['Surface_Slope']),1]
        
        Trajectury_Vector = [self.Profile['Grid_X']-self.Beam_Position_X, self.Profile['Grid_Z']-numpy.interp(self.Beam_Position_X,self.Profile['Grid_X'], self.Profile['Grid_Z'])]
        
        Trajectury_Cosine = (Surface_Normal_Vector[0]*Trajectury_Vector[0]+Surface_Normal_Vector[1]*Trajectury_Vector[1])/numpy.sqrt((numpy.power(Surface_Normal_Vector[0],2)+numpy.power(Surface_Normal_Vector[1],2))*(numpy.power(Trajectury_Vector[0],2)+numpy.power(Trajectury_Vector[1],2)))
        
        Trajectury_Angle = (180/numpy.pi)*numpy.arccos(Trajectury_Cosine)
        
        Redeposition_Trajectury = {'Trajectury_Cosine': Trajectury_Cosine, 'Trajectury_Angle':Trajectury_Angle}
        
        return Redeposition_Trajectury

    
    def reDepositionAngularDistribution(self):
    
        Redeposition_Trajectury = Ion_Beam_Profile(self.Profile, self.Beam_Position_X, self.Beam_Position_Y).reDepositionTrajectury()
        
        Redeposition_Angular_Distribution = (1/(2*numpy.pi))*(1+Redeposition_Trajectury['Trajectury_Cosine'])
        
        Redeposition_Angular_Distribution_Normalized_Factor = 1/(numpy.max(Redeposition_Angular_Distribution))
        
        Redeposition_Angular_Distribution = {'Redeposition_Angular_Distribution': Redeposition_Angular_Distribution*Redeposition_Angular_Distribution_Normalized_Factor}
        
        print (Redeposition_Angular_Distribution)
        
        #plt.figure()
        #plt.plot(self.Profile['Grid_X'],Redeposition_Angular_Distribution['Redeposition_Angular_Distribution'])
        #plt.show()
        
        
        return Redeposition_Angular_Distribution
    
    
    def redepositionShadowEffect(self):
        
        
        
        
        return None
    
    
    
    def reDepositionProfile(self):
        
        Grid_Area = Grid_Structure.Grid_Structure(self.Profile).gridArea()
        
        Primary_Sputtering_Depth = Physical_Effect.Physical_Effect(self.Profile).primarySputtering(self.Beam_Position_X, self.Beam_Position_Y)['Primary_Sputtering_Depth_Total']
        
        Redeposition_Amount_per_GridPoint = numpy.max(numpy.abs(Primary_Sputtering_Depth))*numpy.sum(Grid_Area['Grid_Area'])*self.Parameters['Atomic_density_Sub']
        
        #This is an overestimated amount#
        Redeposition_Amount_per_BeamPosition = Redeposition_Amount_per_GridPoint*((2*numpy.pi*self.Parameters['Beam_Radius'])/self.Parameters['Grid_Space_Y'])
        
        
    
        
        Re_Angular_Distribution =  Ion_Beam_Profile(self.Profile, self.Beam_Position_X, self.Beam_Position_Y).reDepositionAngularDistribution()
        
       
        
        Re_Deposition_Profile =  Redeposition_Amount_per_BeamPosition*Re_Angular_Distribution['Redeposition_Angular_Distribution']
        

        
        Re_Deposition_Profile = {'Re_Deposition_Profile':Re_Deposition_Profile}
        
        print (Re_Deposition_Profile)
        
        plt.figure()
        plt.plot(self.Profile['Grid_X'],Re_Deposition_Profile['Re_Deposition_Profile'])
        plt.show()
        
        #print (Re_Deposition_Profile)
        
        return Re_Deposition_Profile
    
    
    def secondaryIonBeamProfile(self):
        
        Primary_Sputtering_Depth = Physical_Effect.Physical_Effect(self.Profile).primarySputtering()['Primary_Sputtering_Depth_Total']
        
        Secondary_Ion_Beam_Profile = Primary_Sputtering_Depth
        
        Secondary_Ion_Beam_Profile = {'Secondary_Ion_Beam_Profile':Secondary_Ion_Beam_Profile}
        
        return Secondary_Ion_Beam_Profile
    
    
    
if __name__ == "__main__":
    
    import Simulator
    import Scanning_Strategy
    
    
    Profile = Simulator.FIB().Simulation()
    
    Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()
    
    #Pr = Ion_Beam_Profile(Profile, Scanning_Path['Scanning_Path_X'][0], Scanning_Path['Scanning_Path_Y'][0]).primaryIonBeamProfile()
    
    
    
    
    Re = Ion_Beam_Profile(Profile, Scanning_Path['Scanning_Path_X'][0], Scanning_Path['Scanning_Path_Y'][0]).reDepositionProfile()

    
    print ('done')
