import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

enabled = True
sum = 0
for match in re.findall('mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', ''.join(lines)):
    if match == 'do()':
        enabled = True
    elif match == 'don\'t()':
        enabled = False
    elif enabled and match.startswith('mul('):
        groups = re.findall('mul\(([0-9]+),([0-9]+)\)', match)
        for group in groups:
            sum += int(group[0]) * int(group[1])

print("sum = ", sum)