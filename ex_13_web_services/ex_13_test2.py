# prompt for URL, read JSON using urllib
# parse and extract the comment count
# compute the sum

import json
import urllib.request, urllib.parse, urllib.error

sample = 'http://py4e-data.dr-chuck.net/comments_42.json'
actual = 'http://py4e-data.dr-chuck.net/comments_1196477.json'

# url = input('Enter URL: ')
url = actual

# open websocket using urllib, read json and save it
connect = urllib.request.urlopen(url)
data = connect.read().decode()
info = json.loads(data)
print('Len:', len(info))
#print(json.dumps(info, indent=2))

sum = 0

# iterate through list, read out count and sum it
for item in info['comments']:
    count = item['count']
    print('Count:', count)
    sum += count
print('Sum:', sum)
