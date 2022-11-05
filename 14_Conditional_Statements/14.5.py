def letter_grade(score):
    if score > 100:
        print("1 comparisons")
        return None
    if score >= 90:
        print("2 comparisons")
        return 'A'
    if score >= 80:
        print("3 comparisons")
        return 'B'
    if score >= 70:
        print("4 comparisons")
        return 'C'
    if score >= 60:
        print("5 comparisons")
        return 'D'
    if score >= 0:
        print("6 comparisons")
        return 'F'
    print("6 comparisons")
    return None


def main():
    print(letter_grade(101))
    print(letter_grade(100))
    print(letter_grade(95))
    print(letter_grade(90))
    print(letter_grade(85))
    print(letter_grade(80))
    print(letter_grade(75))
    print(letter_grade(70))
    print(letter_grade(65))
    print(letter_grade(60))
    print(letter_grade(55))
    print(letter_grade(0))
    print(letter_grade(-1))


main()
