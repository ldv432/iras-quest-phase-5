from flask_restful import Resource, request
from config import db
from flask import session, make_response
from models.postreaction import PostReaction

class DeleteReaction(Resource):
    def delete(self, id):
        try:
            if "user_id" not in session:
                return {"error": "You must be logged in to remove a reaction"}, 401
            if post_reaction := PostReaction.query.get(id):
                if post_reaction.user_id == session["user_id"]:
                    response = make_response({}, 204)
                else:
                    response = make_response({"error": "Unauthorized user."}, 403)
                return response
            else:
                return {"error": "Post reaction with this ID not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500