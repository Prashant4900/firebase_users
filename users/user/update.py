from firebase_admin import auth
from users.models import FirebaseUsers
from .create_user import create_user
from datetime import datetime


def update_user_info(obj):
    email = "" if not obj.email else obj.email
    username = "" if not obj.name else obj.name
    user_image = "" if not obj.user_image else obj.user_image
    print("email: ", email, " username: ", username, " user_image: ", user_image)

    if FirebaseUsers.objects.filter(id=obj.id).exists():

        if user_image:
            user = auth.update_user(
                uid=obj.uid, email=email, display_name=username,
                email_verified=obj.verified, photo_url=user_image, disabled=obj.disabled
            )
            last_sign_in = user.user_metadata.last_sign_in_timestamp

            FirebaseUsers.objects.filter(uid=obj.uid).update(
                name=username, email=email, verified=obj.verified,
                user_image=user_image, disabled=obj.disabled,
                last_sign_in=datetime.min if not last_sign_in else datetime.utcfromtimestamp(last_sign_in / 1000),
                create_at=datetime.utcfromtimestamp(user.user_metadata.creation_timestamp / 1000),
            )

        user = auth.update_user(
            uid=obj.uid, email=email, display_name=username,
            email_verified=obj.verified, disabled=obj.disabled,
        )

        last_sign_in = user.user_metadata.last_sign_in_timestamp

        FirebaseUsers.objects.filter(uid=obj.uid).update(
            name=username, email=email, verified=obj.verified, disabled=obj.disabled,
            last_sign_in=datetime.min if not last_sign_in else datetime.utcfromtimestamp(last_sign_in / 1000),
            create_at=datetime.utcfromtimestamp(user.user_metadata.creation_timestamp / 1000),
        )

    else:
        create_user(obj)
