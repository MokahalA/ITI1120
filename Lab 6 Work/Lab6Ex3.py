def first_neg(lst):
        '''(lst) -> int
Returns the index of the first negative number in the list that is entered.

Precondition: Returns None if the list is empty or there are no negative numbers
in the list.'''
        
        count=0
        i=0
        while lst != [] and lst[i] > 0 and i< len(lst)-1:
                count += 1
                i=i+1
        if count != len(lst)-1 and lst !=[]:
                return count
     


#Test examples
        
print(first_neg([2,3,-1,4,-2]))
print(first_neg([2,3,1,4,2]))
print(first_neg([]))
