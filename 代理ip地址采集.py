import requests
import re
from bs4 import BeautifulSoup as bs

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
        }

# url = 'https://www.kuaidaili.com/free/inha/1/'
# r = requests.get(url=url, headers=headers)
#
# soup = bs(r.content, 'lxml')
# data = soup.find_all(name='td', attrs={})
# soup1 = re.findall('<td data-title="IP">(.*?)</td>', r.text)
# print(soup1)

list =[]
for i in range(1, 4445):
    url = 'https://www.kuaidaili.com/free/inha/%s'%(i)
    r = requests.get(url=url, headers=headers)
    soup = bs(r.content, 'lxml')
    data = soup.find_all(name='td', attrs={})
    soup1 = re.findall('<td data-title="IP">(.*?)</td>', r.text)
    list.append(soup1)
print(list)


