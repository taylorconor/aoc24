import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

word = "MAS"

def search_from(r, c, lines):
    if lines[r][c] != word[1]:
        return 0
    if not ((lines[r-1][c-1] == word[0] and lines[r+1][c+1] == word[2]) or (lines[r-1][c-1] == word[2] and lines[r+1][c+1] == word[0])):
        return 0
    if not ((lines[r-1][c+1] == word[0] and lines[r+1][c-1] == word[2]) or (lines[r-1][c+1] == word[2] and lines[r+1][c-1] == word[0])):
        return 0
    return 1

count = 0
for r in range(1, len(lines)-1):
    for c in range(1, len(lines[r])-1):
        count += search_from(r, c, lines)

print("count = ", count)