import math


def main():
    n = int(input("Enter a number? "))
    if n <= 1:
        print(n, "is not prime")
        return
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            print(n, "is not prime")
            return
    print(n, "is prime")


main()
