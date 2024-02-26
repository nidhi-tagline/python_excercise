# patterns
# ** **
# *   *
#      
# *   *
# ** **

for i in range(2):
    for j in range(2-i,0,-1):
        print('*',end='')
    for _ in range(i+1):
        print('  ',end='')
    for j in range(2-i,0,-1):
        print('*',end='')
    print()
    
for i in range(3):
    for j in range(i):
        print('*',end='')
    for _ in range(2-i,-1,-1):
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
 
for i in range(1, 4):
    for _ in range(3-i):
        print(' ',end='')
    for j in  range(2*i - 1):
        print('*',end='')
    print()
    
for i in range(1,3):    
    for _ in range(i):
        print(' ',end='')
    for j in range(2*(2-i)+1):
        print('*',end='')
    print()
    
print()
# *
# * *
# *   *
# *     *
# * * * * *   
for i in range(1,6):
    for j in range(i):
        if j == i-1 or j == 0 or i == 5:
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
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
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
a = 1
for i in range(5):
    for j in range(i+1):
        print(end=f"{a} ")
        a+=1
    print()