import urllib.request
from datetime import datetime
import os

from module import base
from module import short_url
from bs4 import BeautifulSoup

from module import tele_api
from module import firebase


class GnuNotificationLegacy(base.BaseNotifier):
    def __init__(self):
        super().__init__()

        self.mode = 'GNU'
        self.id = None
        self.load_id()
        self.channel = os.environ["GNU_CHANNEL"]

    def run(self):
        url = 'http://www.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=10026&boardNo=' + str(self.id)
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')
            # title_list = soup.select_one('.title) # selector option (testing)
            title_list = soup.find_all('h3')

        except urllib.error.HTTPError:
            print('GNU_NOTI: ERROR OCCURRED during scraping (Network)', datetime.now())
            return

        except:
            print('GNU_NOTI: ERROR OCCURRED during scraping', datetime.now())
            return

        html.close()
        noti_title = self.parse_title(title_list, findAllIndex=3)  # at HOT NEWS, Index is 3.

        if noti_title is False:
            print('GNU_NOTI: There is no notification. ID:', self.id, datetime.now())
            self.check(soup)

        else:
            formated_title = '[HOT NEWS]\n' + noti_title
            short = short_url.make_short(url)
            tele = tele_api.Telegram(self.channel)
            tele.notification(formated_title, short)

            firebase.register_new_noti('HOT NEWS', noti_title, short)
            firebase.send_notification('HOT NEWS', noti_title)

            print('GNU_NOTI: NEW NOTIFICATION. ID:', self.id)
            self.id += 1
            self.save_id()

    def save_id(self):
        path = self.root + '/source/last_gnu'
        super().save(self.id, path)

    def load_id(self):
        path = self.root + '/source/last_gnu'
        self.id = super().load(path)


class GnuNotification(base.RssBaseNotifier):
    url = 'http://www.gnu.ac.kr/main/na/ntt/selectRssFeed.do?mi=1127&bbsId=1029'
    category = '학사'
    firebase_ch = 'gnu'
