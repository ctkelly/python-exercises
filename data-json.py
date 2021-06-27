import urllib.request, urllib.parse, urllib.error 
import json

url = input('Enter location: ')
data = urllib.request.urlopen(url)

info = json.loads(data.read())
print('Length: ',len(info))
dataset = info['comments']

numlist = list()
for pair in dataset:
    num = pair['count']
    numlist.append(num)

print(sum(numlist))
