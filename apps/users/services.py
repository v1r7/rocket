from django.contrib.auth import get_user_model

import re


User = get_user_model()


def authenticate(phone_number, password):
    try:
        user = User.objects.get(phone_number=phone_number)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None


def create_user(data: dict):
    user = User(phone_number=data.get('phone_number'))

    user.set_password(data.get('pass1'))
    user.first_name = data.get('first_name')
    user.email = data.get('email')
    user.phone_number = data.get('phone_number')

    user.save()

    return user


phone_number_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check_email(email):
    if re.search(phone_number_regex, email):
        return True
    return False