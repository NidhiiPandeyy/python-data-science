# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    print(a, end =' ')
    while b < n:
        print(b, end =" ")
        a, b = b, a+b