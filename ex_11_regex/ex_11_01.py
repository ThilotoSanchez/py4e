# count lines that match with regex
"""import re

fname = 'mbox.txt'
handler = open(fname)

user_regex = input('Enter a regular expression: ')

nrgx = 0
for line in handler:
    if re.findall(f'{user_regex}', line):
        nrgx += 1

print(f'{fname} had {nrgx} lines that matched {user_regex}')"""

#-----------------------------------------------
# 2nd version with input already written
import re

fname = 'mbox.txt'
handler = open(fname)

input = ['^Author', '^X-', 'java$']

for i in range(len(input)):
    nrgx = 0
    for line in handler:
        if re.findall(input[i], line):
            nrgx += 1
    print(f'{fname} had {nrgx} lines that matched {input[i]}')
