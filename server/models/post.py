from config import db
from sqlalchemy_serializer import SerializerMixin

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    content = db.Column(db.String(300), nullable=False)
    
    #Serialization
    serialize_rules = ('-user.posts', '-postreactions.post')

    #Relationships
    user = db.relationship('User', back_populates='posts')
    postreactions = db.relationship('PostReaction', back_populates='post', cascade='all, delete-orphan')