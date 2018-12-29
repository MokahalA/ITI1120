class Point:
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord
    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

def riddle(a,b):
    a=b
    a.x=1000
    a.y=1000
    
p1=Point(1,2)
p2=Point(10,20)
print(p1,p2)
riddle(p1,p2)
print(p1, p2)


# p1 stores x = 1 and y = 2 and string Point(1,2)
# p2 stores x = 10 and y = 20 and string Point(10,20)
# It prints Point(1,2) Point(10,20)
# riddle(p1,p2) ~ a refers to p1 and b refers to p2 
# a refers to b so now both a and b refer to p2 and p2 now stores x = 1000 and y = 1000
# It prints Point(1,2) Point(1000,1000) since p1 remains unchanged. 
