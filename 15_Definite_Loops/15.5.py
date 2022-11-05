import math


def index_smallest_positive(lst):
    current_min = math.inf
    current_min_index = -1
    for i, n in enumerate(lst):
        if 0 < n < current_min:
            current_min_index = i
            current_min = n
    return current_min_index


def main():
    print(index_smallest_positive([-5, 0, 5, 4, 100, 1, 100, -10, 50, 1]))


main()
