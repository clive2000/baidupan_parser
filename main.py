from bs4 import BeautifulSoup
import requests

# Init a requests session
req_session = requests.Session()

# Asks for baidupan share link
print('Please type in a baidupan sharable link, example: 链接:https://pan.baidu.com/s/XXX 提取码:1234')
baidupan_link = input()

url = 'http://pan.naifei.cc/' + f'?{baidupan_link}'

response = req_session.get(url);

soup = BeautifulSoup(response.text,"html5lib");

with open("links.txt",'w') as f:
    items = soup.select("tbody > tr >td > a")
    for item in items:
        print(item['href'])
        f.write(item['href']+'\n')

print('Done, results written into links.txt')