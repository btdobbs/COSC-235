import random


# n - 1 comparisons for sorted input
# n - m comparisons for unsorted input where m is the first index of out of order condition
def is_sorted1(lst):
    result = True
    comp = 0
    for i in range(1, len(lst)):
        comp += 1
        if lst[i] < lst[i - 1]:
            result = False
            break
    print(comp, " comparisons")
    return result


# 2n-1 comparisons for sorted input
# 2(n-m) comparisons unsorted where m is the first index of out of order condition
def is_sorted2(lst):
    i = 1
    comp = 0
    while True:
        comp += 1
        if i >= len(lst):
            break
        comp += 1
        if lst[i - 1] > lst[i]:
            break
        i += 1
    print(comp, " comparisons")
    return i == len(lst)


def main():
    lst = list(range(1, 101))
    print("Sorted =", is_sorted1(lst))
    print("Sorted =", is_sorted2(lst))
    random.shuffle(lst)
    print("Sorted =", is_sorted1(lst))
    print("Sorted =", is_sorted2(lst))


main()
