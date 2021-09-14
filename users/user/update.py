from firebase_admin import auth
from users.models import FirebaseUsers
from .create_user import create_user


def update_user_info(obj):
    email = "" if not obj.email else obj.email
    username = "" if not obj.name else obj.name
    user_image = "" if not obj.user_image else obj.user_image
    print("email: ", email, " username: ", username, " user_image: ", user_image)

    if FirebaseUsers.objects.filter(id=obj.id).exists():

        if user_image:
            auth.update_user(
                uid=obj.uid, email=email, display_name=username,
                email_verified=obj.verified, photo_url=user_image, disabled=obj.disabled
            )
            FirebaseUsers.objects.filter(uid=obj.uid).update(
                name=username, email=email, verified=obj.verified,
                user_image=user_image, disabled=obj.disabled,
            )

        auth.update_user(
            uid=obj.uid, email=email, display_name=username,
            email_verified=obj.verified, disabled=obj.disabled
        )
        FirebaseUsers.objects.filter(uid=obj.uid).update(
            name=username, email=email, verified=obj.verified, disabled=obj.disabled,
        )

    else:
        create_user(obj)
