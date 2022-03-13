from module import base


class ScholarshipNotification(base.RssBaseNotifier):
    url = 'http://www.gnu.ac.kr/main/na/ntt/selectRssFeed.do?mi=1376&bbsId=1075'
    category = '장학'
    firebase_ch = 'scholarship'
