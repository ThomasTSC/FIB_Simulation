# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy


def Parameters():
    
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
    
    Pixel_Distance = 0.25*Beam_Diameter   
    Full_Pixel_Length = 13*(Beam_Standard_Deviation)    
  
    Pass = 1
    Step = 55
    Scan_Line = 1
    
    Grid_Point = 25
    Grid_Space_Y = 5e-8
    
    Dwell_Time = 1e-6
    Integration_Time = 1e-6


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
                  'Integration_Time': Integration_Time,
                  'Mass_Ion':Mass_Ion,
                  'Mass_Sub':Mass_Substrate,
                  'Atomic_number_Ion':AtomicNumber_Ion,
                  'Atomic_number_Sub':AtomicNumber_Substrate,
                  'Atomic_density_Sub':AtomicDensity_Substrate
                  }
    
    
    
    #print (Parameters)
    
    return Parameters
    



if __name__ == "__main__":
    
    Parameters()
    print ('done')