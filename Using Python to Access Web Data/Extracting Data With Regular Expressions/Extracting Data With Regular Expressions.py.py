import re
file = open('regex_sum_847373.txt')
count = 0
addition = 0
for line in file:
    x = re.findall('([0-9]+)', line)  # regex condition
    l = len(x)  # length of list founde in each line
    for i in range(0, l):
        count += 1  # count loop for confirmation
        addition = addition + int(x[i])  # sum loop
print(addition, count)

# for sum in one line
print(sum([int(i) for i in re.findall('[0-9]+', open("regex_sum_847373.txt").read())]))
