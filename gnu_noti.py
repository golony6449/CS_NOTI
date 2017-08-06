import base

class gnuNotification(base.baseNotifier):
    def __init__(self):
        super(self).__init__()

        self.soupIndex=0

        self.load()

    def run(self):
        self.url = 'http://www.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=10026&boardNo=' + str(id)
        try:
            html = urllib.urlopen(url)
            soup = BeautifulSoup(html, 'html5lib')
            title_list = soup.find_all('h3')
            noti_title = parse_title(title_list, is_gnu=True)
        except:
            print 'GNU_NOTI: ERROR OCCURED during scraping', datetime.now()
            time.sleep(10)
            return
            gnu_noti(id)
            noti_title = False

        if noti_title == False:
            # test
            print 'GNU_NOTI: There is no notification. ID:', id, datetime.now()
            if redirect == False:
                print 'Checking another ID'
                id = (gnu_noti(id + 1, redirect=True)) - 1
        else:
            noti_title = '[HOT NEWS]\n' + noti_title
            short = short_url.makeShort(url)
            tele = tele_api.Telegram('@Testing77')
            tele.notification(noti_title, short)
            print 'GNU_NOTI: NEW NOTIFICATION. ID:', id
            id += 1
            save_load(id, 'w', 'gnu')
        return id

    def save(self,saveData):
        path=self.root+'\source\last_gnu'
        super(self).save(saveData,path)

    def load(self):
        path=self.root+'\source\last_gnu'
        self.id=super(self).load(path)