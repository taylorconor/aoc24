import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
word = "XMAS"

def is_valid(pos, lines):
    return 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[pos[0]])

def search_from(r, c, lines):
    if lines[r][c] != word[0]:
        return 0
    matches = 0
    for dir in dirs:
        letters = 0
        pos = (r, c)
        for letter in word[1:]:
            pos = (pos[0]+dir[0], pos[1]+dir[1])
            if not is_valid(pos, lines):
                break
            if lines[pos[0]][pos[1]] != letter:
                break
            letters += 1
        if letters == len(word)-1:
            matches += 1
    return matches

count = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        count += search_from(r, c, lines)

print("count = ", count)