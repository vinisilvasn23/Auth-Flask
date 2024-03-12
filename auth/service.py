from users.models import User


def find_by_email(email):
    return User.query.filter_by(email=email).first()


def auth(email, password):
    user = find_by_email(email)
    if not user or not user.active or not user.check_password(password):
        return None
    return user
