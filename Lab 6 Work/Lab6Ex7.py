def inner_product(lst1,lst2):
    '''(list,list) -> int
Returns the inner product (dot product) of the integers in the two lists that
are given to the function.'''
    
    total=0
    for i in range(0,len(lst1)):
        total=total+(lst1[i]*lst2[i])
        
    return total



#Test example

print(inner_product([2,3,4],[1,0,2]))
