import urllib2

url='https://api.telegram.org/bot'
api_key='257446028:AAGgXliWqKyOXoGQ8oFm6rmyiB4YVdZ-ovA'
ch_id='chat_id=@CS_NOTI'

class Telegram():

    def __init__(self):
        pass

    def send(self,text=''):
        req = urllib2.Request(url + api_key + '/sendMessage')
        req.add_data(ch_id+'&text='+text.encode('utf-8'))
        socket=urllib2.urlopen(req)

    def notification(self,text='',path=''):
        self.send(text)
        self.send(path)

    def test(self):
        req=urllib2.Request(url+api_key+'/sendMessage')
        req.add_data(ch_id+'&text=''test''')
        socket=urllib2.urlopen(req)
        print socket.read(300)