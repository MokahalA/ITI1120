import math

def roots(a,b,c):   
    d = b**2-4*a*c          #discriminant
    k= math.sqrt(d)         #sqrt of discriminant
    r1= (-b+k)/(2*a)        #solution1 
    r2= (-b-k)/(2*a)        #solution2
    print ("The quadratic equation with coefficients a = ", a ,"b= ", b ,"c= ", c ,"has the following solutions (i.e. roots):", r1 ,"and", r2)
    
