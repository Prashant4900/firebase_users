from firebase_admin import auth
from .models import FirebaseUsers
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    page = auth.list_users()
    all_users = FirebaseUsers.objects.all()
    while page:
        for user in page.users:

            last_sign_in = user.user_metadata.last_sign_in_timestamp
            phone = "" if not user.phone_number else user.phone_number
            password = "" if not user.password_hash else user.password_hash
            username = "Guest User" if not user.display_name else user.display_name
            user_image = "" if not user.photo_url else user.photo_url

            if not all_users.filter(uid=user.uid).exists():
                firebase_user = FirebaseUsers(
                    uid=user.uid, email=user.email, name=username, verified=user.email_verified, disabled=user.disabled,
                    user_image=user_image,
                    create_at=datetime.fromtimestamp(user.user_metadata.creation_timestamp / 1000),
                    last_sign_in=None if not last_sign_in else datetime.utcfromtimestamp(last_sign_in / 1000),
                    phone=phone, password=password, provider=user.provider_data[0].provider_id
                )
                firebase_user.save()

            else:
                FirebaseUsers.objects.filter(uid=user.uid).update(
                    email=user.email, name=username, verified=user.email_verified, disabled=user.disabled,
                    user_image=user_image,
                    create_at=datetime.fromtimestamp(user.user_metadata.creation_timestamp / 1000),
                    last_sign_in=None if not last_sign_in else datetime.utcfromtimestamp(last_sign_in / 1000),
                    phone=phone, password=password, provider=user.provider_data[0].provider_id
                )
        page = page.get_next_page()

    html = "<h1>List Updated</h1>"
    return HttpResponse(html)
