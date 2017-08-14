import time
import urllib.request
from datetime import datetime

from module import base
from module import short_url
from bs4 import BeautifulSoup

from module import tele_api


class csNotification(base.baseNotifier):
    def __init__(self):
        super().__init__()

        self.load_id()

    def run(self):
        url = 'http://cs.gnu.ac.kr/sub02/06.php?id=' + str(self.id) + '&mode=read'
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')
            title_list = soup.find_all('h3')
        except:
            print('CS_NOTI: ERROR OCCURED during scraping', datetime.now())
            time.sleep(10)

        noti_title = self.parse_title(title_list, findAllIndex=3)  # at CS, Index is 3.

        if noti_title == False:
            print('CS_NOTI: There is no notification. ID:', self.id, datetime.now())
            self.check()

        else:
            noti_title = noti_title
            short = short_url.makeShort(url)
            tele = tele_api.Telegram('@Testing77')  #Should Edit at live server
            tele.notification(noti_title, short)
            print('CS_NOTI: NEW NOTIFICATION. ID:', self.id)
            self.id += 1
            self.save_id()

    def save_id(self):
        path = self.root + '\source\last_cs'
        super().save(self.id, path)

    def load_id(self):
        path = self.root + '\source\last_cs'
        self.id = super().load(path)
