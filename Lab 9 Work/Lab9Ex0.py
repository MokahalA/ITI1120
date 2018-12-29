def get_year():
    '''(int) -> (int)
Returns the entered four digit year as an integer, if anything other than
a 4 digit integer is entered the user is prompted to enter again.'''
    
    n = ""
    
    while len(n) != 4:
        try:
            n = input("Enter a 4 digit year: ")
            if len(n) != 4:
                print("Please enter a four digit integer for the year")
            else:
                yr = int(n)
                
        except ValueError:
            print("Please enter a four digit integer for the year")
    return yr

print(get_year())
