

import urllib
from bs4 import BeautifulSoup

url='http://cs.gnu.ac.kr/sub02/06.php?id=830&mode=read'
html = urllib.urlopen(url)
soup = BeautifulSoup(html,'html5lib',from_encoding='utf-8')

title_list=soup.find_all('td','tdleft')

print
