from routes.__init__ import Resource, request, make_response, session
from models.user import User

class Login(Resource):
    def post(self):
        try:
            data = request.json
            user = User.query.filter_by(email=data.get("email", "")).first()
            if user and user.authenticate(data.get("password", "")):
                session["user_id"] = user.id
                return make_response(user.to_dict(), 200)
            else:
                return make_response("Login information incorrect.", 401)
        except Exception as e:
            return {"error": str(e)}, 400