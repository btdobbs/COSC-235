# A program to display the first 9 Fibonacci numbers
def fib(n):
    # Input: an integer value n where n > 0
    # Return: the nth Fibonacci number blank
    curr = 1
    prev = 1
    for i in range(n - 2):
        curr, prev = curr + prev, curr
    return curr


for k in range(1, 10):
    print("Fibonacci #", k, ":", fib(k))
