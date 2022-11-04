def max_of_3(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value


def main():
    # three numbers taken two at a time gives six combinations
    print(max_of_3(10, 20, 30))
    print(max_of_3(10, 30, 20))
    print(max_of_3(20, 10, 30))
    print(max_of_3(20, 30, 10))
    print(max_of_3(30, 10, 20))
    print(max_of_3(30, 20, 10))


main()
