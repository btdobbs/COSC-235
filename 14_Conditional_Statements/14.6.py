grades = [0] * 101
grades[0:59] = 'F' * 60
grades[60:69] = 'D' * 10
grades[70:79] = 'C' * 10
grades[80:89] = 'B' * 10
grades[90:100] = 'A' * 11


def letter_grade(score):
    if score < 0 or score > 100:
        return None
    return grades[score]


def main():
    print(letter_grade(101))
    print(letter_grade(100))
    print(letter_grade(90))
    print(letter_grade(89))
    print(letter_grade(80))
    print(letter_grade(79))
    print(letter_grade(70))
    print(letter_grade(69))
    print(letter_grade(60))
    print(letter_grade(59))
    print(letter_grade(0))
    print(letter_grade(-1))


main()
