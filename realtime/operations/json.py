from django.forms.models import model_to_dict
import json


def to_json(uuid, obj):

    data = {
        "id": obj.id,
        "uuid": uuid,
        "name": obj.name,
        "user": model_to_dict(obj.user),
    }

    instance = json.dumps(data, default=str)
    return json.loads(instance)
