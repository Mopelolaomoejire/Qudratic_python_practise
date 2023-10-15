n = int(input('enter positive numbers'))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial = factorial*i
        print(factorial)
