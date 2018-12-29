


def mess(phrase):
    '''(str) -> str
returns a string that is a new version of the phrase where the characters
r,s,t,v,w,x,y,z are capitalized if they are present and the spaces are replaced with '-\' '''

    vowels= ''
    for char in phrase:
        if char in "rstvwxyz":
            phrase = phrase.replace(char,char.upper())
        if char in " ":
            phrase = phrase.replace(char,'-')
            
    return phrase
