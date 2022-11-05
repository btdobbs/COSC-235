def collatz(n):
    seq = []
    while True:
        seq.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return seq


def main():
    s1 = collatz(1)
    print(s1)
    s3 = collatz(3)
    print(s3)


main()
