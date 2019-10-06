
import re

file = open('refrom.txt')
for line in file:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
