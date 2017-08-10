import base
import time
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import short_url
import tele_api

class gnuNotification(base.baseNotifier):
    def __init__(self):
        super().__init__()

        self.load_id()

    def run(self):
        url = 'http://www.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=10026&boardNo=' + str(self.id)
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')
            title_list = soup.find_all('h3')
            noti_title = self.parse_title(title_list, findAllIndex=3)   # at HOT NEWS, Index is 3.
        except:
            print ('GNU_NOTI: ERROR OCCURED during scraping', datetime.now())
            time.sleep(10)
            return
            gnu_noti(self.id)
            noti_title = False

        if noti_title == False:
            # test
            print ('GNU_NOTI: There is no notification. ID:', self.id, datetime.now())
            if redirect == False:
                print ('Checking another ID')
                self.id = (gnu_noti(self.id + 1, redirect=True)) - 1
        else:
            noti_title = '[HOT NEWS]\n' + noti_title
            short = short_url.makeShort(url)
            tele = tele_api.Telegram('@Testing77')
            tele.notification(noti_title, short)
            print ('GNU_NOTI: NEW NOTIFICATION. ID:', self.id)
            self.id += 1
            self.save_id()

    def save_id(self):
        path=self.root+'\source\last_gnu'
        super().save(self.id,path)

    def load_id(self):
        path=self.root+'\source\last_gnu'
        self.id=super().load(path)