from bs4 import BeautifulSoup
import requests
import html5lib

temp=requests.get('http://cs.gnu.ac.kr/csadmin/sub.do?mCode=MN0038')
temp2=BeautifulSoup(temp.text,'html5lib')
temp3=temp2.find_all('tr',class_='isnotice')
temp4=temp2.find_all('tr',class_='child_1')

for i in range(5):
    print(temp3[i].contents[3].contents[1].attrs['title'])

for i in range(10):
    print(temp4[i].contents[1].contents[0])
    print(temp4[i].contents[3].contents[1].attrs['title'])

temp=range(10)
for i in range(1):
    print(temp[i])