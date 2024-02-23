from collections import Counter

names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
print(f'Names : {names}')

lengths = []
for name in names:
    lengths.append(len(name))
print(f'Name lengths : {lengths}')

lengths_count = Counter(lengths)

print('\nThe three most frequent name lengths are :')    
for length, count in lengths_count.most_common(3):
    name_list = [name for name in names if len(name) == length]
    print(f'{count} names of Length {length} : {name_list}')
    
print('\nThe three least frequent name lengths are :')
for length, count in lengths_count.most_common()[:-4:-1]:
    name_list = [name for name in names if len(name) == length]
    print(f'{count} names of Length {length} : {name_list}')    
    
    

 