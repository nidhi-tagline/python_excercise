# patterns
# ** **
# *   *
#      
# *   *
# ** **

n = 2
for i in range(n):
    for j in range(n-i,0,-1):
        print('*',end='')
    for _ in range(i+1):
        print('  ',end='')
    for j in range(n-i,0,-1):
        print('*',end='')
    print()
for i in range(n+1):
    for j in range(i):
        print('*',end='')
    for _ in range(n-i,-1,-1):
        print('  ',end='')
    for j in range(i):
        print('*',end='')
    print()

print()

#   *  
#  *** 
# *****
#  *** 
#   *  

n = 3
for i in range(1,n+1):
    for _ in range(n-i):
        print(' ',end='')
    for j in  range(2*i - 1):
        print('*',end='')
    print()
for i in range(1,n):    
    for _ in range(i):
        print(' ',end='')
    for j in range(2*((n-1)-i)+1):
        print('*',end='')
    print()
    
print()

# *
# * *
# *   *
# *     *
# * * * * *   

n = 5
for i in range(1,n+1):
    for j in range(i):
        if j == i-1 or j == 0 or i == n:
            print('* ',end='')
        else:
            print(end='  ')
            
    print()
 
print()  

# * * * * *
# *       *
# *       *
# *       * 
# * * * * *

n=5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print(end='* ')
        else:
            print(end='  ')
    print()

print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

a,n = 1,5
for i in range(n):
    for j in range(i+1):
        print(end=f"{a} ")
        a+=1
    print()