# ref. https://firebase.google.com/docs/firestore/quickstart?hl=ko

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

cred = credentials.Certificate(os.environ['GOOGLE_SERVICE_ACCOUNT'])
firebase_admin.initialize_app(cred)
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
        id_docu = db.collection('environ').document('dev_id')
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
