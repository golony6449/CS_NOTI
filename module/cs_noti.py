import time
import urllib.request
from datetime import datetime
import os

from module import base
from module import short_url
from bs4 import BeautifulSoup

from module import tele_api


class CsNotification(base.BaseNotifier):
    def __init__(self):
        super().__init__()

        self.mode = 'CS'
        self.load_id()
        self.channel = os.environ["CS_CHANNEL"]

    def run(self):
        url = 'http://cs.gnu.ac.kr/csadmin/sub.do?robot=Y&mCode=MN0038'
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')

        except urllib.error.HTTPError:
            print('CS_NOTI: ERROR OCCURRED during scraping (Network)', datetime.now())
            return
        except:
            print('CS_NOTI: ERROR OCCURRED during scraping', datetime.now())
            return

        html.close()
        titleList = self.findNotification(soup)

        if titleList is False:
            print('CS_NOTI: There is no notification.', datetime.now())
            # self.check()

        else:
            for title in titleList:
                # print(title['title'])
                short=short_url.make_short(url + '&' + title['url'][1:]) # String slice for delete '?' character

                tele = tele_api.Telegram(self.channel)
                tele.notification(title['title'], short)
                print('CS_NOTI: NEW NOTIFICATION.')
                self.save_id()

    def findNotification(self, target):
        notiList = list()
        title_list = target.find_all('tr', class_='isnotice')

        if len(title_list) > self.noticeId:
            for i in range(len(title_list) - self.noticeId):
                # print(title_list[i].contents[3].contents[1].attrs['title'])
                notiList.append({'title': title_list[i].contents[3].contents[1].attrs['title'],
                                 'url': title_list[i].contents[3].contents[1].attrs['href']})

            self.noticeId = len(title_list)     # Update ID

        title_list = target.find_all('tr', class_='child_1')
        newestNumber = int(title_list[0].contents[1].text)

        if newestNumber > self.id:
            for i in range(newestNumber - self.id):
                # print(title_list[i].contents[3].contents[1].attrs['title'])
                notiList.append({'title': title_list[i].contents[3].contents[1].attrs['title'],
                                 'url': title_list[i].contents[3].contents[1].attrs['href']})
            self.id = newestNumber  # Update ID
        if len(notiList) == 0:
            return False
        else:
            return notiList

    def send(self, title, url):
        tele = tele_api.Telegram('@Testing77')  # Should Edit at live server

        short = short_url.make_short(url)
        tele.notification(title[i], short)
        print('CS_NOTI: NEW NOTIFICATION. ID:', self.id)
        self.id += 1
        self.save_id()

    def save_id(self):
        path = self.root + '/source/last_cs'
        super().save(self.id, path)

        path = self.root + '/source/last_cs_notice'
        super().save(self.noticeId, path)

    def load_id(self):
        path = self.root + '/source/last_cs'
        self.id = super().load(path)

        path = self.root + '/source/last_cs_notice'
        self.noticeId = super().load(path)

    def extractId(self, titleList):
        title_list = titleList
        newNoti = []
        count = 0
        for i in title_list:
            temp = i.find_all('img', alt='새글')
            if len(temp) == 1:
                newNoti.append(count)
            count = count + 1
        return newNoti