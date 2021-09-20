from firebase_admin import firestore
from firestore.models import DummyModel
from .json import to_json

firestoreDB = firestore.client()


def update_data(obj):
    if not obj.uid:
        users_ref = firestoreDB.collection(u'dummy').document()
        data = to_json(users_ref.id, obj)
        users_ref.set(data)
    else:
        users_ref = firestoreDB.collection(u'dummy').document(u""f'{obj.uid}'"")
        data = to_json(users_ref.id, obj)
        users_ref.update(data)

    if not DummyModel.objects.filter(uid=users_ref.id).exists():
        instance = DummyModel(uid=users_ref.id, name=obj.name, user1=obj.user1
                              # update_at=str(firestore.firestore.SERVER_TIMESTAMP)
                              )
        instance.save()

    DummyModel.objects.filter(uid=users_ref.id).update(name=obj.name, user1=obj.user1
                                                       # update_at=str(firestore.firestore.SERVER_TIMESTAMP)
                                                       )
