def max_of_3(a, b, c):
    max_value = None
    if a > b > c:
        max_value = a
    if a > c > b:
        max_value = a
    if b > a > c:
        max_value = b
    if b > c > a:
        max_value = b
    if c > a > b:
        max_value = c
    if c > b > a:
        max_value = c
    return max_value


def max_of_3_with_equals(a, b, c):
    max_value = None
    if a >= b >= c:
        max_value = a
    if a >= c >= b:
        max_value = a
    if b >= a >= c:
        max_value = b
    if b >= c >= a:
        max_value = b
    if c >= a >= b:
        max_value = c
    if c >= b >= a:
        max_value = c
    return max_value


def main():
    print(max_of_3(3, 3, 5))  # prints None
    print(max_of_3_with_equals(3, 3, 5))  # prints 5


main()
