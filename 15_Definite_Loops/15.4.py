import math


def smallest_positive(lst):
    current_min = math.inf
    for n in lst:
        if 0 < n < current_min:
            current_min = n
    return current_min


def main():
    print(smallest_positive([-5, 0, 5, 4, 100, 1, 100, -10, 50, 1]))
