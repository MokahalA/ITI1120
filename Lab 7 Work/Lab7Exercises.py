#5.16

def indexes(word,char):
    '''(str,str) -> list
Returns the positions of a character in a given string'''
    res=[]
    for n in range(len(word)):
        if word[n] == char:
            res.append(n)
    return res
            
            
#test examples
print(indexes('mississippi','s'))
print(indexes('mississippi','i'))
print(indexes('mississippi','a'))
print(" ")


#5.17

def doubles(lst):
    '''(list) -> str
Returns the integers in the given list that are exactly twice the previous int
in the list'''
    
    i=-1
    for num in range(1,len(lst)):
        i=i+1
        if lst[num] == 2*int(lst[i]):
            print(lst[num])
    return (" ")


#test example
print(doubles([3,0,1,2,3,6,2,4,5,6,5]))



#5.18

def four_letter(lst):
    '''(lst) -> lst
Returns a list of all the four letter words in a given list'''
    sub_list=[]
    for word in lst:
        if len(str(word)) == 4:
            sub_list.append(str(word))
    return sub_list


#test example
print(four_letter(['dog','letter','stop','door','bus','dust']))



print(" ")

#5.19

def inBoth(lst1,lst2):
    '''(lst,lst) -> bool
Returns True if there is an item in common between both given lists,
otherwise returns False'''
    for a in lst1:
        for b in lst2:
            if a == b:
                return True
    return False


#test example           
print(inBoth([3,2,5,4,7],[9,0,1,3]))
print(inBoth([3,2,5],[9,0,1]))

print(" ")

#5.20

def intersect(lst1, lst2):
    '''(list,list) -> list
Returns a list of the values that are present in both given lists'''
    
    l=[]
    for i in lst1:
        if i in lst2 and i in lst1:
            l.append(i)
    return l


#test example
print(intersect([3,5,1,7,9],[4,2,6,3,9]))
                

print(" ")


#5.21

def pair(lst1,lst2,n):
    '''(list,list,int) -> str
Prints the pairs of integers from the first and second lists that add up to n '''
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] + lst2[j] == n:
                print(lst1[i], lst2[j])
    return " "

#test example
print(pair([2,3,4],[5,7,9,12],9))



#5.22

def pairSum(lst,n):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j] == n:
                print(i, j)
    return " "

#test example
print(pairSum([7,8,5,3,4,6],11))


print(" ")

#5.29

def lastfirst(lst):
    first_names=[]
    last_names=[]
    both=[]
    for i in range(len(lst)):
        first_names.append(((lst[i]).split())[1])
        last_names.append(((lst[i].split())[0]).strip(','))
    both.append(first_names)
    both.append(last_names)
    return both

#test example
print(lastfirst(['Gerber, Len','Fox, Kat','Dunn, Bob']))
        
print(" ")

#5.31

def subsetSum(lst,n):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                if lst[i] + lst[j] + lst[k] == n:
                    return True
    return False

#test example

print(subsetSum([5,4,10,20,15,19],38))
print(subsetSum([5,4,10,20,15,19],10))


print(" ")


#5.33

def mystery(n):
    count=0
    while n != 1:
        count=count+1
        n//=2   
    return count

#test examples

print(mystery(4))
print(mystery(11))
print(mystery(25))

print(" ")


#5.46

def inversions(s):
        count = 0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] > s[j]:
                    count +=  1
        return count

#test examples
print(inversions('ABBFHDL'))
print(inversions('ABCD'))
print(inversions('DCBA'))

print(" ")



#5.48

def sublist(lst1,lst2):
    for i in range(len(lst1)):
        if lst2.index(lst1[i]) < lst2.index(lst1[i+1]) and lst2.index(lst1[i+1]) < lst2.index(lst1[i+2]):
            return True
        else:
            return False
        
#test examples
print(sublist([15,1,100],[20,15,30,50,1,100]))
print(sublist([15,50,20],[20,15,30,50,1,100]))

print(" ")


#5.37

def mssl(lst):
    max_end = max_current =0
    for i in lst:
        max_end = max(0,max_end + i)
        max_current = max(max_current, max_end)
    return max_current


#test examples
print(mssl([3,4,5]))
print(mssl([4,-2,-8,5,-2,7,7,2,-6,5]))
print(mssl([-2,-3,-5]))
    
    
