def fact(n):
    if n == 0: #base case
        return 1
    
    return n * fact(n-1)# recursive case 
    
import sys
sys.setrecursionlimit(3000)

n = int(input())
fact(n)