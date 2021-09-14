from firebase_admin import auth
from users.models import FirebaseUsers


def delete_user(obj):
    auth.delete_user(obj.uid)
    instance = FirebaseUsers.objects.get(id=obj.id)
    instance.delete()
