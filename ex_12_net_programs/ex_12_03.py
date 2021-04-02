# retrieving document from url
# display <= 3000 characters and count all char

import urllib.request, urllib.parse, urllib.error

url = 'http://data.pr4e.org/intro.txt'

fhand = urllib.request.urlopen(url)
count = 0
max = 3000

# show limited amount of characters
for line in fhand:
    line_length = len(line.decode())
    if count + line_length > max: break
    count += len(line.decode())
    print(line.decode().rstrip('\n'))
print('Shown characters:', count)
total_chars = 0

# count characters in whole file
for line in fhand:
    total_chars += len(line.decode())
print('Total characters:', total_chars)
