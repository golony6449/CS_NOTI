#-*- coding: utf-8 -*-

import urllib
import tele_api
from bs4 import BeautifulSoup
import time

def main():
    id = 828
    interval=5

    while True:
        url='http://cs.gnu.ac.kr/sub02/06.php?id='+str(id)+'&mode=read'
        html = urllib.urlopen(url)
        soup = BeautifulSoup(html,'html5lib',from_encoding='utf-8')

        title_list=soup.find_all('td','tdleft')
        noti_title=parse_title(title_list)

        if noti_title==False:
            #test
            print 'ERROR: There is no notification. ID:',id
            time.sleep(interval)
        else:
            #test
            #print id,'번째 공지사항: ',noti_title
            tele=tele_api.Telegram()
            tele.notification(noti_title,url)
            id+=1

def parse_title(target):
    source=str(target[0]).decode('utf=8')
    ouput=''
    start=0
    end=0

    for pointer in range(len(source)-1):
        if source[pointer] == '>':
            start = pointer+1
        try:
            if source[pointer] == '<' :
                end = pointer
        except:
            pass

#Check NULL contents
    if start==end:
        return False
    else:
        return source[start:end]


if __name__=='__main__':
    main()
