import urllib
import BeautifulSoup
import datetime
import sys
import os


class baseNotifier:
    def __init__(self):
        self.url=''
        self.mode=None
        self.root=path = os.path.dirname(os.path.abspath(__file__))

    def parse_title(self,target):
        target_num = 0
        if mode == :
            target_num = 3
        source = str(target[target_num]).decode('utf-8')
        ouput = ''
        start = 0
        end = 0

        for pointer in range(len(source) - 1):
            if source[pointer] == '>':
                start = pointer + 1
        for pointer in range(start, len(source) - 1):
            if source[pointer] == '<':
                end = pointer
                break

    def save(self,saveData,path):
        file = open(path, 'w')
        file.write(str(saveData))

    def load(self,path):
        file = open(path, 'r')
        loaded_value = file.readline()
        return int(loaded_value)
