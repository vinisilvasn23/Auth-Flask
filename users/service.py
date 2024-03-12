from .models import User
from .database import get_session


def find_by_id(id, session):
    user = session.query(User).get(id)
    if user is None:
        return {"error": "User not found"}, 404
    return user


def find_by_email(email, session):
    user = session.query(User).filter_by(email=email).first()
    if user:
        return None


def create_user(name, email, password):
    with get_session() as session:
        find_by_email(email, session)
        user = User(name=name, email=email)
        user.set_password(password)
        session.add(user)
        session.commit()
        return user


def update(user_id, data):
    session = get_session()
    user = find_by_id(user_id, session)

    for field, value in data.items():
        if hasattr(user, field):
            if value is not None:
                setattr(user, field, value)

    session.commit()
    return user.to_dict()


def desactive(user_id, active):
    session = get_session()
    user = find_by_id(user_id, session)

    user.active = active
    session.commit()

    return user.to_dict()
