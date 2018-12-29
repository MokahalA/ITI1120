def is_palindrome(s):
    """(str) -> bool
    Return whether or not a string is a palindrome.
    """
    if len(s) <= 1:
        return True

    if s[0].lower() != s[-1].lower():
        return False

    return is_palindrome(s[1:-1])


#test

print(is_palindrome('blurb'))    #False
print(is_palindrome('a'))        #True
print(is_palindrome('anna'))     #True
print(is_palindrome('Anna'))     #True
print(is_palindrome("A man, a plan, a canal -- Panama!"))   #False
print(is_palindrome("Madam, I'm Adam"))    #False
