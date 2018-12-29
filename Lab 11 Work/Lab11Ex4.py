def is_palindrome_v2(s):
    """(str) -> bool
    Return whether or not a string is a palindrome. While ignoring
    letters not of the english alphabet
    """
    #Just 1 letter so its a palindrome
    if len(s) <= 1:
        return True
    
    #First letter is not in the alphabet
    if not s[0].isalpha():
        return is_palindrome_v2(s[1:])

    #Last letter is not in the alphabet
    if not s[-1].isalpha():
        return is_palindrome_v2(s[:-1])

    # Comparing first and last letter to see if they are the same.
    if s[0].casefold() != s[-1].casefold():
        return False
    
    return is_palindrome_v2(s[1:-1])


#test


print(is_palindrome_v2("A man, a plan, a canal -- Panama!"))   # True
print(is_palindrome_v2("Go hang a salami, I'm a lasagna hog")) # True
print(is_palindrome_v2("Madam, I'm Adam"))  # True
print(is_palindrome_v2("Madam, I'm"))       # False 
print(is_palindrome_v2('blurb'))            # False
print(is_palindrome_v2('a'))                # True
print(is_palindrome_v2('Anna'))             # True
