rock = 'rock'
paper = 'paper'
scissors = 'scissors'


def decide(choice1, choice2):
    if choice1 == choice2:
        return 0
    if (choice1 == paper and choice2 == rock) or (choice1 == rock and choice2 == scissors) or (
            choice1 == scissors and choice2 == paper):
        return 1
    else:
        return 2


def main():
    print(decide(rock, rock))
    print(decide(rock, paper))
    print(decide(rock, scissors))
    print(decide(paper, paper))
    print(decide(paper, scissors))
    print(decide(paper, rock))
    print(decide(scissors, scissors))
    print(decide(scissors, rock))
    print(decide(scissors, paper))


main()
