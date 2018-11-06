# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy


class Import_Parameters:



    def __init__(self):
        
        
        pass



    def Parameters(self):
        
        #Global Constant#
        nm_to_m = 1e-9 
        keV_to_eV = 1000        
        pA_to_A = 1e-12
        
        #Instrument Parameters#
        Beam_Current = 70*pA_to_A 
        Beam_Diameter = 70*nm_to_m #m
    
        Beam_Radius = 0.5*Beam_Diameter
        Beam_Energy = 30*keV_to_eV
        Beam_Standard_Deviation = Beam_Diameter/numpy.sqrt(8*numpy.log(2))
        Pressure = 0 #Not yet decided
        
        #Physical Parameters#
        
        """The property parameters and the physical constants"""
        """The parameters below are currently only for Ga/Si system."""
        Unit_Charge = 1.6e-19
        Avogadro_Number = 6e23
        Temperature = 293
        Gas_Constant = 8.314    
        Boltzman_Constant = 1.38*1e-23
        
        
        #Process Parameters
        #Pixel_Area = (numpy.pi)*((Beam_Radius)**2)
        
        Pixel_Area = (numpy.pi)*((6.25*Beam_Standard_Deviation)**2)
        Pixel_Distance = 0.2*Beam_Diameter   
        Full_Pixel_Length = 13*(Beam_Standard_Deviation)    
      
        Pass = 1
        Step = 1
        Scan_Line = 1
        
        Grid_Point = 25
        Grid_Space_Y = 5e-8
        
        Dwell_Time = 1e-6    
        Integration_Time = 1e-6
        Dwell_Time_Matrix = Integration_Time*numpy.ones_like(Grid_Point)
    
    
    
        #The properties of Si/Ga system#
        Mass_Ion = 69.723
        Mass_Substrate = 28.0855    
        AtomicNumber_Ion = 31 
        AtomicNumber_Substrate = 14
        AtomicDensity_Substrate = 5e28
        
        Ion_Flux = ((Beam_Current)/Unit_Charge)/Pixel_Area #Ion/(m2 per second)
        
        
        
        Parameters = {
                      'Beam_Current':Beam_Current, 
                      'Beam_Diameter':Beam_Diameter,
                      'Beam_Radius': Beam_Radius,
                      'Beam_Energy': Beam_Energy,
                      'Beam_Standard_Deviation':Beam_Standard_Deviation, 
                      'Pressure':Pressure, 
                      'Unit_Charge': Unit_Charge,
                      'Avogadro_Number':Avogadro_Number,
                      'Temperature': Temperature,
                      'Gas_Constant': Gas_Constant,
                      'Boltzman_Constant':Boltzman_Constant,
                      'Pixel_Area':Pixel_Area,
                      'Pixel_Distance':Pixel_Distance, 
                      'Full_Pixel_Length':Full_Pixel_Length ,
                      'Ion_Flux': Ion_Flux,
                      'Pass':Pass,
                      'Step':Step, 
                      'Scan_Line':Scan_Line,
                      'Grid_Point':Grid_Point,
                      'Grid_Space_Y':Grid_Space_Y,
                      'Dwell_Time':Dwell_Time,
                      'Dwell_Time_Matrix':Dwell_Time_Matrix,
                      'Integration_Time': Integration_Time,
                      'Mass_Ion':Mass_Ion,
                      'Mass_Sub':Mass_Substrate,
                      'Atomic_number_Ion':AtomicNumber_Ion,
                      'Atomic_number_Sub':AtomicNumber_Substrate,
                      'Atomic_density_Sub':AtomicDensity_Substrate
                      }
        
        
        
        #print (Parameters)
        
        return Parameters
        
        
        
    def Sputtering_Parameters(self):
        
        
        Parameters = Import_Parameters.Parameters(self)
        
        Sublimation_Energy = 4.664
        Energy_Transfer_Factor = 4*(Parameters['Mass_Sub']*Parameters['Mass_Ion'])/(numpy.power((Parameters['Mass_Sub']+Parameters['Mass_Ion']),2))
        Eth = 6.7*(Sublimation_Energy/Energy_Transfer_Factor)
        Reduced_Energy = (0.03255)*(1/(Parameters['Atomic_number_Ion']*Parameters['Atomic_number_Sub']))*(1/numpy.sqrt( numpy.power(Parameters['Atomic_number_Ion'],(2/3))+numpy.power(Parameters['Atomic_number_Sub'],(2/3))))*(Parameters['Mass_Sub']/(Parameters['Mass_Sub']+Parameters['Mass_Ion']))*Parameters['Beam_Energy']
        
        Nuclear_Stopping_Power_Coe_1 = 3.441*numpy.sqrt(Reduced_Energy)*numpy.log(Reduced_Energy+2.718)/(1+6.355*numpy.sqrt(Reduced_Energy)+Reduced_Energy*(6.882*numpy.sqrt(Reduced_Energy)-1.708))
        Nuclear_Stopping_Power = Nuclear_Stopping_Power_Coe_1*84.78*(Parameters['Atomic_number_Ion']*Parameters['Atomic_number_Sub'])*(Parameters['Mass_Ion']/(Parameters['Mass_Sub']+Parameters['Mass_Ion']))*(1/numpy.sqrt(numpy.power(Parameters['Atomic_number_Ion'],(2/3))+numpy.power(Parameters['Atomic_number_Sub'],(2/3))))
        Coefficiemt_k = 0.0793*(numpy.power((Parameters['Mass_Sub']+Parameters['Mass_Ion']),(3/2)))*(1/((numpy.power(Parameters['Mass_Ion'],(3/2)))*(numpy.sqrt(Parameters['Mass_Sub']))))*((numpy.power(Parameters['Atomic_number_Ion'],(2/3)))*numpy.sqrt(Parameters['Atomic_number_Sub']))*(1/(numpy.power(((numpy.power(Parameters['Atomic_number_Ion'],(2/3)))+(numpy.power(Parameters['Atomic_number_Sub'],(2/3)))),(3/4))))
        Inelastic_electronic_Stopping_Power = Coefficiemt_k*numpy.sqrt(Reduced_Energy)
        Coefficient_W = 2.32
        Coefficient_A = Coefficient_W*(numpy.power(Reduced_Energy,(-0.2)))/(1+numpy.power((Parameters['Mass_Ion']/7),3))
        Coefficient_s = 2.5
        Coefficient_Q = 0.75
        Coefficient_alpha = 0.0875*(numpy.power((Parameters['Mass_Sub']/Parameters['Mass_Ion']),(-0.15)))+0.165*((Parameters['Mass_Sub']/Parameters['Mass_Ion']))
        Sputtering_Yield_1 = 0.042*Coefficient_Q*Coefficient_alpha*(1/Sublimation_Energy)*(Nuclear_Stopping_Power)*(1/(1+Coefficient_A*Inelastic_electronic_Stopping_Power))*(numpy.power((1-numpy.sqrt(Eth/Parameters['Beam_Energy'])),(Coefficient_s)))
        
        
        #f
        fs = (1.86*numpy.power((Parameters['Mass_Sub']/Parameters['Mass_Ion']),(-0.115)))-(0.0657)*(Parameters['Mass_Sub']/Parameters['Mass_Ion'])
        Coefficient_Z = 1-numpy.sqrt(Eth/Parameters['Beam_Energy'])
        Sputtering_Yield_2 = fs*(1+2.5*((1-Coefficient_Z)/Coefficient_Z))
        
        #Sigma
        Coefficient_QQ = 0.75
        Coefficient_r = numpy.power((Coefficient_QQ/(0.019-0.0257*(Parameters['Mass_Sub']/100)+0.032*(numpy.power((Parameters['Mass_Sub']/100),2))-0.01*(numpy.power((Parameters['Mass_Sub']/100),3)))),3)
        Bohr_Radius = 5.29e-11
        Coefficient_a12 = (numpy.power((9*(numpy.power(numpy.pi,2))/128),(1/3)))*(Bohr_Radius/(numpy.sqrt(numpy.power(Parameters['Atomic_number_Ion'],(2/3))+numpy.power(Parameters['Atomic_number_Sub'],(2/3)))))
        Coefficient_Phi = (numpy.power((Coefficient_a12/Coefficient_r),(1.5)))*numpy.sqrt((Parameters['Atomic_number_Ion']*Parameters['Atomic_number_Sub'])*(1/(Parameters['Beam_Energy']*numpy.sqrt(numpy.power(Parameters['Atomic_number_Ion'],(2/3))+numpy.power(Parameters['Atomic_number_Sub'],(2/3))))))
        Coefficient_AngMax = numpy.deg2rad(90-286*((1e10)*numpy.power((Coefficient_Phi),(0.45))))
        Sputtering_Yield_3 = Sputtering_Yield_2*numpy.cos(Coefficient_AngMax)
        
        
        Sputtering_Parameters = {'Sputtering_Yield_1':Sputtering_Yield_1,
                                 'Sputtering_Yield_2':Sputtering_Yield_2,
                                 'Sputtering_Yield_3':Sputtering_Yield_3}
        
        
        
           
        return Sputtering_Parameters
        
        
        
        
        



if __name__ == "__main__":
    
    Import_Parameters().Parameters()
    Import_Parameters().Sputtering_Parameters()
    print ('done')