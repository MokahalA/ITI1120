class Point:
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord
    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

def increment_all(x,p):
    x=x+1
    p.x=p.x+1
    p.y=p.y+1
    
p1=Point(1,10)
y=1
print(y,p1)
increment_all(y,p1)
print(y, p1)


# p1 stores the value x = 1 and y = 10 and the string " Point('1','10') "
# y = 1
# It prints 1 Point(1,10)
# increment_all(y,p1) ~ p.x = 1+1 and p.y = 10+1 so p1 now stores x = 2 and y = 11
# It prints 1 Point(2,11)
