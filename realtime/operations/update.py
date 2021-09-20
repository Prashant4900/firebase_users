from firebase_admin import db
from .json import to_json
from realtime.views import *

ref = db.reference()
user_ref = ref.child("dummy")


def update(obj):
    # ---------------------- Firebase -----------------------------------#
    print("not obj.uid: ", not obj.uuid)
    if not obj.uuid:
        data = user_ref.push()
        json1 = to_json(data.key, obj)
        data.update(json1)
    else:
        data = user_ref.child(obj.uuid)
        json1 = to_json(data.key, obj)
        data.update(json1)
    # ---------------------- Local -----------------------------------#
    print(not DummyModel.objects.filter(uuid=data.key).exists())
    if not DummyModel.objects.filter(uuid=data.key).exists():
        instance = DummyModel(uuid=data.key, name=obj.name, user=obj.user)
        instance.save()
    else:
        DummyModel.objects.filter(uuid=data.key).update(name=obj.name, user=obj.user)
