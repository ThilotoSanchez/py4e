import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_1196476.xml'
uh = urllib.request.urlopen(url, context=ctx)

count = 0

data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Count:', len(lst))

for item in lst:
    #print('Name', item.find('name').text)
    item_count = int(item.find('count').text)
    count += item_count
    #print('Attribute', item.get('x'))
print('Sum:', count)
