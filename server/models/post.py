from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())

    #Serialization
    serialize_rules = ('-user.posts', '-postreactions.post')

    #Relationships
    user = db.relationship('User', back_populates='posts')
    postreactions = db.relationship('PostReaction', back_populates='post', cascade='all, delete-orphan')

    #Validations
    #Need to make sure to find user with the user_id given