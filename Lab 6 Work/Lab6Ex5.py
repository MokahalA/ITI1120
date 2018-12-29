n=int(input("Enter a positive even integer for the size of the list? " ))

import random 

#1 list of length n filled with zeros

a=[ ]
print(a+(n*[0]))      #method 1 


print((a+[0])*n)      #method 2
                          


#2 list b of length n filled with random integers between  1 and 100


b=[ ]                           #method 1 (for loop)
for i in range(n):
    b.append(random.randrange(1,101))

print(b)



b2=[]                           #method 2 (while loop)
i=0
while i < n:
    i=i+1
    b2.append(random.randrange(1,101))
    
print(b2)



#3 Creating a variable that is an alias of the list

c=b[:]
print(c)



#4 Set the first half of elements of c to zero and print both b and c

c[:n//2]=[0]*(n//2)
print(b)
print(c)

    

#5 Copy list b into a list d

d=b[:]                  #method 1
print(d)

d=b.copy()              #method 2
print(d)



#6 To create a list e that has every 2nd element of b

e=b[1::2]

print(e)




