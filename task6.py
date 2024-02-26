# count substring occurs in the given string.

string = 'PQRQRQRQ'
substring = 'QRQ'
print(f'String: {string} \nSubstring: {substring}\n')

str_list = []
for i in range(len(string)):
    str_list.append(string[i:i+len(substring)])
    if i == len(string)-len(substring):
        break

print(str_list)
count = str_list.count(substring)
print("Number of times substring appears in the given string: ", count)
