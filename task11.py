import math

AP_Series = [2, 5, 8, 11, 15, 17]
GP_Series = [3, 6, 9, 12, 16, 18]

# For A.P series
diff = AP_Series[1] - AP_Series[0]   
for i in range(1,len(AP_Series)):
    if eval(f'{AP_Series[i]} - {AP_Series[i-1]}') == diff:
        continue
    else:
        AP_Series[i] = AP_Series[i-1] + diff
print(f'correct A.P : {AP_Series}')

# For G.P series
ratio = GP_Series[1] / GP_Series[0]   
for i in range(1,len(GP_Series)):
    if eval(f'{GP_Series[i]} / {GP_Series[i-1]}') == ratio:
        continue
    else:
        GP_Series[i] = int(GP_Series[i-1] * ratio)
print(f'correct G.P : {GP_Series}')