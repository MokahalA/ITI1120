def gcd(a,b):
    """(int, int) -> int
    Returns the greatest common denominator using euclid's algorithm
    Precondition a >= b, b > 0
    """
    #if remainder 0 then GCD is a
    if b == 0:
        return a
    
    return gcd(b, a % b) # gcd(a, b) = gcd(b, remainder) repeats until remainder is 0.


#test

print(gcd(36,20))     # 4



# The depth of recursion is 4 if called with the above test.
