from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://dr-chuck.com/'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

pcount = 0
# Retrieve all of the anchor tags
paragraphs = soup('p')
for paragraph in paragraphs:
    #print('Paragraph:', paragraph)
    #print('Contents:', paragraph.contents[0])
    pcount += 1
print('Paragraphs total:', pcount)
