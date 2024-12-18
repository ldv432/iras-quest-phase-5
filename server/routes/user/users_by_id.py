from flask_restful import Resource
from flask import session, make_response
from models.user import User
from config import db  

class DeleteUser(Resource):
    def delete(self, id):
        try:
            
            if "user_id" not in session:
                return {"error": "You must be logged in to delete a user."}, 401
            
            user = User.query.get(id)
            if not user:
                return {"error": "User with this ID not found."}, 404
           
            if user.id != session["user_id"]:
                return {"error": "Unauthorized user."}, 403
            
            db.session.delete(user)
            db.session.commit()
            
            return make_response({}, 204)
        
        except Exception as e:
            # Handle unexpected errors
            return {"error": str(e)}, 500