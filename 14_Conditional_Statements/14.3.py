def middle(a, b, c):
    mid_value = None
    if (a >= b >= c) or (c >= b >= a):
        return b
    if (b >= a >= c) or (c >= a >= b):
        return a
    if (b >= c >= a) or (a >= c >= b):
        return c
    return mid_value


def main():
    # test all numbers are different
    print(middle(10, 20, 30))
    print(middle(10, 30, 20))
    print(middle(20, 10, 30))
    print(middle(20, 30, 10))
    print(middle(30, 10, 20))
    print(middle(30, 20, 10))
    # test two numbers are same
    print(middle(30, 20, 20))
    print(middle(20, 30, 20))
    print(middle(20, 20, 30))
    # test all numbers are same
    print(middle(30, 30, 30))


main()
