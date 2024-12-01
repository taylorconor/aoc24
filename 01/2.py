import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

lhs = []
rhs = []
for line in lines:
    groups = re.findall('([0-9]+)\s+([0-9]+)', line)
    for group in groups:
        lhs.append(int(group[0]))
        rhs.append(int(group[1]))

lhs.sort()
rhs.sort()

sum = 0
for i in range(len(lhs)):
    sum += lhs[i] * rhs.count(lhs[i])

print("sum = ", sum)