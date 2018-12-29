
n1=int(input("Enter the first integer: "))
n2=int(input("Enter the second integer: "))
print(n1+n2)

answer=input("Would you like to perform the operation again? ")
answer=(answer.strip()).lower()


while answer == "yes" and answer !="no":
    n1=int(input("Enter the first integer: "))
    n2=int(input("Enter the second integer: "))
    print(n1+n2)
    answer=input("Would you like to perform the operation again? ")
    answer=(answer.strip()).lower()


    
