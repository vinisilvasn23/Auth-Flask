from sqlalchemy import Column, Integer, String, Boolean
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session

Base = declarative_base()

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)

    def to_dict(self):
        session = object_session(self)
        if session is None:
            session = db.session
            session.add(self)
            session.commit()
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'active': self.active
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        db.session.commit()


User.query = db.session.query_property()
