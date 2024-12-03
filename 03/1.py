import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

sum = 0
for line in lines:
    groups = re.findall('mul\(([0-9]+),([0-9]+)\)', line)
    for group in groups:
        sum += int(group[0]) * int(group[1])

print("sum = ", sum)