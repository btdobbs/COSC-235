import random

hopper = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32,
          33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
          62, 63, 64, 65, 66, 67, 68, 69]
wb1 = random.choice(hopper)
hopper.remove(wb1)
wb2 = random.choice(hopper)
hopper.remove(wb2)
wb3 = random.choice(hopper)
hopper.remove(wb3)
wb4 = random.choice(hopper)
hopper.remove(wb4)
wb5 = random.choice(hopper)
hopper.remove(wb5)
rb = random.randint(1, 26)

print('Picks:', wb1, wb2, wb3, wb4, wb5, rb)
