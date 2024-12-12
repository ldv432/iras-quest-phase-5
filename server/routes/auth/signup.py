from routes.__init__ import Resource, request, db, make_response, session
from models.user import User
from sqlalchemy.exc import IntegrityError

class Signup(Resource):
    def post(self):
        try:
            data = request.json
            user = User(email=data.get("email"), username=data.get("username"))
            user.password = data.get("password")
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id
            return make_response(user.to_dict(), 201)
        except IntegrityError as e:
            return {"error": str(e.orig)}, 422
        except Exception as e:
            return {"error": str(e)}, 422
        