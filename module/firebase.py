# ref. https://firebase.google.com/docs/firestore/quickstart?hl=ko

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

cred = credentials.Certificate(os.environ['GOOGLE_SERVICE_ACCOUNT'])
firebase_admin.initialize_app(cred)
db = firestore.client()


def register_new_noti(category, title, url):
  new_docu = db.collection('dev').document()
  new_docu.set({
    'category': category,
    'title': title,
    'url': url
  })
