# this program crawls an entered webpage
# it reads the <span> tags, counts them and sums their values up

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_1196474.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the spans
spans = soup('span')
count = 0
sum = 0
for span in spans:
    count += 1
    # Look at the parts of a span
    comments = int(span.contents[0])
    sum += comments
print('Count', count)
print('Sum', sum)
