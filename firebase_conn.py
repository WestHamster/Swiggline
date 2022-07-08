import firebase_admin
from firebase_admin import credentials, firestore
# Product account
# cred = credentials.Certificate('swiggline-5f03319dddcf.json')

databaseURL = {'databaseURL': "https://swiggline.firebaseio.com"}

# Service account
cred = credentials.Certificate('swiggline-eaef7a3e0243.json')
firebase_admin.initialize_app(cred)
database = firestore.client()
