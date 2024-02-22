numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

print(f'\nList : {numbers}')
print('''\nChoose one of option below:
  A. Length of the list
  B. Display first 3 numbers
  C. Display sum of odd numbers
  D. Number of deplicate numbers
  E. Display list without duplicate numbers''')

choice = input('\nEnter your choice(A/B/C/D/E) : ')

if choice == 'A':
    print('Length of list is :', len(numbers))

elif choice == 'B':
    sublist = []
    for i in range(3):
        sublist.append(numbers[i])
    print(f'First 3 numbers : {sublist}')

elif choice == 'C':
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    print(f'Sum of odd numbers : {sum}')
    
elif choice == 'D':
    duplicate = set()
    for num in numbers:
        n = numbers.count(num)
        if n > 1:
           duplicate.add(num) 
    print(f'number of duplicate number : {len(duplicate)}')
    
elif choice == 'E':
    for num in numbers:
        count = numbers.count(num)
        if count > 1:
            numbers.remove(num)
    print(f'List without duplicate numbers : {numbers}')
    
else:
    print('Invalid choice..')