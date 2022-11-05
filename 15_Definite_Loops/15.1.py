def main():
    hour_sum = 0
    for day in range(7):
        prompt = "Enter hours worked on day " + str(day + 1) + ": "
        hour_sum += int(input(prompt))
    print(hour_sum, "total hour(s) worked")


main()
