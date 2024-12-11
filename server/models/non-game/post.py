from config import db
from sqlalchemy_serializer import SerializerMixin

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    content = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)

    #Serialization

    #Relationships
    postreactions = db.relationship('PostReaction', back_populates='user', cascade='all, delete-orphan')