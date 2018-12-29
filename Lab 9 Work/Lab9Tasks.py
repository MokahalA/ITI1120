# Task 1

def foo1(n):    
    i=1   
    while i<n:  #n
        i=i*2 
        count=count+1 

# O(n)

def foo2(n):
    i=n 
    while i >= 1: 
        i= i//2
        
# O(log N) base 2

def foo3(n):
    for i in range(n):  #n
        print("*")

# O(n)

def foo4(n):
    for i in range(-n,n,3): #2n/3
        print("*")
# O(n)

def foo5(n):
    for i in range(n): # n 
        for j in range(i+1,n): # (n-1)*n
            print("*")        
# O(n^2)

def foo6(n):
    for i in range(n): #n
        for j in range(n): #n*n
            for k in range(n): #n*n*n
                print("*")
# O(n^3)


def foo7(n):
    for i in range(n):  #n 
        j=n  
        while j>=1:  # log n  base: 2
            j=j//2

# O(n*log N)


#Task 2


def annona(L):
    count=0
    for i in range(len(L)): #n
        flag = True
        for j in range(len(L)): #n*n
            if L[i] == L[j] and i != j: #n*n
                flag = False
        if flag: #n
            count=count+1
    return count

# O(n^2)

lst=[1,0,2,0,3]
result=annona(lst)
print(result)

#1  It prints 3 
#2  The function finds out how many of the elements in the list are not repeated.
#3  1000 * 1000 = 1 million times so (D) for how many times L[i] == L[j] is printed.
#4  The function would do roughly n^2 operations



#Task 4
#Prog Ex 1

# It will find the position for the value of v that is largest (closest to the end) since it starts searching
# from the end of the list.



#Task 5  min_or_max function
#Prog Ex 2

# On a list of size n, the function would do a number of operations that is O(n) linear.



#Task 6
# nlogn = n and you find out where they intersect 



# Task 7  Selection Sort
# It finds the minimum and inserts it at the beginning and repeats for the next position.

# List = [6,5,4,3,7,1,2]

# After each iteration of the loop the list will be:

# i=1  [1,5,4,3,7,6,2]  
# i=2  [1,2,4,3,7,6,5]
# i=3  [1,2,3,4,7,6,5]
# i=4  [1,2,3,4,5,6,7]



