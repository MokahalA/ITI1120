#Ex Dict 1:

def letter2number_if(lgrade):
    '''(str) -> int
returns an integer that is the corresponding number grade for the given letter grade'''
    if lgrade == "A+":
        return 10
    if lgrade == "A":
        return 9
    if lgrade == "A-":
        return 8
    if lgrade == "B+":
        return 7
    if lgrade == "B":
        return 6
    if lgrade == "C+":
        return 5
    if lgrade == "C":
        return 4
    if lgrade == "D+":
        return 3
    if lgrade == "D":
        return 2
    if lgrade == "E":
        return 1
    if lgrade == "F":
        return 0
    
#test examples:
print(letter2number_if("A-"))
print(letter2number_if("E"))

print(" ")

def letter2number_dict(lgrade):
    '''(str) -> int
returns an integer that is the corresponding number grade for the given letter grade'''
    ng = {
    "A+":10,
    "A":9,
    "A-":8,
    "B+":7,
    "B":6,
    "C+":5,
    "C":4,
    "D+":3,
    "D":2,
    "E":1,
    "F":0,
    } 
    return ng[lgrade]
#test examples:
print(letter2number_dict("A-"))
print(letter2number_dict("E"))

print(" ")


#Ex Dict 2:

agencies={"CCC":"Civilian Conservation Corps",
          "FCC":"Federal Communications Commission",
          "FDIC":"Federal Deposit Insurance Corporation",
          "SSB":"Social Security Board",
          "WPA":"Works Progress Administration",
          }
#a
agencies["SEC"] = "Securities and Exchange Commission"

#b   
agencies["SSB"] = "Social Security Administration"

#c
agencies.pop("CCC",None)
agencies.pop("WPA",None)

print(agencies)

print(" ")


#6.5:

def lookup(phonebook):
    first_name=input("Enter the first name: ")
    last_name=input("Enter the last name: ")
    person = (first_name, last_name)
    if person in phonebook:
        return phonebook[person]
    else:
        print('The name you entered is unknown')


phonebook = {("Anna", "Karenina"):"(123)456-78-90",
                ("Yu","Tsun"):"(901)234-56-78",
                ("Hans","Castorp"):"(321)908-76-54",
                }

print(lookup(phonebook))
print(" ")

#Ex Dict 3:

def lookup_v2(phonebook):
        first=input("Enter the first name: ")
        last=input("Enter the last name: ")

        person = (last,first)
        if person in phonebook:
            return phonebook[person]
        else:
            print('The name you entered is not known')
            
phonebook2 = {('Smith', 'Jane'):'123-45-67',
              ('Doe','John'):['987-65-43','833-32-45'],
              ('Baker', 'David'):'567-89-01',
              }

print(lookup_v2(phonebook2))

print(" ")
print(" ")

#Ex Dict 4:
# reverse function implementation
def reverse(phonebook):
    
    reversePB= {}
    
    for key in phonebook:
        value = phonebook[key]
        reversePB[value] = key
    return reversePB
    
phonebook3 = {('Smith', 'Jane'):'123-45-67',
              ('Doe','John'):'987-65-43',
              ('Baker', 'David'):'567-89-01',
              }
print(reverse(phonebook3))


