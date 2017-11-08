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

# memoization
def memFib(n, memo = {0:0, 1:1}):
    if n not in memo:
        memo[n] = memFib(n-1, memo) + memFib(n-2, memo)
    return memo[n]

depth = 100

start = time.time()

print(fib(depth))
fibTime = time.time()
print(bottomUpFib(depth)[-1]) # gets last element
bottomUpTime = time.time()
print(memFib(depth))
memTime = time.time()

print("Fib Time: " + str(fibTime-start))
print("Bottom-Up Time: " + str(bottomUpTime-fibTime))
print("Memoization Time: " + str(memTime-bottomUpTime))
