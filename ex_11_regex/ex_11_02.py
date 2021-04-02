# extract revision numbers to get average
import re

fname = 'mbox.txt'
handler = open(fname)

rev_num = list()
# iterate through lines to collect revision numbers
for line in handler:
    numbers = re.findall('New Revision: ([0-9]+)', line)
    # iterate through list with multiple digits
    for i in range(len(numbers)):
        num = float(numbers[i])
        rev_num.append(num)
# print out the average of all list items
print(sum(rev_num) / len(rev_num))
