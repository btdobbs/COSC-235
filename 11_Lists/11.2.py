import statistics

input_line = input('Enter quiz scores separated by spaces: ')
input_line = input_line.replace(",", " ")
scores = [int(s) for s in input_line.split()]
average_score = statistics.mean(scores)
standard_deviation = statistics.stdev(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)
print('The average score is', average_score, end='.\n')
print('The standard deviation of scores is', standard_deviation, end='.\n')
print('The median of scores is', median, end='.\n')
print('The mode of scores is', mode, end='.\n')
