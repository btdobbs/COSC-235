import random


def pick(hopper):
    i = random.randrange(len(hopper))
    number = hopper[i]
    del hopper[i]
    return number


def main():
    wb_hopper = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
    rb_hopper = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    wb1 = pick(wb_hopper)
    wb2 = pick(wb_hopper)
    wb3 = pick(wb_hopper)
    wb4 = pick(wb_hopper)
    wb5 = pick(wb_hopper)
    rb = pick(rb_hopper)
    print('Picks:', wb1, wb2, wb3, wb4, wb5, rb)


main()
