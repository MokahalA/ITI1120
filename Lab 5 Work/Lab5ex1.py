#Programming Exercise 1

def ah(l,x,y):
    '''(list,integer,integer) -> tuple
Returns a tuple where the first number contained in it represents how many numbers in
a given list are between the integers given as x and y, the second number represents
the minimum number in the list of numbers between x and y.'''


    list_numbers=[]
    for num in range(max(l)+1):
        if num in l and num > x and num < y:
            list_numbers.append(num)
    
    return (len(list_numbers),min(list_numbers))



#Test example

t = [5,1,-2.5,10,13,8]
print(ah(t,2,11))

