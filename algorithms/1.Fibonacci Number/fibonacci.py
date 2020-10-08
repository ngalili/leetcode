# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

# original algorithm
def __fibonacci(num):
    if num <= 0:
        print("Incorrect!")
    elif num == 1:
        return 0 
    elif num == 2:
        return 1
    else:
        return __fibonacci(num-1) + __fibonacci(num-2)

def fibonacci(num: int) -> int:
        a, b, counter = 0, 1, 0
        while True:
            if (counter > num): return
            yield a
            a,b = b, a+b
            counter += 1

# optimized algorithm         
def fib(N: int) -> int:
    f = fibonacci(N)
    for last in f:
        pass
    return last

if __name__ == "__main__":
    print(fib(3))