####     Task 1     ####

def orange(n):
    if n > 0:
        print(n,end=" ")
        orange(n-2)

orange(10)

print()


def guava(n):
    if n > 0:
        guava(n-2)
        print(n,end=" ")

guava(10)

print()

## a) orange prints: 10 8 6 4 2
##    guava prints:  2 4 6 8 10

## b) orange: If n > 0 then n is printed and then reduced by 2 and this repeats itself. 
##    guava: If n > 0  then n is reduced by 2 and stored as n and then the n is printed from the last stack to first stack. 


####     Task 2     ####

def mulberry(n):
    if n == 1:
        return 1 
    else:
      return n + mulberry(n - 1) 

print( mulberry(1000) )

## a) It prints 10  (4+3+2+1)

## b) If n is not 1 then it reduces n by 1 and stores it until n reaches 1. Then it adds up all the stored numbers when it resumes the functions.

## c) If n is a negative number then it will loop infinitely because n will always become more negative and wont reach 1. 

## e) -The maximum number of functions on the stack is n
##    -It crashes for mulberry(1000) because it exceeds the python limit for stacks running.


####     Task 3     ####

def cantaloupe(n): 
    if n > 0:
        print( n % 10)
        cantaloupe(n // 10)     
    
cantaloupe(7254)

## a) It prints 4  5  2  7

## b) It prints the last digit of the number (remainder) and then integer divides the digit by 10 and repeats until there are no more digits. 
##  So it ends up printing the digits of the number in reverse.

## c) The max number of functions running at a time is equal to the number of digits in n or the len(n).


####     Task 4     ####

def almond(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        tmp=almond(lst[0:len(lst)-1])
        if tmp>lst[len(lst)-1]:
            return tmp
        else:
            return lst[len(lst)-1]

a = [2, 7, -11]
print( almond(a) )

## a) It prints 7

## b) Given a list, this function recursively reduces the list by 1 element until the list size is 1 then it returns the middle element in the list.





####     Task 5     ####

def fig(lst, high):
    if high == 0:
        return lst[0]
    else:
        tmp=fig(lst, high - 1)
        if tmp>lst[high]:
            return tmp
        else:
            return lst[high]

a = [2, 7, -11]
print( fig (a, len(a)-1) )

## a) It prints 7

## b) It returns the middle element in the list by making function calls to fig and reducing high by 1 each time, in each function call it stores the number in position l[high].

 



####     Task 6     ####

def nox(s, ch):
    if len(s)==0:
        return s
    elif s[0]==ch:
        return nox(s[1:], ch)
    else:
        return s[0]+nox(s[1:], ch)

print( nox('Cacic', 'c' ))

## a) It prints Cai 

## b) It removes all of the occurences of the given character from the string by reducing the string by 1 character in each function call until the length of the string is 0
##  and then it prints each removed character that is not == ch.



