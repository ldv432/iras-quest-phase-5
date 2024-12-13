from flask_restful import Resource, request
from models.player import Player
from config import db

class PlayerResource(Resource):

    def get(self):
        try:
            player = Player.query.first()
            if not player:
                return {"error": "Player not found."}, 404
            return player.to_dict(), 200
        except Exception as e:
            return {"error": str(e)}, 500
        
    def patch(self):
        try:
            player = Player.query.first()
            if not player:
                return {"error": "Player not found."}, 40
            data = request.json
            if 'health' in data:
                player.health = data['health']
            if 'score' in data:
                player.score = data['score']
            if 'time' in data:
                player.time = data['time']
            db.session.commit()
            return player.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
    
