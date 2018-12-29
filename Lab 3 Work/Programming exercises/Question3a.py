def is_divisible(n,m):
    ''' (int,int) --> bool
prints True if n is divisible by m, otherwise it prints False ''' 
    if n%m == 0:
        print(True)
    else:
        print(False)


n=input("Enter 1st integer: ")
m=input("Enter 2nd integer: ")
if (int(n)%int(m)) == 0:
    print(n , "is divisble by", m)
else:
    print(n, "is not divisble by", m)



        
