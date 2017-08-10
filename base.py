import os


class baseNotifier:
    def __init__(self):
        self.url=''
        self.mode=None
        self.root=path = os.path.dirname(os.path.abspath(__file__))

    def parse_title(self,target,findAllIndex):
        source = target[findAllIndex]
        ouput = ''
        start = 0
        end = 0
        print(source.contents[1])
        return source.contents[1]
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

    def save(self,saveData,path):
        file = open(path, 'w')
        file.write(str(saveData))

    def load(self,path):
        file = open(path, 'r')
        loaded_value = file.readline()
        return int(loaded_value)
