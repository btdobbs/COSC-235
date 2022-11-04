def to_fahrenheit(temperature):
    return round(((9/5) * temperature) + 32, 1)


def main():
    print(to_fahrenheit(0), "°F")  # prints 32 °F
    print(to_fahrenheit(24), "°F")  # prints 75.2 °F
    print(to_fahrenheit(37), "°F")  # prints 98.6 °F
    print(to_fahrenheit(100), "°F")  # prints 212 °F


main()
