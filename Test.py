    
v0 = [0,0]
v1 = [2,0]
v2 = [0,2] 
p = [1,1]   
    
def B(v0,v1,v2,p):    
    s=(v1[0]-v0[0])*(v2[1]-v0[1])-(v1[1]-v0[1])*(v2[0]-v0[0])
    a=((v1[0]-p[0])*(v2[1]-p[1])-(v1[1]-p[1])*(v2[0]-p[0]))/s
    b=((v1[0]-p[0])*(v0[1]-p[1])-(v1[1]-p[1])*(v0[0]-p[0]))/s
    c =1-a-b
    
    print (a,b,c)
    return (a,b,c)

B(v0,v1,v2,p)