import os, re
from functools import cmp_to_key

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

rules = [(int(s[0]), int(s[1])) for s in [l.split('|') for l in lines[:lines.index('')]]]
pages = [[int(y) for y in x.split(',')] for x in lines[lines.index('')+1:]]

order = {}
for r in rules:
    if r[0] not in order.keys():
        order[r[0]] = []
    order[r[0]].append(r[1])

def cmp(first, second):
    if first == second:
        return 0
    if first in order.keys() and second in order[first]:
        return -1
    return 1

sum = 0
for p in pages:
    s = sorted(p, key=cmp_to_key(cmp))
    if p == s:
        sum += p[len(p) // 2]

print(sum)