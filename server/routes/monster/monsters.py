from flask_restful import Resource, request
from models.monster import Monster
from config import db

class MonsterById(Resource):
    def patch(self, monster_id):
        try:
            monster = Monster.query.get(monster_id)
            if not monster:
                return {"error": "Favorite not found."}, 404
            data = request.json
            health = data.get('health')
            if health:
                monster.health = health
            
                db.session.commit()
                return monster.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500