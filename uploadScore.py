import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('secret.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aihackaton-253aa-default-rtdb.firebaseio.com/'
})

ref = db.reference('score')
print(ref.get())
ref.set({'sum': sum})