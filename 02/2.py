import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]


def is_safe(l):
    return (all(l[i] < l[i + 1] and abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1)) or
            all(l[i] > l[i + 1] and abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1)))


safe = 0
for line in lines:
    nums = [int(x) for x in line.split(' ')]
    if is_safe(nums):
        safe += 1
    else:
        for i in range(len(nums)):
            if is_safe(nums[:i] + nums[i+1:]):
                safe += 1
                break

print("safe = ", safe)