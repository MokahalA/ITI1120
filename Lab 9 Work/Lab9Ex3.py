def first_one(L):
    '''(list) -> int
Returns position of first 1 in the list '''
    
    start = 0
    end = len(L) -1

    while end - start > 1:
        mid = (start + end)//2
        key = L[mid]
        if key == 0:
            start = mid+1
        elif key == 1:
            end = mid -1
    if L[start] == 1:
        return start
    elif L[end] == 1:
        return end
    return -1

#test example:
print(first_one([0,0,0,0,0,0,1,1]))
# >> 6
print(first_one([1,1]))
# >> 0 
print(first_one([0,0,0]))
# >> -1

print(" ")

def last_zero(L):
    '''(list) -> int
Returns the position of last 0 in the list '''
    
    start = 0
    end = len(L) -1
    while end - start > 1:
        mid = (start + end)//2
        key = L[mid]
        if L[start] == 1:
            return start -1
        if key == 1:
            end = mid -1
        elif key == 0:
            start = mid + 1
    if L[end] == 0:
        return end
    elif L[start] == 0:
        return start
    elif L[start] == 1:
        return start -1
    return first_one(L)-1

#test

print(last_zero([0,0,0,0,0,0,1,1]))
# >> 5
print(last_zero([1,1]))
# >> -1
print(last_zero([0,0,0]))
# >> 2
