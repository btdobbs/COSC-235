def main():
    n = int(input("How many integers do you want to enter? "))
    odd_sum = 0
    for i in range(n):
        prompt = "Enter integer " + str(i + 1) + ": "
        x = int(input(prompt))
        if x % 2 == 1:
            odd_sum += 1
    print(odd_sum, "of the integers entered were odd.")


main()
