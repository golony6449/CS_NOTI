import urllib.request
from datetime import datetime

from module import base
from module import short_url
from bs4 import BeautifulSoup

from module import tele_api


class agencyNotification(base.baseNotifier):
    def __init__(self):
        super().__init__()

        self.mode='Agency'
        self.load_id()

    def run(self):
        url = 'http://www.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=10303&boardNo=' + str(self.id)
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')
            title_list = soup.find_all('h3')
        except:
            print('AGENCY_NOTI: ERROR OCCURED during scraping', datetime.now())
            return

        html.close()
        noti_title = self.parse_title(title_list, findAllIndex=3)  # at Agency Notice, Index is 3.

        if noti_title == False:
            print('AGENCY_NOTI: There is no notification. ID:', self.id, datetime.now())
            self.check()

        else:
            noti_title = '[기관공지]\n' + noti_title
            short = short_url.makeShort(url)
            tele = tele_api.Telegram('@Testing77')  #Should Edit at live server
            tele.notification(noti_title, short)
            print('AGENCY_NOTI: NEW NOTIFICATION. ID:', self.id)
            self.id += 1
            self.save_id()

    def save_id(self):
        path = self.root + '\source\last_agency'
        super().save(self.id, path)

    def load_id(self):
        path = self.root + '\source\last_agency'
        self.id = super().load(path)
