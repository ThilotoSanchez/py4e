# find all integers in text and sum 'em up
import re

while True:
    try:
        fname = input('Enter a file name: ')
        #if len(fname) < 1: fname = 'regex_sum_42.txt'
        if len(fname) < 1: fname = 'regex_sum_1196472.txt'
        handle = open(fname)
        break
    except:
        print("File not found. Try again")
        continue

num_lst = list()
# iterate through lines to find digits
for line in handle:
    numbers = re.findall('[0-9]+', line)
    # iterate through list with multiple digits
    for i in range(len(numbers)):
        num = int(numbers[i])
        num_lst.append(num)
# calculate sum of all items in list
print(sum(num_lst))
