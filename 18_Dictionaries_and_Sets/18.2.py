def unique_items(lst):
    item_set = set()
    for item in lst:
        item_set.add(item)
    return len(lst) == len(item_set)


def main():
    print(unique_items([1, 2, 3, 4]))
    print(unique_items([1, 2, 2, 3, 4]))


main()

