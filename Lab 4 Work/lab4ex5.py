def prime(n):
    '''(int) -> bool
returns a boolean expression "True" if the number inputted is a prime number and
"False" if it is not a prime number.'''
    for d in range(2,n+1,1):
        condition= (not n%d==0 and d>=2)
        return condition 
            

n=int(input("Enter a positive integer: "))
for d in range(1,n+1,1):
    if n%d==0:
        print(d,end=" ")
print("\n")

if prime(n):
    print("The number ", n ," is a prime")
else:
    print("The number", n ,"is not a prime")

