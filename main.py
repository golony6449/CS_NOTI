#-*- coding: utf-8 -*-

import urllib
import tele_api
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime
import short_url
import sys

def main():
    interval = 5
    option=mode_select()
    try:
        cs_id=save_load(rw='r',mode='cs')
        gnu_id=save_load(rw='r',mode='gnu')
    except:
        #Failsafe
        cs_id=830
        gnu_id=3320

    if option=='all':
        while True:
            cs_id=cs_noti(cs_id)
            gnu_id=gnu_noti(gnu_id)
            time.sleep(interval)
    elif option=='cs':
        while True:
            cs_id=cs_noti(cs_id)
            time.sleep(interval)
    elif option=='gnu':
        while True:
            gnu_id=gnu_noti(gnu_id)
            time.sleep(interval)
    else:
        print 'ERROR: Incorrect Mode Please check again'
        exit()

def cs_noti(id):
    url = 'http://cs.gnu.ac.kr/sub02/06.php?id=' + str(id) + '&mode=read'
    try:
        html = urllib.urlopen(url)
        soup = BeautifulSoup(html, 'html5lib', from_encoding='utf-8')

        title_list = soup.find_all('td', 'tdleft')
        noti_title = parse_title(title_list)
    except:
        print 'CS_NOTI: ERROR OCCURED during scraping', datetime.now()
        time.sleep(10)
        cs_noti(id)
        noti_title=False

    if noti_title == False:
        print 'CS_NOTI: There is no notification. ID:', id, datetime.now()
    else:
        short = short_url.makeShort(url)
        tele = tele_api.Telegram('@CS_NOTI')
        tele.notification(noti_title, short)
        print 'CS_NOTI: NEW NOTIFICATION. ID:',id
        id += 1
        save_load(id, 'w','cs')
    return id

def gnu_noti(id):
    url = 'http://www.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=10026&boardNo=' + str(id)
    try:
        html = urllib.urlopen(url)
        soup = BeautifulSoup(html, 'html5lib')
        title_list = soup.find_all('h3')
        noti_title = parse_title(title_list,is_gnu=True)
    except:
        print 'GNU_NOTI: ERROR OCCURED during scraping', datetime.now()
        time.sleep(10)
        gnu_noti(id)
        noti_title=False

    if noti_title == False:
        # test
        print 'GNU_NOTI: There is no notification. ID:', id, datetime.now()
    else:
        short = short_url.makeShort(url)
        tele = tele_api.Telegram('@GNU_NOTI')
        tele.notification(noti_title, short)
        print 'GNU_NOTI: NEW NOTIFICATION. ID:',id
        id += 1
        save_load(id, 'w','gnu')
    return id

def parse_title(target,is_gnu=False):
    target_num=0
    if is_gnu==True:
        target_num=3
    source=str(target[target_num]).decode('utf-8')
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
    if start==end or len(source[start:end])<8:
        return False
    else:
        return source[start:end]

def save_load(para=0,rw='',mode=''):
    path=path=os.path.dirname( os.path.abspath( __file__ ) )
    if mode=='cs':
        if rw=='w' and para !=0:
            file=open(path+'\source\last_cs','w')
            file.write(str(para))
            return 0
        elif rw=='r':
            file=open(path+'\source\last_cs','r')
            loaded_value=file.readline()
            return int(loaded_value)

    elif mode=='gnu':
        if rw == 'w' and para != 0:
            file = open(path + '\source\last_gnu', 'w')
            file.write(str(para))
            return 0
        elif rw == 'r':
            file = open(path + '\source\last_gnu', 'r')
            loaded_value = file.readline()
            return int(loaded_value)
    # mode is not cs or gnu. or rw is not r or w
    print 'ERROR: Wrong parameter.'

def mode_select():
    if len(sys.argv)==1:
        print 'ERROR: There is no Parameter. Please check README'
    # mode=[all,cs,gnu]
    mode=[False,False,False]
    for a in sys.argv:
        if a=='all':
            mode[0]=True
        elif a=='cs':
            mode[1]=True
        elif a=='gnu':
            mode[2]=True
    if mode[1]==True and mode[2]==True:
        return 'all'
    if mode[0]==True:
        return 'all'
    elif mode[1]==True:
        return 'cs'
    elif mode[2]==True:
        return 'gnu'
# This case is occured when user enter incorrect option
    print 'ERROR:Please Enter Correct Option'
    exit()

if __name__=='__main__':
    main()
