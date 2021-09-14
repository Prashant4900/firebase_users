from firebase_admin import auth
from .models import FirebaseUsers
from django.http import HttpResponse


# Create your views here.
def index(request):
    page = auth.list_users()
    all_users = FirebaseUsers.objects.all()
    while page:
        for user in page.users:

            last_sign_in = "" if not user.user_metadata.last_sign_in_timestamp else user.user_metadata.last_sign_in_timestamp
            phone = "" if not user.phone_number else user.phone_number
            password = "" if not user.password_hash else user.password_hash
            username = "Guest User" if not user.display_name else user.display_name
            user_image = "" if not user.photo_url else user.photo_url

            if not all_users.filter(uid=user.uid).exists():
                firebase_user = FirebaseUsers(
                    uid=user.uid, email=user.email, name=username, verified=user.email_verified,
                    disabled=user.disabled, user_image=user_image, create_at=user.user_metadata.creation_timestamp,
                    last_sign_in=last_sign_in, phone=phone,
                    password=password,
                    provider=user.provider_data[0].provider_id
                )
                firebase_user.save()

            if all_users.filter(uid=user.uid).exists():
                FirebaseUsers.objects.filter(uid=user.uid).update(
                    email=user.email, name=username, verified=user.email_verified,
                    disabled=user.disabled, user_image=user_image, create_at=user.user_metadata.creation_timestamp,
                    last_sign_in=last_sign_in, phone=phone,
                    password=password,
                    provider=user.provider_data[0].provider_id
                )
        page = page.get_next_page()

    html = "<h1>Home Page</h1>"
    return HttpResponse(html)
