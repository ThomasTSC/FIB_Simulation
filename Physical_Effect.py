'''
Created on May 15, 2018

@author: thoma
'''

import Parameters
import numpy
import Grid_Structure
import Simulator
import Ion_Beam_Profile
import scipy



class Physical_Effect:
    '''
    classdocs
    '''


    def __init__(self, Profile):
        
        self.Parameters = Parameters.Parameters()
        
        self.Profile = Profile
        
        
        #Primary sputtering yield
        # Y(E,0)
        self.Sublimation_Energy = 4.664
        self.Energy_Transfer_Factor = 4*(self.Parameters['Mass_Sub']*self.Parameters['Mass_Ion'])/(numpy.power((self.Parameters['Mass_Sub']+self.Parameters['Mass_Ion']),2))
        self.Eth = 6.7*(self.Sublimation_Energy/self.Energy_Transfer_Factor)
        self.Reduced_Energy = (0.03255)*(1/(self.Parameters['Atomic_number_Ion']*self.Parameters['Atomic_number_Sub']))*(1/numpy.sqrt( numpy.power(self.Parameters['Atomic_number_Ion'],(2/3))+numpy.power(self.Parameters['Atomic_number_Sub'],(2/3))))*(self.Parameters['Mass_Sub']/(self.Parameters['Mass_Sub']+self.Parameters['Mass_Ion']))*self.Parameters['Beam_Energy']
        
        self.Nuclear_Stopping_Power_Coe_1 = 3.441*numpy.sqrt(self.Reduced_Energy)*numpy.log(self.Reduced_Energy+2.718)/(1+6.355*numpy.sqrt(self.Reduced_Energy)+self.Reduced_Energy*(6.882*numpy.sqrt(self.Reduced_Energy)-1.708))
        self.Nuclear_Stopping_Power = self.Nuclear_Stopping_Power_Coe_1*84.78*(self.Parameters['Atomic_number_Ion']*self.Parameters['Atomic_number_Sub'])*(self.Parameters['Mass_Ion']/(self.Parameters['Mass_Sub']+self.Parameters['Mass_Ion']))*(1/numpy.sqrt(numpy.power(self.Parameters['Atomic_number_Ion'],(2/3))+numpy.power(self.Parameters['Atomic_number_Sub'],(2/3))))
        self.Coefficiemt_k = 0.0793*(numpy.power((self.Parameters['Mass_Sub']+self.Parameters['Mass_Ion']),(3/2)))*(1/((numpy.power(self.Parameters['Mass_Ion'],(3/2)))*(numpy.sqrt(self.Parameters['Mass_Sub']))))*((numpy.power(self.Parameters['Atomic_number_Ion'],(2/3)))*numpy.sqrt(self.Parameters['Atomic_number_Sub']))*(1/(numpy.power(((numpy.power(self.Parameters['Atomic_number_Ion'],(2/3)))+(numpy.power(self.Parameters['Atomic_number_Sub'],(2/3)))),(3/4))))
        self.Inelastic_electronic_Stopping_Power = self.Coefficiemt_k*numpy.sqrt(self.Reduced_Energy)
        self.Coefficient_W = 2.32
        self.Coefficient_A = self.Coefficient_W*(numpy.power(self.Reduced_Energy,(-0.2)))/(1+numpy.power((self.Parameters['Mass_Ion']/7),3))
        self.Coefficient_s = 2.5
        self.Coefficient_Q = 0.75
        self.Coefficient_alpha = 0.0875*(numpy.power((self.Parameters['Mass_Sub']/self.Parameters['Mass_Ion']),(-0.15)))+0.165*((self.Parameters['Mass_Sub']/self.Parameters['Mass_Ion']))
        self.Sputtering_Yield_1 = 0.042*self.Coefficient_Q*self.Coefficient_alpha*(1/self.Sublimation_Energy)*(self.Nuclear_Stopping_Power)*(1/(1+self.Coefficient_A*self.Inelastic_electronic_Stopping_Power))*(numpy.power((1-numpy.sqrt(self.Eth/self.Parameters['Beam_Energy'])),(self.Coefficient_s)))
        
        
        #f
        self.fs = (1.86*numpy.power((self.Parameters['Mass_Sub']/self.Parameters['Mass_Ion']),(-0.115)))-(0.0657)*(self.Parameters['Mass_Sub']/self.Parameters['Mass_Ion'])
        self.Coefficient_Z = 1-numpy.sqrt(self.Eth/self.Parameters['Beam_Energy'])
        self.Sputtering_Yield_2 = self.fs*(1+2.5*((1-self.Coefficient_Z)/self.Coefficient_Z))
        
        #Sigma
        self.Coefficient_QQ = 0.75
        self.Coefficient_r = numpy.power((self.Coefficient_QQ/(0.019-0.0257*(self.Parameters['Mass_Sub']/100)+0.032*(numpy.power((self.Parameters['Mass_Sub']/100),2))-0.01*(numpy.power((self.Parameters['Mass_Sub']/100),3)))),3)
        self.Bohr_Radius = 5.29e-11
        self.Coefficient_a12 = (numpy.power((9*(numpy.power(numpy.pi,2))/128),(1/3)))*(self.Bohr_Radius/(numpy.sqrt(numpy.power(self.Parameters['Atomic_number_Ion'],(2/3))+numpy.power(self.Parameters['Atomic_number_Sub'],(2/3)))))
        self.Coefficient_Phi = (numpy.power((self.Coefficient_a12/self.Coefficient_r),(1.5)))*numpy.sqrt((self.Parameters['Atomic_number_Ion']*self.Parameters['Atomic_number_Sub'])*(1/(self.Parameters['Beam_Energy']*numpy.sqrt(numpy.power(self.Parameters['Atomic_number_Ion'],(2/3))+numpy.power(self.Parameters['Atomic_number_Sub'],(2/3))))))
        self.Coefficient_AngMax = numpy.deg2rad(90-286*((1e10)*numpy.power((self.Coefficient_Phi),(0.45))))
        self.Sputtering_Yield_3 = self.Sputtering_Yield_2*numpy.cos(self.Coefficient_AngMax)
    
    
    
    def maxSputteringYield(self):
        
        Max_Sputtering_Yield = []
        
        for deg in range(0,90):
        
            MaxAngel_to_Rad = numpy.deg2rad(deg)
        
            Max_Cos = numpy.cos(MaxAngel_to_Rad) 
        
            Max_Sputtering_Yield.append(self.Sputtering_Yield_1*(numpy.power((1/Max_Cos.astype(float)),(self.Sputtering_Yield_2)))*(numpy.exp(-self.Sputtering_Yield_3*((1/Max_Cos.astype(float))-1))))
        
        
        Max_Sputtering_Yield = numpy.max(Max_Sputtering_Yield)
        
        #print (Max_Sputtering_Yield)
        
        return Max_Sputtering_Yield
    
        
    def sputteringYield(self):
        
        
        Max_Sputtering_Yield = Physical_Effect(self.Profile).maxSputteringYield()
        
        Singular_Point = Grid_Structure.Grid_Structure(self.Profile).findSingularPoint()
        

        Incident_Cos = Grid_Structure.Grid_Structure(self.Profile).incidentCosine()
        
        Sputtering_Yield = self.Sputtering_Yield_1*(numpy.power((1/Incident_Cos['Incident_Cos'].astype(float)),(self.Sputtering_Yield_2)))*(numpy.exp(-self.Sputtering_Yield_3*((1/Incident_Cos['Incident_Cos'].astype(float))-1)))
        
        
        Sputtering_Yield = {'Sputtering_Yield': Sputtering_Yield}
        
        #print ((Sputtering_Yield))
        
        return Sputtering_Yield
    

    
    def dwellTimeMatrix(self):
        
        Dwell_Time_Matrix = self.Parameters['Integration_Time']*numpy.ones_like(self.Profile['Grid_X'])
        
        Dwell_Time_Matrix = {'Dwell_Time_Matrix': Dwell_Time_Matrix}
    
        
        return Dwell_Time_Matrix
    
    
    def primarySputtering(self,Beam_Position_X,Beam_Position_Y):
    
        Primary_Ion_Beam = Ion_Beam_Profile.Ion_Beam_Profile(self.Profile).primaryIonBeamProfile(Beam_Position_X,Beam_Position_Y)
        
        Sputtering_Yield = Physical_Effect(self.Profile).sputteringYield()
                
        Dwell_Time_Matrix = Physical_Effect(self.Profile).dwellTimeMatrix()
      
        Incident_Angle = Grid_Structure.Grid_Structure(self.Profile).incidentAngle()
      
        Surface_Moving_Vector = Grid_Structure.Grid_Structure(self.Profile).surfaceMovingVector()
        
        
        Surface_Moving_Vector_X = -(Surface_Moving_Vector['Surface_Moving_Vector'][0]/numpy.sqrt(numpy.power(Surface_Moving_Vector['Surface_Moving_Vector'][0],2) + numpy.power(Surface_Moving_Vector['Surface_Moving_Vector'][1],2)))
        Surface_Moving_Vector_Z = -(Surface_Moving_Vector['Surface_Moving_Vector'][1]/numpy.sqrt(numpy.power(Surface_Moving_Vector['Surface_Moving_Vector'][0],2) + numpy.power(Surface_Moving_Vector['Surface_Moving_Vector'][1],2)))
        
        #print (Primary_Ion_Beam['Primary_Ion_Beam_Profile_Mid']*(Sputtering_Yield['Sputtering_Yield'])*Grid_Area) 
        
        
        Primary_Sputtering_Depth_Total = -(1/self.Parameters['Atomic_density_Sub'])*Primary_Ion_Beam['Primary_Ion_Beam_Profile']*(Sputtering_Yield['Sputtering_Yield'])*Dwell_Time_Matrix['Dwell_Time_Matrix']
     
        
        Primary_Sputtering_Depth_X = Primary_Sputtering_Depth_Total*Surface_Moving_Vector_X
        Primary_Sputtering_Depth_Z = Primary_Sputtering_Depth_Total*Surface_Moving_Vector_Z
        

        Primary_Sputtering_Depth = {'Primary_Sputtering_Depth_X':Primary_Sputtering_Depth_X, 
                                    'Primary_Sputtering_Depth_Z':Primary_Sputtering_Depth_Z,
   
                                    'Primary_Sputtering_Depth_Total':Primary_Sputtering_Depth_Total}
      
        #print (Primary_Sputtering_Depth)
      
        return Primary_Sputtering_Depth
    
    
    
    def Redeposition(self):
        
        
        Redeposition_Total = []

        
        
        Redeposition_X = Redeposition_Total
        
        Redeposition_Z = Redeposition_Total
        
        
        Redeposition = {'Redeposition_X':Redeposition_X, 
                        'Redeposition_Z':Redeposition_Z,
                        'Redeposition_Total':Redeposition_Total
                        }
        
        
        
        return  Redeposition
    
    
    
    
    
    def secondarySputtering(self):
        
        
        Secondary_Sputtering_Depth = {}
        
        return Secondary_Sputtering_Depth
    
    
    

    def meanFreePathEffect(self):
        
        
        
        
        return 0
    
    
if __name__ == "__main__":
    
    import Scanning_Strategy

    import Simulator
    
    Profile = Simulator.FIB().Simulation()
    
    
    Physical_Effect(Profile).dwellTimeMatrix()
    
    

    
    
    
    
    print ('done')
    