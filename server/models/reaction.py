from config import db
from sqlalchemy_serializer import SerializerMixin

class Reaction(db.Model, SerializerMixin):
    __tablename__ = 'reactions'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    reaction_type = db.Column(db.String, nullable=False)

    #Relationships
    postreactions = db.relationship('PostReaction', back_populates='reaction', cascade='all, delete-orphan')