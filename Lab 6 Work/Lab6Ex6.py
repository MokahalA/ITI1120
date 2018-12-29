def fib(n):
    '''(int) -> list
Returns a list containing the values of the fibonacci sequence up to nth term that
is entered by the user.'''
    
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst


#Test examples

print(fib(7))

