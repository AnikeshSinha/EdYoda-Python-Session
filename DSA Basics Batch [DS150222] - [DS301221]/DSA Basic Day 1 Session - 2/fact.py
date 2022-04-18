def fact1(n):
    
    if n == 0:
        return 1
    return n * fact1(n-1)
    
n = int(input())
fact1(n)