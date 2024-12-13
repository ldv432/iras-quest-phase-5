from models.post import Post
from flask_restful import Resource, request
from config import db

class ForumPosts(Resource):
    def get(self):
        posts = Post.query
        return [post.to_dict() for post in posts], 200

    
class AddForumPost(Resource):
    def post(self):
        data = request.json
        user_id = data.get('user_id')
        content = data.get('content')
        created_at = data.get('created_at')

        if not user_id or not content:
            return {"error": "User ID and content are required."}, 400

        new_post = Post(user_id=user_id, content=content, created_at=created_at)
        db.session.add(new_post)
        db.session.commit()

        return new_post.to_dict(), 201



