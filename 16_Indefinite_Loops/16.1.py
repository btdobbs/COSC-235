def main():
    count = 0
    n = 0
    while n != "":
        n = input("Enter a number: ")
        if n != "" and int(n) % 2 == 1:
            count += 1

    print(count,"odd numbers were entered")


main()
