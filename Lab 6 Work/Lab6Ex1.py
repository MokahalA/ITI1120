def sum_odd_while_v2(n):
    '''(int)-> int
Returns an integer that represents the sum of all odd integers between 5 and
the entered integer n.'''
    
    i=n
    total=0
    while i !=5: 
        for i in range(5,n,2):
            total=total+i
        return total


#Test examples
print(sum_odd_while_v2(10))        
print(sum_odd_while_v2(-7))
