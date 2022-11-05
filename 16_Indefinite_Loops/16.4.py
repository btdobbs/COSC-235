def main():
    lst = [1, 2, 3, 4, 5]
    print(lst)
    index = 0
    while index < len(lst):
        lst[index] = str(lst[index])
        index += 1
    print(lst)


main()
