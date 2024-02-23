# recursion function that calculate the sum of numbers present in the list.
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]

def sum_of_elements(numList):
    if len(numList) == 0:
        return 0
    else:
        return numList[0] + sum_of_elements(numList[1:])
    
sum = sum_of_elements(numbers)
print(sum)
