def sum_5_consecutive_for(lst):       #For loop

    if (len(lst)<5):
        return False

    total = 0

    for i in range(0,len(lst)):
        total= 0
        for j in range(i,i+5):
            if(j >= len(lst)):
                return False
            total = total + lst[j]

        if (total==0):
            return True

    return False


#Test examples

print(sum_5_consecutive_for([2,3,-3,2,4,-6]))
print(sum_5_consecutive_for([-10,1,1,4,2,10,13]))
print(sum_5_consecutive_for([2,1,-3,-3,-3,2,7,4,-6]))
print(sum_5_consecutive_for([]))
print(sum_5_consecutive_for([1,-1,0]))


print(" ")

def sum_5_consecutive_while(lst):        #While loop

    if (len(lst)<5):
        return False
    total= 0
    i=0
    while(i<len(lst)):
        total = 0
        j=i
        while(j<(i+5)):
            if (j >= len(lst)):
                return False
            total = total + lst[j]
            j=j+1
        i=i+1

        if (total == 0):
            return True
        
    return False



#Test examples

print(sum_5_consecutive_while([2, 3, -3, 2, 4,-6])) 
print(sum_5_consecutive_while([-10, 1, 1, 4, 2, 10, 13])) 
print(sum_5_consecutive_while([2, 1, -3, -3, -3, 2, 7, 4, -6])) 
print(sum_5_consecutive_while([])) 
print(sum_5_consecutive_while([1, -1,0]))











