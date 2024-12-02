import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]


def is_safe(l):
    return (all(l[i] < l[i + 1] and abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1)) or
            all(l[i] > l[i + 1] and abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1)))


safe = 0
for line in lines:
    safe += is_safe([int(x) for x in line.split(' ')])

print("safe = ", safe)