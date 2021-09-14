from firebase_admin import auth
from users.models import FirebaseUsers
from datetime import datetime


def create_user(obj):
    email = "" if not obj.email else obj.email
    password = "" if not obj.password else obj.password
    name = "" if not obj.name else obj.name
    phone = "" if not obj.phone else obj.phone
    disabled = "" if not obj.disabled else obj.disabled
    verified = "" if not obj.verified else obj.verified
    print("*********************************************")
    print("email: ", email, "pass: ", password, "name: ", name, "phone: ", phone,
          "disable: ", disabled, "verify: ", verified)

    user = auth.create_user(
        display_name=name,
        email=email,
        password=password,
        email_verified=verified,
        disabled=disabled
    )

    instance = FirebaseUsers(
        uid=user.uid, name=user.display_name, email=user.email,
        verified=user.email_verified, disabled=user.disabled,
        create_at=datetime.now(),
        provider=user.provider_data[0].provider_id
    )

    if phone:
        user = auth.create_user(
            display_name=name,
            email=email,
            password=password,
            email_verified=verified,
            disabled=disabled,
            phone_number=phone,
        )

        instance = FirebaseUsers(
            uid=user.uid, name=user.display_name, email=user.email,
            verified=user.email_verified, disabled=user.disabled,
            create_at=datetime.now(),
            provider=user.provider_data[0].provider_id, phone=user.phone_number
        )

    instance.save()
