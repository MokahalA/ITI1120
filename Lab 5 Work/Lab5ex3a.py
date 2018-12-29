#Programming Exercise 3a:

def arithmetic(a_List):
    '''(lst) -> bool
    Returns the boolean expression True if numbers on the given list of numbers
    forms an arithmetic progression and False otherwise.
    
    Precondition: A sequence with only one number is considered arithmetic.'''
    
    diff1=(a_List[1]-a_List[0])
    i=1
    for num in range(1,len(a_List)-1,1):
        i=i+1
        diff2=(a_List[i]-a_List[num])
        if diff1 != diff2:
            return False
    return True


#Test examples

print(arithmetic([-5,-1,3,7,11]))
print(arithmetic([0,-1,3,7,11]))
a= [5,10,15,24,29]
print(arithmetic(a))
print(arithmetic(a[:3]))
               
