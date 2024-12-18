from models.user import User
from flask_restful import Resource, request
from flask import make_response
from config import db
from better_profanity import profanity

class CreateUser(Resource):
    def post(self):     
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check user entered info
        if not username or not email or not password:
            return {"error": "Username, email and password are required."}, 400
        
        # Validate the validators
        if len(username) < 2:
            return {"error": "Username must be at least two characters long."}
        if not username.isalnum():
            return {"error": "Username can only contain numbers and letters."}
        for key, value in data.items():
            if profanity.contains_profanity(value):
                return {"error": f"Inapproriate content detected in {key}"}

        # Check backend for duplicates
        if User.query.filter_by(username=username).first():
            return {"error": "Username is already taken."}, 400
        if User.query.filter_by(email=email).first():
            return {"error": "Email is already in use."}, 400
        
        # We passed, we send   
        try:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.serialize(), 201)
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
            
         
    