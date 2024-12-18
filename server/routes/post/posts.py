from flask_restful import Resource, request
from config import db
from models.post import Post
from flask import session

class ForumPosts(Resource):
    def get(self):
        # Existing logic for GET requests
        try:
            posts = Post.query.all()
            return [post.to_dict() for post in posts], 200
        except Exception as e:
            return {"error": str(e)}, 500

    def post(self):
        # New logic to handle POST requests
        try:
            if "user_id" not in session:
                return {"error": "You must be logged in to create a post"}, 401

            data = request.get_json()
            content = data.get("content")

            if not content:
                return {"error": "Content cannot be empty"}, 400

            # Create a new post
            new_post = Post(user_id=session["user_id"], content=content)
            db.session.add(new_post)
            db.session.commit()

            return new_post.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 500
