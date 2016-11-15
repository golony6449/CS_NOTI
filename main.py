#-*- coding: utf-8 -*-

import urllib
import tele_api
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime

def main():
    interval = 5
    try:
        id = save_load(rw='r')
    except:
        #Failsafe
        id=3270

    while True:
        url='http://www.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=10026&boardNo='+str(id)
        try:
            html = urllib.urlopen(url)
            soup = BeautifulSoup(html,'html5lib')

            title_list=soup.find_all('div','title')

            noti_title=parse_title(title_list)

            if noti_title==False:
                #test
                print 'NOTE: There is no notification. ID:',id,datetime.now()
                time.sleep(interval)
            else:
                #test
                #print id,'번째 공지사항: ',noti_title
                tele=tele_api.Telegram()
                tele.notification(noti_title,url)
                id+=1
                print 'send!'
                save_load(id,'w')
        except:
            print 'WARNING: ERROR OCCURED', datetime.now()
            time.sleep(10)

def parse_title(target):
    if len(target)==0:
        return False

    source=str(target[0]).decode('utf-8')
    ouput=''
    start=0
    end=0

    for pointer in range(50):
        if source[pointer] == '>':
            start = pointer+1

    for pointer in range(start,len(source)-1):
        if source[pointer] == '<' :
            end = pointer
            break

#Check NULL contents
    if start==end:
        return False
    else:
        return source[start:end]

def save_load(para=0,rw=''):
    path=path=os.path.dirname( os.path.abspath( __file__ ) )
    if rw=='w' and para !=0:
        file=open(path+'\source\last_id','w')
        file.write(str(para))

    elif rw=='r':
        file=open(path+'\source\last_id','r')
        loaded_value=file.read()
        return int(loaded_value)
    else:
        print 'ERROR: Wrong parameter.'

if __name__=='__main__':
    main()
