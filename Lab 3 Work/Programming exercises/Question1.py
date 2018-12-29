def pay(w,h):
    '''(int,int) --> float
Given integers of hourly wage w and number of hours h. It returns the employee\'s
wage including overtime as a float.'''

    p= w*h
    o1= (1.5*w)*(h%40)
    o2= (2*w)*(h%60)
    if h<=40:
        print (p)
    elif h>40 and h<=60:
        print (400 + (o1))
    else:
        print(400 + 300 + (o2))
    
        
