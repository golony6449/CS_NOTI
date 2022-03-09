import requests
from os.path import dirname
import os


def load():
    path = dirname(dirname(os.path.abspath(__file__)))
    try:
        file = open(path + '/source/naver', 'r')
        loaded_value = file.readlines()
        ID = loaded_value[0].strip()
        SECRET = loaded_value[1].strip()
        file.close()

    except FileNotFoundError:
        ID = os.environ["NAVER_ID"]
        SECRET = os.environ["NAVER_SECRET"]

    return ID, SECRET


def make_short(target):
    ID, SECRET = load()
    header = {'X-Naver-Client-Id': ID, 'X-Naver-Client-Secret': SECRET}
    naver = 'https://openapi.naver.com/v1/util/shorturl'
    data = {'url': target}

    maker = requests.post(url=naver, data=data, headers=header)
    maker.close()
    output = maker.json()['result']['url']
    return output
