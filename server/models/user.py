from config import db, flask_bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
import re

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128), nullable=False)

    #Relationships
    players = db.relationship('Player', back_populates='user', cascade='all, delete-orphan')
    posts = db.relationship('Post', back_populates='user', cascade='all, delete-orphan')
    postreactions = db.relationship('PostReaction', back_populates='user', cascade='all, delete-orphan')

    #Serialization
    serialize_rules = ('-_password_hash', '-players', '-posts', '-postreactions')

    #Representation
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

    #Validations
    @validates('username')
    def validate_username(self, _, value):
        if len(value) < 2:
            raise ValueError("Username must be at least 2 characters long.")
        if not value.isalnum():
            raise ValueError("Username must only contain letters and numbers.")
        return value

    @validates('email')
    def validate_email(self, _, value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format.")
        return value
    
    @hybrid_property
    def password(self):
        raise AttributeError("passwords can only be set, not read.")

    @password.setter
    def password(self, password_to_validate):
        if not isinstance(password_to_validate, str):
            raise TypeError("password must be a string")
        if not 8 <= len(password_to_validate) <= 25:
            raise ValueError("password must be a string between 8 and 25 characters long")
        hashed_password = flask_bcrypt.generate_password_hash(password_to_validate).decode("utf-8")
        self._password_hash = hashed_password

    def authenticate(self, password_to_check):
        return flask_bcrypt.check_password_hash(self._password_hash, password_to_check)
    