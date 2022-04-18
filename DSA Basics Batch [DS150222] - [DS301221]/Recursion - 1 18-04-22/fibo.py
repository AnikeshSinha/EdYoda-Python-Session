def fib(n):
    if n == 1:
        return 1
    
    fib_n_1 = fib(n-1)
    fib_n_2 = fib(n-2)
    output = fib_n_1 + fib_n_2
    
    return output


n = 2
fib(n)