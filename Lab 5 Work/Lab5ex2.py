def is_perfect(n):
    '''(int) -> bool
    Returns the boolean expression True if the given integer is a perfect number
    and False otherwise.'''
    
    add = 0
    for num in range(1,n):
        if (n % num == 0):
            add = add + num
    if (add == n):
        return True
    else:
        return False

#Test examples

print(is_perfect(6))
print(is_perfect(12))



r=input("What are the perfect numbers that are smaller than: ")
for j in range(1,int(r)):
    if is_perfect(j):     
        print(j, end=" ")
    
            


  

#try with 10000

#try with 350000000
