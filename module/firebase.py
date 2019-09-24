# ref. https://firebase.google.com/docs/firestore/quickstart?hl=ko

import firebase_admin
from firebase_admin import credentials, messaging
from firebase_admin import firestore
import os

# cred = credentials.Certificate(os.environ['GOOGLE_SERVICE_ACCOUNT'])
cred = credentials.Certificate('c:/gnu-noti-firebase-adminsdk.json')
try:
    firebase_admin.initialize_app(cred)
except ValueError:
    print("The default Firebase app already exists")
db = firestore.client()


def register_new_noti(category, title, url):
    try:
        _ = os.environ['DEBUG']
        id_docu = db.collection('environ').document('dev_id')
        id = id_docu.get().to_dict()['id']

        new_docu = db.collection('dev').document(str(id))
        id_docu.update({
            'id': id + 1
        })
    except KeyError:
        id_docu = db.collection('environ').document('mix_id')
        id = id_docu.get().to_dict()['id']

        new_docu = db.collection('mix').document(str(id))
        id_docu.update({
            'id': id + 1
        })

    new_docu.set({
        'id': id,
        'category': category,
        'title': title,
        'url': url
    })


def send_notification(title, body, topic=''):
    if topic == '':
        try:
            _ = os.environ['DEBUG']
            topic = 'dev'
        except KeyError:
            topic = 'mix'

    noti = messaging.Notification(title='GNU-NOTI ({})'.format(title), body=body)
    message = messaging.Message(notification=noti, topic=topic)
    response = messaging.send(message)
    print("Send Notification Successfully")
