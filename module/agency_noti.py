import urllib.request
from datetime import datetime
import os

from module import base
from module import short_url
from bs4 import BeautifulSoup

from module import tele_api
from module import firebase


class AgencyNotification(base.BaseNotifier):
    def __init__(self):
        super().__init__()

        self.mode='Agency'
        self.id = None
        self.load_id()
        self.channel = os.environ["GNU_CHANNEL"]

    def run(self):
        url = 'http://www.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=10303&boardNo=' + str(self.id)
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')
            title_list = soup.find_all('h3')

        except urllib.error.HTTPError:
            print('AGENCY_NOTI: ERROR OCCURRED during scraping (Network)', datetime.now())
            return

        except:
            print('AGENCY_NOTI: ERROR OCCURRED during scraping', datetime.now())
            return

        html.close()
        noti_title = self.parse_title(title_list, findAllIndex=3)  # at Agency Notice, Index is 3.

        if noti_title is False:
            print('AGENCY_NOTI: There is no notification. ID:', self.id, datetime.now())
            self.check(soup)

        else:
            formated_title = '[기관공지]\n' + noti_title
            short = short_url.makeShort(url)
            tele = tele_api.Telegram(self.channel)
            tele.notification(formated_title, short)

            firebase.register_new_noti('기관공지', noti_title, short)
            firebase.send_notification('기관공지', noti_title)

            print('AGENCY_NOTI: NEW NOTIFICATION. ID:', self.id)
            self.id += 1
            self.save_id()

    def save_id(self):
        path = self.root + '/source/last_agency'
        super().save(self.id, path)

    def load_id(self):
        path = self.root + '/source/last_agency'
        self.id = super().load(path)
