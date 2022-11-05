import statistics
import games


def main():
    cube_die = games.CubeDie()
    rolls = []
    for i in range(1000):
        cube_die.roll()
        rolls.append(cube_die.get_top())
    print("Average roll:", statistics.mean(rolls))
    print("Standard Deviation of rolls:", statistics.stdev(rolls))


main()
