import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from firebase_conn import database


doc_ref = database.collection(u'user_wallet').document(u'wallet_desc')
doc_ref.set({
    u'userId': {'id': '123','amount': '1220', 'transact_time': datetime.now().today(), 'transaction': 'credit'}
})


users_ref = database.collection(u'user_wallet').document(u'wallet_desc')
# docs = users_ref.stream()

users_ref.update({
    u'userId': {'id': '125', 'amount': '1220', 'transact_time': datetime.now().today(), 'transaction': 'credit'}
})

users_ref = database.collection(u'user_wallet')
docs = users_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

# doc_ref = db.collection(u'user_wallet').document(u'wallet_desc')
# doc_ref.add({
#     u'amount': u'80',
#     u'transact_time': u'Lovelace',
#     u'transaction': u'credit',
#     u'userId': u'125'
# })