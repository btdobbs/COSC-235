ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'


def decide(choice1, choice2):
    if choice1 == choice2:
        return 0
    if (choice1 == PAPER and choice2 == ROCK) or (choice1 == ROCK and choice2 == SCISSORS) or (
            choice1 == SCISSORS and choice2 == PAPER):
        return 1
    else:
        return 2


def main():
    print(decide(ROCK, ROCK))
    print(decide(ROCK, PAPER))
    print(decide(ROCK, SCISSORS))
    print(decide(PAPER, PAPER))
    print(decide(PAPER, SCISSORS))
    print(decide(PAPER, ROCK))
    print(decide(SCISSORS, SCISSORS))
    print(decide(SCISSORS, ROCK))
    print(decide(SCISSORS, PAPER))


main()
