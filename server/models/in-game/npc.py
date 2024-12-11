from config import db
from sqlalchemy_serializer import SerializerMixin

class Npc(db.Model, SerializerMixin):
    __tablename__ = 'npcs'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    dialogue = db.Column(db.String)

    #Serialization

    #Relationships
    