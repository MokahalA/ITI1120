#Programming Exercise 3b:

def is_sorted(a_List):
    '''(lst) -> bool
    Returns the boolean expression True if numbers on the given list of numbers
    forms are sorted in order of smallest to largest and False otherwise.'''
    
    i=0
    for num in range(0,len(a_List)-1,1):
        i=i+1
        if a_List[i] < a_List[num]:
            return False
    return True 


           
#Test examples

print(is_sorted([1,1,1,7,7]))
print(is_sorted([-10,-1,3,7,100]))
print(is_sorted([0,3,1,7,11]))
a= [5,-10,15,24,29]
print(is_sorted(a))
print(is_sorted(a[1:4]))
               
