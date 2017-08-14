from os import path
from time import sleep


class baseNotifier:
    def __init__(self):
        self.url = ''
        self.mode = None
        self.root = \
            path.dirname(path.dirname(path.abspath(__file__)))
        self.checkOnemore = False

    def parse_title(self, target, findAllIndex):
        try:
            source = target[findAllIndex]  #in cs_noti, ERROR occur here. When There is NO new notice.
        except:
            return False
        # print(source.contents[1])  #test

        try:
            return source.contents[1]   #in agency,gnu_noti, ERROR occur. When There is No new notice.
        except:
            return False

        # legacy code
        # ouput = ''
        # start = 0
        # end = 0
        # for pointer in range(len(source) - 1):
        #     if source[pointer] == '>':
        #         start = pointer + 1
        # for pointer in range(start, len(source) - 1):
        #     if source[pointer] == '<':
        #         end = pointer
        #         break
        #
        # # Check NULL contents
        # if start == end or len(source[start:end]) < 8:
        #     return False
        # else:
        #     return source[start:end]

    def check(self):
        if self.checkOnemore == True:
            return

        sleep(10)
        print('Checking another ID')
        self.checkOnemore = True
        self.id = self.id + 1
        self.run()

    def save(self, saveData, path):
        file = open(path, 'w')
        file.write(str(saveData))

    def load(self, path):
        try:
            file = open(path, 'r')
        except:
            print('ERROR: There is no last noti data (\source\last_cs, last_gnu, last_agency)')
            exit()

        loaded_value = file.readline()
        return int(loaded_value)
