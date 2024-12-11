from config import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)

    #Serialization

    #Relationships
    postreactions = db.relationship('PosttReaction', back_populates='user', cascade='all, delete-orphan')