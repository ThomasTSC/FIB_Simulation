import Parameters
import numpy
import Grid_Structure



class PrimarySputtering:
    
    
    def __init__(self, Profile, Beam_Position_X, Beam_Position_Y):
        
        self.Physical_Parameters = Parameters.Physical_Parameters()
        self.Profile = Profile
        self.Grid_Structure = Grid_Structure.Grid_Structure(self.Profile).grid()
        self.Sputtering_Parameters = Parameters.Sputtering_Parameters()
        self.Beam_Position_X = Beam_Position_X
        self.Beam_Position_Y = Beam_Position_Y 
        
        
    def primaryIonBeamProfile(self):
        
        
        Primary_Ion_Beam_Profile = self.Physical_Parameters['Ion_Flux']*numpy.exp(-(((self.Profile['Grid_X']-self.Beam_Position_X)**2+(self.Profile['Grid_Y']-self.Beam_Position_Y)**2)/(2*self.Physical_Parameters['Beam_Standard_Deviation']**2)))
        
        Pr_Normalized_Factor = 1/(numpy.sum(Primary_Ion_Beam_Profile)/self.Physical_Parameters['Ion_Flux'])
    
        Primary_Ion_Beam_Profile = {'Primary_Ion_Beam_Profile':Primary_Ion_Beam_Profile*Pr_Normalized_Factor}
    
        #print (Primary_Ion_Beam_Profile)
    
        return Primary_Ion_Beam_Profile
        
        
        
    def sputteringYield(self):
    
        
        Sputtering_Yield = self.Sputtering_Parameters['Sputtering_Yield_1']*(numpy.power((1/self.Grid_Structure['Incident_Cos'].astype(float)),(self.Sputtering_Parameters['Sputtering_Yield_2'])))*(numpy.exp(-self.Sputtering_Parameters['Sputtering_Yield_3']*((1/self.Grid_Structure['Incident_Cos'].astype(float))-1)))
        
        
        Sputtering_Yield = {'Sputtering_Yield': Sputtering_Yield}
        
        #print ((Sputtering_Yield))
        
        return Sputtering_Yield
    

    
    def dilutedIonBeamEffect(self):
        
        
        Grid_Length = numpy.sqrt(numpy.power(numpy.diff(self.Profile['Grid_Z']),2) + numpy.power(numpy.diff(self.Profile['Grid_X']),2))
        
        Grid_Length = 0.5*(Grid_Length[0:-1]+Grid_Length[1:])
        
        Grid_Length = numpy.append(Grid_Length,[self.Profile['Grid_Space_X']])
       
        Grid_Length = numpy.insert(Grid_Length,0,self.Profile['Grid_Space_X'])
        
        
        Initial_Grid_Length = self.Profile['Grid_Space_X']
        
        Diluted_Ion_Beam_Effect = Initial_Grid_Length/Grid_Length
        
        Diluted_Ion_Beam_Effect = {'Diluted_Ion_Beam_Effect': Diluted_Ion_Beam_Effect}
        
        #print (Diluted_Ion_Beam_Effect)
        
        return Diluted_Ion_Beam_Effect        
        
        
    
    def primarySputtering(self):
    
        Primary_Ion_Beam = PrimarySputtering.primaryIonBeamProfile(self)
        
        Diluted_Ion_Beam_Effect = PrimarySputtering.dilutedIonBeamEffect(self)
        
        Sputtering_Yield = PrimarySputtering.sputteringYield(self)
                
        
        
        Surface_Moving_Vector_X = -(self.Grid_Structure['Surface_Moving_Vector'][0]/numpy.sqrt(numpy.power(self.Grid_Structure['Surface_Moving_Vector'][0],2) + numpy.power(self.Grid_Structure['Surface_Moving_Vector'][1],2)))
        Surface_Moving_Vector_Z = -(self.Grid_Structure['Surface_Moving_Vector'][1]/numpy.sqrt(numpy.power(self.Grid_Structure['Surface_Moving_Vector'][0],2) + numpy.power(self.Grid_Structure['Surface_Moving_Vector'][1],2)))
        
        
        Primary_Sputtering_Depth_Total = -(1/self.Physical_Parameters['Atomic_density_Sub'])*Primary_Ion_Beam['Primary_Ion_Beam_Profile']*(Sputtering_Yield['Sputtering_Yield'])*self.Physical_Parameters['Dwell_Time_Matrix']*Diluted_Ion_Beam_Effect['Diluted_Ion_Beam_Effect']
     
        
        Primary_Sputtering_Depth_X = Primary_Sputtering_Depth_Total*Surface_Moving_Vector_X
        Primary_Sputtering_Depth_Z = Primary_Sputtering_Depth_Total*Surface_Moving_Vector_Z
        

        Primary_Sputtering_Depth = {'Primary_Sputtering_Depth_X':Primary_Sputtering_Depth_X, 
                                    'Primary_Sputtering_Depth_Z':Primary_Sputtering_Depth_Z,
                                    'Primary_Sputtering_Depth_Total':Primary_Sputtering_Depth_Total}
      
        #print (Primary_Sputtering_Depth)
      
        return Primary_Sputtering_Depth
    
    
    


if __name__ == "__main__":
    

    print ('done')    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        