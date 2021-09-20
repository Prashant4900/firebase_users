from django.forms.models import model_to_dict
import json


def to_json(uuid, obj):
    data = {
        u'uid': uuid,
        u'name': obj.name,
        "user": model_to_dict(obj.user1),
        # u'updateAt': firestore.firestore.SERVER_TIMESTAMP,
    }

    instance = json.dumps(data, default=str)
    return json.loads(instance)

