def is_eligible(age,citizenship,prison):
     '''(int,str,str) -> bool
returns "True" if the person is eligible to vote and "False" if they are not
eligible to vote.'''
     if age >=18 and citizenship == "Yes" or "YES" and prison== "No" or "no":
          return True
     else:
          return False

        





name=input("What is your name ? ")
age= int(input("What is your age ? "))
citizenship= input("Are you a Canadian citizen ? ")
prison= input("Are you currently serving time in prison ? ")



if is_eligible(age,citizenship,prison):
    print(name, ", you are eligible to vote")
else:
    print(name, ", you are ineligible to vote")
