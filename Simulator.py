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
        self.initSegment = Grid_Structure.Grid_Structure().initSegment(self.initGrid)
        self.Scanning_Path = Scanning_Strategy.Scanning_Strategy().rasterScan()



    def Simulation(self):
        
        Segment = self.initSegment
        
        for Pass in range(self.Parameters['Pass']):
        
            for Step in range(len(self.Scanning_Path['Scanning_Path_X'])):
                Beam_Position = [self.Scanning_Path['Scanning_Path_X'][Step], self.Scanning_Path['Scanning_Path_Y'][Step]]
                Primary_Ion_Beam = Ion_Beam_Profile.Ion_Beam_Profile().Primary_Ion_Beam_Profile(Beam_Position[0], Beam_Position[1], Segment)
                #plt.figure()
                #plt.plot(Segment['Segment_XCor'],Primary_Ion_Beam)
                #plt.show()
                Primary_Sputtering = Physical_Effect.Physical_Effect().primarySputtering(Beam_Position[0], Beam_Position[1],Segment)
                
                Segment['Segment_XCor']= Segment['Segment_XCor']+ Primary_Sputtering['Primary_Sputtering_Depth_X']
                Segment['Segment_ZCor']= Segment['Segment_ZCor']+ Primary_Sputtering['Primary_Sputtering_Depth_Z']
                
        
                
                Segment = {'Segment_XCor_Front': Segment['Segment_XCor_Front'],
                      'Segment_XCor_End': Segment['Segment_XCor_End'],
                      'Segment_XCor': Segment['Segment_XCor'],
                      'Segment_YCor': Segment['Segment_YCor'],
                      'Segment_ZCor': Segment['Segment_ZCor'],
                      'Segment_ZCor_Front': Segment['Segment_ZCor_Front'],
                      'Segment_ZCor_End': Segment['Segment_ZCor_End'],
                      'Beam_Position':Beam_Position}
            
            
        
        return Segment
    
    
    
    
if __name__ == "__main__":
    
    Result = FIB().Simulation()
    
    #print (Result)
    
    plt.figure()
    plt.xlim(0,2e-7)
    plt.ylim(-5e-6,1e-7)
    plt.scatter(Result['Segment_XCor'],Result['Segment_ZCor'])
    plt.show()
    
    print ('done')
    
    