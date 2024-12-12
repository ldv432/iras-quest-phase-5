from routes.__init__ import Resource, db, make_response, session
from models.user import User


class CurrentUser(Resource):
    def get(self):
        try:
            if "user_id" in session:
                if user := db.session.get(User, session["user_id"]):
                    return make_response(user.to_dict(), 200)
                del session["user_id"]
                return make_response({"error": "Unauthorized user."}, 401)
            return make_response({"error": "Unauthorized user. Please login again"}, 401)
        except Exception as e:
            return {"error": str(e)}, 500