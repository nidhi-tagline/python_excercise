# find out the pairs that have sum = n
from itertools import combinations

numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = int(input('Enter number :'))

combinationList = [[a,b] for [a,b] in combinations(numbers, 2) if a+b == n ]
uniqueCombination = []
for [a,b] in combinationList:
    if [a,b] in uniqueCombination or [b,a] in uniqueCombination:
        continue
    else:
        uniqueCombination.append([a,b])

print(f'pairs that have sum = {n} : {uniqueCombination}')
