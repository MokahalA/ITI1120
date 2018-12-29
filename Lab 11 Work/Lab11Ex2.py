def count_digits(n):
    """(int) -> int
    Return the number of digits in the integer n.
    Precondition: n >= 0
    """
    if n // 10 == 0:
        return 1
    return 1 + count_digits(n//10)


#test

print(count_digits(0))          #1
print(count_digits(7))          #1
print(count_digits(73))         #2
print(count_digits(13079797))   #8
