import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# To get things started
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Variables for count, position, and actual index position 
count = int(input('Enter count: '))
position = int(input('Enter position: '))
index_pos = position - 1

# Print the 3rd link on each new page, then open that link and repeat the process as many times as specified in the count
while count > 0:
    tags = soup('a')
    next_name = tags[index_pos]
    print(next_name.get('href', None))
    url = next_name.get('href')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = count - 1

