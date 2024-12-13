from flask_restful import Resource, request
from config import db

class AddReaction(Resource):
    def post(self):
        try:
            data = request.json
            user_id = data.get('user_id')
            post_id = data.get('post_id')
            reaction_type = data.get()