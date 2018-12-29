def min_or_max_index(lst, boolean):
    """(list of numbers, bool) -> tuple of (number, int)
Returns the index (position) of the minimum or maximum and the minimum or maximum.
Preconditions: len(lst) >= 1 """
    if boolean:
        return my_min(lst)
    else:
        return my_max(lst)

#Above function calls either my_min or my_max depending on the boolean
    
def my_max(lst):
    """(list of numbers) -> (number,index)
Returns the maximum value in list and its index.
Preconditions: len(lst) >= 1 """
    maximum = lst[0]
    pos = 0
    for i in range(len(lst)):  #n 
        if lst[i] > maximum:
            maximum = lst[i]
            pos = i
    return (maximum, pos)

def my_min(lst):
    """(list of numbers) -> (number,index)
Returns the minimum value in list and its index.
Preconditions: len(lst) >= 1 """
    minimum = lst[0]
    pos = 0
    for i in range(len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]
            pos = i
    return (minimum, pos)


#Test example
print(min_or_max_index([1,2,3,4,5],True))
# >> (1,0)  minimum
print(min_or_max_index([1,2,3,4,5],False))
# >> (5,4)  maximum
