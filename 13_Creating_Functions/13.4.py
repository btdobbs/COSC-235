def bmi(height, weight):
    return (703 * weight)/(height*height)


def main():
    person_height = float(input('Enter your height in inches: '))
    person_weight = float(input('Enter your weight in pounds: '))
    print(f'Your BMI is {bmi(person_height, person_weight)}')


main()
