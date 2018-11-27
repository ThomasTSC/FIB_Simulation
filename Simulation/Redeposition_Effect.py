'''
Created on Oct 12, 2018

@author: thoma
'''


import Parameters
import Grid_Structure
import numpy

import matplotlib.pyplot as plt



class Redeposition:
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
        
        
    
    def referenceCosineDistribution(self):

        Ref_Radian_Range = numpy.linspace(-numpy.pi,numpy.pi,len(self.Profile['Grid_X']))
    
        Ref_Cosine_Distribution = (1/(2*numpy.pi))*(1+numpy.cos(Ref_Radian_Range))
        

        Ref_Cosine_Distribution = {'Ref_Cosine_Distribution': Ref_Cosine_Distribution}
    
        #print (Ref_Cosine_Distribution )
    
        return Ref_Cosine_Distribution
    
    
    def reDepositionTrajectury(self):
        
        
        Trajectury_Vector = [self.Profile['Grid_X']-self.Beam_Position_X, self.Profile['Grid_Z']-numpy.interp(self.Beam_Position_X,self.Profile['Grid_X'], self.Profile['Grid_Z'])]
        
        Trajectury_Cosine = (self.Grid_Structure['Surface_Normal_Vector'][0]*Trajectury_Vector[0]+self.Grid_Structure['Surface_Normal_Vector'][1]*Trajectury_Vector[1])/numpy.sqrt((numpy.power(self.Grid_Structure['Surface_Normal_Vector'][0],2)+numpy.power(self.Grid_Structure['Surface_Normal_Vector'][1],2))*(numpy.power(Trajectury_Vector[0],2)+numpy.power(Trajectury_Vector[1],2)))
        
        Trajectury_Cosine[Trajectury_Cosine < 0] = 0
        
        Trajectury_Angle = (180/numpy.pi)*numpy.arccos(Trajectury_Cosine)+90
        
        Trajectury_Radian = (numpy.pi/180)*Trajectury_Angle
        
        Redeposition_Trajectury = {'Trajectury_Cosine': Trajectury_Cosine, 'Trajectury_Angle':Trajectury_Angle, 'Trajectury_Radian':Trajectury_Radian}
        
        #print (Redeposition_Trajectury)
        
        return Redeposition_Trajectury

    
    def reDepositionAngularDistribution(self):
    
        Redeposition_Trajectury = Redeposition.reDepositionTrajectury(self)
        
        Redeposition_Angular_Distribution = (1/(2*numpy.pi))*(1+numpy.cos(Redeposition_Trajectury['Trajectury_Radian']))

        Ref_Cosine_Distribution = Redeposition.referenceCosineDistribution(self)
    
        
        
        Area_Redeposition_Angular = numpy.trapz(Redeposition_Angular_Distribution, dx=self.Physical_Parameters['Grid_Space_Y'])
        Area_Redeposition_Reference = numpy.trapz(Ref_Cosine_Distribution['Ref_Cosine_Distribution'] , dx=self.Physical_Parameters['Grid_Space_Y'])
        
        print("Angualr =", Area_Redeposition_Angular)
        
        print ("Ref =", Area_Redeposition_Reference)
        
        
        #plt.figure()
        #plt.plot(self.Profile['Grid_X'],Ref_Cosine_Distribution['Ref_Cosine_Distribution']/(max(Ref_Cosine_Distribution['Ref_Cosine_Distribution'])))
        #plt.plot(self.Profile['Grid_X'],Redeposition_Angular_Distribution/max(Redeposition_Angular_Distribution))
        #plt.show()
        
        
        Redeposition_Angular_Distribution = {'Redeposition_Angular_Distribution':Redeposition_Angular_Distribution,
                                             'Normalized': Area_Redeposition_Angular/Area_Redeposition_Reference}
        
        
        return Redeposition_Angular_Distribution
    
    
    def redepositionShadowEffect(self):
        
        
        
        
        return None
    
    
    
    def reDepositionProfile(self):
        
        
        Primary_Sputtering_Depth = self.Primary_Sputtering['Primary_Sputtering_Depth_Total']
        
        Redeposition_Amount_per_GridPoint = numpy.max(numpy.abs(Primary_Sputtering_Depth))*numpy.sum(self.Grid_Structure['Grid_Area'])*self.Physical_Parameters['Atomic_density_Sub']
        
        #This is an overestimated amount#
        Redeposition_Amount_per_BeamPosition = Redeposition_Amount_per_GridPoint*((2*numpy.pi*self.Physical_Parameters['Beam_Radius'])/self.Physical_Parameters['Grid_Space_Y'])
        
        
        Re_Angular_Distribution =  Redeposition.reDepositionAngularDistribution(self)
        
        Re_Deposition_Profile =  Redeposition_Amount_per_BeamPosition*(Re_Angular_Distribution['Redeposition_Angular_Distribution']/max(Re_Angular_Distribution['Redeposition_Angular_Distribution']))

        
        
        Re_Deposition_Profile = {'Re_Deposition_Profile':Re_Deposition_Profile*Re_Angular_Distribution['Normalized']}
        
        
        
        #plt.figure()
        #plt.plot(self.Profile['Grid_X'],Re_Deposition_Profile['Re_Deposition_Profile'])
        #plt.show()
        
        print (Re_Deposition_Profile)
        
        return Re_Deposition_Profile
    
    
    
    
    
    def reDeposition(self):

       
        
        Redeposition_Ion_Beam = Redeposition.reDepositionProfile(self)
        
        
        Surface_Moving_Vector_X = (self.Grid_Structure['Surface_Moving_Vector'][0]/numpy.sqrt(numpy.power(self.Grid_Structure['Surface_Moving_Vector'][0],2) + numpy.power(self.Grid_Structure['Surface_Moving_Vector'][1],2)))
        Surface_Moving_Vector_Z = (self.Grid_Structure['Surface_Moving_Vector'][1]/numpy.sqrt(numpy.power(self.Grid_Structure['Surface_Moving_Vector'][0],2) + numpy.power(self.Grid_Structure['Surface_Moving_Vector'][1],2)))
        
        
        Redeposition_Total = -(1/self.Physical_Parameters['Atomic_density_Sub'])*(Redeposition_Ion_Beam['Re_Deposition_Profile']/self.Grid_Structure['Grid_Area'])*((self.Physical_Parameters['Grid_Space_Y']/(2*numpy.pi*self.Physical_Parameters['Beam_Radius'])))
        
        
        Redeposition_X = Redeposition_Total*Surface_Moving_Vector_X
        
        Redeposition_Z = Redeposition_Total*Surface_Moving_Vector_Z
        
        
        Redeposition_Depth = {'Redeposition_X':Redeposition_X, 
                        'Redeposition_Z':Redeposition_Z,
                        'Redeposition_Total':Redeposition_Total
                        }
        
        
        
        
        print (Redeposition_Depth)
        
        return Redeposition_Depth
    
    

if __name__ == "__main__":
    
    


    print ('done')    
        
        
        
        