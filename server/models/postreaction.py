from config import db
from sqlalchemy_serializer import SerializerMixin

class PostReaction(db.Model, SerializerMixin):
    __tablename__ = 'postreactions'

    __table_args__ = (db.UniqueConstraint("user_id", "post_id"),)

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, index=True)
    reaction_id = db.Column(db.Integer, db.ForeignKey('reactions.id'), nullable=False, index=True)

    #Relationships
    user = db.relationship('User', back_populates='postreactions')
    post = db.relationship('Post', back_populates='postreactions')
    reaction = db.relationship('Reaction', back_populates='postreactions')

    #Serialization
    serialize_rules = ('-user', '-post', '-reaction')