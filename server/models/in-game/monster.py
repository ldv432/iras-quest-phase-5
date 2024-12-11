from config import db
from sqlalchemy_serializer import SerializerMixin

class Monster(db.Model, SerializerMixin):
    __tablename__ = 'monsters'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)
   

    #Serialization

    #Relationships