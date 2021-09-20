from firebase_admin import firestore
from firestore.models import DummyModel


firestoreDB = firestore.client()


def delete_data(obj):
    firestoreDB.collection(u'dummy').document(u""f'{obj.uid}'"").delete()
    instance = DummyModel.objects.get(id=obj.id)
    instance.delete()
