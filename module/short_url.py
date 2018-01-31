import requests
from os.path import dirname
import os

def load():
    path=dirname(dirname(os.path.abspath( __file__ )))
    try:
        file = open(path + '/source/naver', 'r')
    except:
        print('ERROR: No Naver API_key. Please Check Again')

    loaded_value=file.readlines()
    ID=loaded_value[0].strip()
    SECRET=loaded_value[1].strip()
    return ID,SECRET

def makeShort(target):
    ID, SECRET = load()
    header = {'X-Naver-Client-Id': ID, 'X-Naver-Client-Secret': SECRET}
    naver = 'https://openapi.naver.com/v1/util/shorturl'
    data = {'url': target}

    maker=requests.post(url=naver,data=data,headers=header)
    maker.close()
    output=maker.json()['result']['url']
    return output
