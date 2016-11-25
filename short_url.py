import requests
import os

def load():
    path=path=os.path.dirname( os.path.abspath( __file__ ) )
    file=open(path+'/source/naver','r')
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
    output=maker.json()['result']['url']
    return output
