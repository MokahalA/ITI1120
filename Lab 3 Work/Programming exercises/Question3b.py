def is_divisible(n,m):
    ''' (int,int) --> bool
prints True if n is divisible by m, otherwise it prints False ''' 
    return n%m == 0


def is_divisible23n8(n):
    ''' (int) --> bool
returns "yes" if integer n is divisible by 2 or 3 but not 8, it returns "no"
if integer n is divisible by 2 or 3 and 8.'''

    if (is_divisible(n,3) or is_divisible(n,2) and not is_divisible(n,8)):
        return("yes")
    if(is_divisible(n,3) or is_divisible(n,2) and is_divisible(n,8)):
        return("no")
    
n=int(input("Enter an integer: "))
if is_divisible23n8(n) == "yes":
    print(str(n), "is divisible by 2 or 3 but not 8")
else:
    print("It is not true that", str(n) ,"is divisble by 2 or 3 but not 8")
            
    


