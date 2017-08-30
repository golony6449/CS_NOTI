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

        self.mode = 'CS'
        self.load_id()

    def run(self):
        #url = 'http://cs.gnu.ac.kr/sub02/06.php?id=' + str(self.id) + '&mode=read'
        url = 'http://cs.gnu.ac.kr/csadmin/sub.do?mode=view&idx=' + str(self.id) + '&mCode=MN0038'
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')
            #title_list = soup.select_one('.board-view-title') # selector option (testing)
            title_list = soup.find_all('h4')
        except urllib.error.HTTPError:
            title_list = None # Cause Error in parse_title. (network is fine. Just No Notification)
        except:
            print('CS_NOTI: ERROR OCCURED during scraping', datetime.now())
            return

        noti_title = self.parse_title(title_list, findAllIndex=0)  # at CS, Index is 0.

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
