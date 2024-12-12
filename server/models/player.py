from config import db
from sqlalchemy_serializer import SerializerMixin

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    health = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)


    #Relationships
    user = db.relationship('User', back_populates='players')
    
    #Serialization