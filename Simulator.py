'''
Created on 15.05.2018

@author: chou
'''


import Ion_Beam_Profile
import Grid_Structure
import Physical_Effect
import Scanning_Strategy
import matplotlib.pyplot as plt
import Parameters


class FIB:
    '''
    classdocs
    '''

    def __init__(self):
        
        self.Parameters = Parameters.Parameters()
        self.initGrid = Grid_Structure.Grid_Structure().initialGrid()
        self.initSegment = Grid_Structure.Grid_Structure().initialSegment(self.initGrid)
        self.Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()



    def Simulation(self):
        
        Segment = self.initSegment
        
        for Pass in range(self.Parameters['Pass']):
        
            for Step in range(len(self.Scanning_Path['Scanning_Path_X'])):
                Beam_Position = [self.Scanning_Path['Scanning_Path_X'][Step], self.Scanning_Path['Scanning_Path_Y'][Step]]
                Primary_Ion_Beam = Ion_Beam_Profile.Ion_Beam_Profile().Primary_Ion_Beam_Profile(Beam_Position[0], Beam_Position[1], Segment)
                Primary_Sputtering = Physical_Effect.Physical_Effect().primarySputtering(Beam_Position[0], Beam_Position[1],Segment)
                
                
                Segment['Segment_XCor_Front']= Segment['Segment_XCor_Front']+ Primary_Sputtering['Primary_Sputtering_Depth_X_Front']
                Segment['Segment_ZCor_Front']= Segment['Segment_ZCor_Front']+ Primary_Sputtering['Primary_Sputtering_Depth_Z_Front']
                
                Segment['Segment_XCor_End']= Segment['Segment_XCor_End']+ Primary_Sputtering['Primary_Sputtering_Depth_X_End']
                Segment['Segment_ZCor_End']= Segment['Segment_ZCor_End']+ Primary_Sputtering['Primary_Sputtering_Depth_Z_End']

                Segment['Segment_XCor']= 0.5*(Segment['Segment_XCor_Front'] + Segment['Segment_XCor_End'])
                Segment['Segment_ZCor']= 0.5*(Segment['Segment_ZCor_Front'] + Segment['Segment_ZCor_End'])
        

                
                Segment = {'Segment_XCor_Front': Segment['Segment_XCor_Front'],
                      'Segment_XCor_End': Segment['Segment_XCor_End'],
                      'Segment_XCor': Segment['Segment_XCor'],
                      'Segment_YCor': Segment['Segment_YCor'],
                      'Segment_ZCor': Segment['Segment_ZCor'],
                      'Segment_ZCor_Front': Segment['Segment_ZCor_Front'],
                      'Segment_ZCor_End': Segment['Segment_ZCor_End'],
                      'Primary_Sputtering':Primary_Sputtering,
                      'Beam_Position':Beam_Position}
            
            
                #Resampling Smoothing#
                Segment['Segment_XCor_Front']= Grid_Structure.Grid_Structure().Surface_Smoothing(Segment)['Segment_XCor_Front']
                Segment['Segment_XCor_End']= Grid_Structure.Grid_Structure().Surface_Smoothing(Segment)['Segment_XCor_End']
                Segment['Segment_ZCor_Front']= Grid_Structure.Grid_Structure().Surface_Smoothing(Segment)['Segment_ZCor_Front']
                Segment['Segment_ZCor_End']= Grid_Structure.Grid_Structure().Surface_Smoothing(Segment)['Segment_ZCor_End']
            
            
                #Convolution Smoothing#
                #Segment['Segment_XCor_Front']= Grid_Structure.Grid_Structure().convolution_Smoothing(Segment)['Segment_XCor_Front']
                #Segment['Segment_XCor_End']= Grid_Structure.Grid_Structure().convolution_Smoothing(Segment)['Segment_XCor_End']
                #Segment['Segment_ZCor_Front']= Grid_Structure.Grid_Structure().convolution_Smoothing(Segment)['Segment_ZCor_Front']
                #Segment['Segment_ZCor_End']= Grid_Structure.Grid_Structure().convolution_Smoothing(Segment)['Segment_ZCor_End']
            
            
            
        
        return Segment
    
    
    
    
if __name__ == "__main__":
    
    Result = FIB().Simulation()
    
    #print (Result)
    
    m_to_nm = 1e9
    
    plt.figure()
    #plt.xlim(0,1e-6)
    #plt.ylim(-1e-7,1e-7)
    plt.title('Simulated Trench')
    #plt.scatter(Result['Segment_XCor_Front']*m_to_nm,Result['Segment_ZCor_Front']*m_to_nm)
    #plt.scatter(Result['Segment_XCor_End']*m_to_nm,Result['Segment_ZCor_End']*m_to_nm)
    plt.scatter(Result['Segment_XCor']*m_to_nm,Result['Segment_ZCor']*m_to_nm)
    plt.show()
    
    print ('done')
    
    