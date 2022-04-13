from mo1 import sum1



cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    
    startinglist = [ 0 , 1]
    for ele in range(2 , n):
        startinglist.append(startinglist[ele - 1] + startinglist[ele - 2])
        
    return startinglist
        
    # return a list of fibonacci numbers

print(__name__)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))