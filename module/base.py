from os import path
from time import sleep

import requests
import bs4
from bs4 import BeautifulSoup

from module import firebase


class NotifierInterface:
    def run(self):
        pass


class BaseNotifier(NotifierInterface):
    def __init__(self):
        self.url = ''
        self.mode = None
        self.root = \
            path.dirname(path.dirname(path.abspath(__file__)))
        self.checkOneMore = False

    def parse_title(self, target, findAllIndex):
        if self.mode == 'CS':
            para = 0
        else:
            para = 1

        try:
            source = target[findAllIndex]
        except:
            return False
        # print(source.contents[1])  #test

        if para == 1:
            try:
                return source.contents[para]   #in agency,gnu_noti, ERROR occur. When There is No new notice.
            except:
                return False

        else:
            try:
                return source.text  # for cs_noti
            except:
                return False

    def run(self):
        pass

    def check(self, bs4_obj):
        sleep(10)
        if self.checkOneMore is True:
            return

        # 글이 삭제된 경우 예외처리
        script_tag_list = bs4_obj.find_all('script')

        for idx, tag in enumerate(script_tag_list):
            # print(idx, '번 확인중', tag.text)
            if "권한" in tag.text:
                print(self.id, '번 글은 삭제되었습니다.')
                self.id += 1
                self.save_id()
                return

        # 글 번호를 1개 건너 뛰는 경우 예외처리
        print('Checking another ID')
        self.checkOneMore = True
        self.id = self.id + 1
        self.run()

    def save(self, saveData, path):
        file = open(path, 'w')
        file.write(str(saveData))

    def load(self, path):
        try:
            file = open(path, 'r')
        except:
            print('ERROR: There is no last noti data in source directory')
            exit()

        loaded_value = file.readline()
        return int(loaded_value)

    def save_id(self):
        pass


class BaseNotifierV2(NotifierInterface):
    url = None
    category = None

    def __init__(self):
        pass

    def is_valid(self):
        if self.url is None or self.category is None:
            return False

        return True

    def run(self):
        if self.is_valid() is False:
            raise RuntimeError('parameter(url, firestore_collection_id) is Empty')

        items = self.parse_data()
        last_remote_id = firebase.get_last_remote_id(self.category)     # 지금까지 처리한 공홈의 게시글 ID
        new_last_remote_id = 0                                          # 현재 처리한 게시글 중 최종 ID (이 값으로 Firestore 값 갱신)

        list_new_noti = []

        for item in items:
            item_id = self.get_noti_id(item)

            if item_id > last_remote_id:
                data = {
                    'title': item.find('title').text,
                    'url': item.find('link').text
                }

                list_new_noti.insert(0, data)
                new_last_remote_id = max(item_id, new_last_remote_id)

        # Firestore 저장
        for noti in list_new_noti:
            firebase.register_new_noti(self.category, noti['title'], noti['url'])

        # TODO Push 발송

        # Firestore > environ > last_remote_id 갱신
        firebase.update_last_remote_id(self.category, new_last_remote_id)

    def parse_data(self):
        raw_xml_data = requests.get(self.url)
        soup = BeautifulSoup(raw_xml_data.text, 'xml')

        return soup.find('channel').find_all('item')

    def get_noti_id(self, bs4_item_tag: bs4.element.Tag):
        noti_url = bs4_item_tag.find('link').get_text()
        url_params = [param for param in noti_url.split('?')[1].split('&')]

        for p in url_params:
            if 'nttSn' in p:
                return int(p.split('=')[1])

        return None
