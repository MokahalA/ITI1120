for i in range(5,0,-1):
     num=1
     for j in range (1,i+1):
          print(num, end="| ")
          num=num*2
     print()


#range of i is 5,4,3,2,1

#First line i=5 and range of j is (1,6) it prints 1, 2, 4, 8, 16
#Second line i= 4 and range of j is (1,5) it prints 1, 2, 4, 8
#Third line i= 3 and range of j is (1,4) it prints 1, 2, 4
#Fourth line i= 2 and range of j is (1,3) it prints 1, 2
#Fifth line i = 1 and range of j is (1,2) it prints 1
# Each number is separated by a "|"
