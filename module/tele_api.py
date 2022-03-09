# import urllib2
import requests
import os


class Telegram:
    def __init__(self, to_which):
        self.ch_id = to_which

        try:
            path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file = open(path + "/source/api_key", "r")
            self.api_key = file.read().strip()
            file.close()
        except FileNotFoundError:
            self.api_key = os.environ["TELEGRAM_API"]

    def send(self, text=''):
        url = 'https://api.telegram.org/bot'
        data = {
            'chat_id': self.ch_id,
            'text': text
        }

        socket = requests.post(url=url + self.api_key + '/sendMessage', data=data)
        if socket.status_code != 200:
            print("error occurred (Telegram): " + str(socket.status_code) + socket.text)
        socket.close()

    def notification(self, text='', path=''):
        self.send(text + '\n' + path)

    # def test(self):
    #     req=urllib2.Request(url+api_key+'/sendMessage')
    #     req.add_data(self.ch_id+'&text=''test''')
    #     socket=urllib2.urlopen(req)
    #     print (socket.read(300))
