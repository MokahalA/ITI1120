def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''
     
     if(not(is_square(m))): # if matrix is not square
          return False      # return False
     
     #Condition 1
     
     merged_list=[]
     for o in m:
          merged_list += o
     for l in range(len(merged_list)):
          for k in range(l+1,len(merged_list)):
                 if merged_list[l] == merged_list[k]:
                    return False
               
     #Condition 2
               
     diagonal1=0
     diagonal2=0
     col_sum=0
     row_sum=0
     c=len(m[0])-1
     for i in range(len(m)):
          for j in range(len(m[i])):
               if i == j:
                    diagonal1 = diagonal1 + m[i][j]
     for r in range(len(m)):
          diagonal2 = diagonal2 + m[r][c]
          c=c-1
     for a in range(0,1):
          for b in range(0,len(m)):
               row_sum=row_sum + m[a][b]
     for e in range(0,1):
          for f in range(0,len(m[0])):
               col_sum=col_sum + m[f][e]
     if col_sum == row_sum and diagonal1 == diagonal2:
          return True
     else:
        return False




# main
# TESTING OF magic functions

# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
