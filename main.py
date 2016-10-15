#-*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

def main():

    for id in range(822,830):

        url='http://cs.gnu.ac.kr/sub02/06.php?id='+str(id)+'&mode=read'
        html = urllib.urlopen(url)
        soup = BeautifulSoup(html,'html5lib',from_encoding='utf-8')

        title_list=soup.find_all('td','tdleft')
        noti_title=parse_title(title_list)

        print id,'번째 공지사항: ',noti_title

def parse_title(target):
    source=str(target[0]).decode('utf=8')
    ouput=''
    start=0
    end=0

    for pointer in range(len(source)-1):
        if source[pointer] == '>':
            start = pointer+1
        try:
            if source[pointer] == '<' and pointer > start:
                end = pointer
        except:
            pass
    return source[start:end]


if __name__=='__main__':
    main()