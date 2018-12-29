def is_prime(n):
    '''(number) -> bool
Return True if a given positive number n>=2 is a prime and false otherwise
Precondition n>=2 '''


    for divisor in range(2,n):
        if n%divisor == 0:
            return False
        
    return True 


#Test example

print(is_prime(1))       #Should return False since 1 is not a prime number
