# expands https://www.py4e.com/code3/urllinks.py
# read html file, extract Href, scan for tags relative to first name in list
# follow link and repeat process until last file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

sample = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
actual = 'http://py4e-data.dr-chuck.net/known_by_Wilson.html'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
#url = actual
count = int(input('Enter count: '))
position = int(input('Enter position: '))
position -= 1
names = dict()

for i in range(count):
    # open and handle URL
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    #print('TAG:', tag)
    name = tags[position].contents[0]
    url = tags[position].get('href', None)
    #names[name] = names.get(name, 0) + url
    print('Retrieving:', tags[position].get('href', None))
