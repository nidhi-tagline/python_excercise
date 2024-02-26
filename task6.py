# count substring occurs in the given string.
import re

string = 'PQRQRQRQ'
substring = 'QRQ'
print(f'String: {string} \nSubstring: {substring}')

count = 0
for i in range(len(string)):
    result = re.match(substring,string[i:])
    if result :
        count += 1

print("Number of times substring appears in the given string: ", count)
