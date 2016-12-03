import urllib2
import requests
import os

url='https://api.telegram.org/bot'

try:
    path=os.path.dirname( os.path.abspath( __file__ ) )
    api_key = open(path+'/source/api_key', 'r').read()

except:
    print 'ERROR: No API_key. Please Check Again'
    exit()

class Telegram():
    def __init__(self,to_which):
        self.ch_id = to_which

    def send(self,text=''):
        data={'chat_id':self.ch_id,'text':text}
        socket=requests.post(url=url+api_key+'/sendMessage',data=data)

    def notification(self,text='',path=''):
        #self.send(text)
        #self.send(path)
        self.send(text+'\n'+path)

    def test(self):
        req=urllib2.Request(url+api_key+'/sendMessage')
        req.add_data(self.ch_id+'&text=''test''')
        socket=urllib2.urlopen(req)
        print socket.read(300)