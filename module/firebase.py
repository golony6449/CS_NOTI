# ref. https://firebase.google.com/docs/firestore/quickstart?hl=ko

import firebase_admin
from firebase_admin import credentials, messaging
from firebase_admin import firestore
import os

cred = credentials.Certificate(os.environ['GOOGLE_SERVICE_ACCOUNT'])

try:
    firebase_admin.initialize_app(cred)
except ValueError:
    print("The default Firebase app already exists")
db = firestore.client()


def register_new_noti(category: str, title: str, url: str):
    try:
        _ = os.environ['DEBUG']
        id_docu = db.collection('environ').document('dev_id')
        id = id_docu.get().to_dict()['id']

        new_docu = db.collection('dev').document(str(id))
        id_docu.update({
            'id': id + 1
        })
    except KeyError:
        # 혼합 리스트
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

    # 채널에 따른 추가
    target_ch_id = get_last_noti_id(category)
    new_target_ch_docu = db.collection(category).document(str(target_ch_id))

    db.collection('environ').document(category).update({
        'id': target_ch_id + 1
    })

    new_target_ch_docu.set({
        'id': target_ch_id,
        'category': category,
        'title': title,
        'url': url
    })


def send_notification(title, body):
    topics = []

    try:
        _ = os.environ['DEBUG']
        topics.append('dev')
    except KeyError:
        # 더 이상 mix 채널 사용 안함
        # topics.append('mix')

        if title == 'HOT NEWS':
            topics.append('gnu')

        if title == '기관공지':
            topics.append('agency')

    noti = messaging.Notification(title='GNU-NOTI ({})'.format(title), body=body)

    for t in topics:
        message = messaging.Message(notification=noti, topic=t)
        response = messaging.send(message)
        print("{}: Send Notification Successfully".format(t))


def migration():
    mix_collection = db.collection("mix")
    docs = mix_collection.stream()

    for d in docs:
        dict_data = d.to_dict()
        print(u'{} => {} 처리중'.format(d.id, dict_data))

        register_new_noti(dict_data['category'], dict_data['title'], dict_data['url'])


def get_last_noti_id(category: str):
    id_target_ch_docu = db.collection('environ').document(category)
    target_ch_id = id_target_ch_docu.get().to_dict()['id']

    return target_ch_id


def get_last_remote_id(category: str):
    doc_last_remote_id = db.collection('environ').document('last_remote_id')
    last_remote_id = doc_last_remote_id.get().to_dict()[category]
    return last_remote_id


def update_last_remote_id(category: str, id: int):
    id_docu = db.collection('environ').document('last_remote_id')

    doc = id_docu.get().to_dict()
    doc[category] = id

    id_docu.update(doc)
