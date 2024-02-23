# a recursive function which returns the nth Fibonacci number
ans = [0 for i in range(1000)]
def fibonacci(n):  
    if n <= 1:
        return n
    
    if ans[n] != 0:
        return ans[n]
    else:
        ans[n] = fibonacci(n-1)+fibonacci(n-2)     
        return ans[n]
        
num = int(input('Enter number :'))
nth_num = fibonacci(num)
print(f'{num}th fibonacci number : {nth_num}')
