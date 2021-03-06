# an implementation with while loop
def linear_search_v1(lst, value):
     """ (list, object) -> int
     Return the index of the first occurrence of value in lst, or return
     -1 if value is not in lst.
     >>> linear_search_v1([2, 5, 1, -3], 5)
     1
     >>> linear_search_v1([2, 4, 2], 2)
     0
     >>> linear_search_v1([2, 5, 1, -3], 4)
     -1
     >>> linear_search_v1([], 5)
     -1
     """

     i = len(lst)-1  
     k = -1
     while i != -1:
          if lst[i] == value:
               return i
          else:    
               i= i-1
     return k
#test
print(linear_search_v1([2, 4, 2], 2))
# >> 2
     

# an implementation with for loop
def linear_search_v2(lst, value):
     """ same docstring as above
     """
     k= -1
     for i in range(len(lst)-1,-1,-1):
          if lst[i] == value:
               return i
     return k

#test
print(linear_search_v2([2, 4, 2], 2))
# >> 2


# an implementation with sentinel

# all three versions are correct and do roughly n operations on a list of size n
# the following solution uses no branching (i.e. if statements)

def linear_search_v3(lst, value):
     """ same docstring as above
     """     
     lst.insert(0,value)
     i=len(lst)-1
     # Keep going until we find value.
     while lst[i] != value:
          i-=1
     # Remove the sentinel.
     lst.pop(0)
     
     return i-1

#test
print(linear_search_v3([2, 4, 2], 2))
# >> 2


