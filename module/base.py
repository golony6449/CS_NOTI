from os import path
from time import sleep


class baseNotifier:
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
