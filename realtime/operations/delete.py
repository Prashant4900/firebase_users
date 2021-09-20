from firebase_admin import db
from realtime.models import DummyModel

ref = db.reference()
user_ref = ref.child("dummy")


def delete(obj):
    user_ref.child(obj.uuid).delete()
    instance = DummyModel.objects.get(uuid=obj.uuid)
    instance.delete()
