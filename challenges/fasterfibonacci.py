import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def bottomUpFib(n):
        fibs = [0, 1]
        for i in range(2, n+1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs



depth = 7

print(fib(depth))
print(memFib(depth))
print(bottomUpFib(depth)[-1]) # gets last element
