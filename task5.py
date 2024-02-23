# find out the pairs that have sum = n

numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = int(input('Enter number :'))

uniqueNumber = set()
for i in numbers:
    uniqueNumber.add(i)
uniqueNumber = list(uniqueNumber)
combinationList = [[a,b] for a in uniqueNumber for b in uniqueNumber if a+b == n and a!=b]

uniqueCombination = []
for [a,b] in combinationList:
    if [b,a] in uniqueCombination:
        continue
    else:
        uniqueCombination.append([a,b])

print(f'pairs that have sum = {n} : {uniqueCombination}')
