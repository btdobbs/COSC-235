import random


def rock_paper_scissors():
    lst = ['rock', 'paper', 'scissors']
    return random.choice(lst)


def main():
    print(rock_paper_scissors())
    print(rock_paper_scissors())
    print(rock_paper_scissors())
    print(rock_paper_scissors())


main()
