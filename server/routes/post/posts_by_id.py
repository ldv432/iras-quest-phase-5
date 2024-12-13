from models.post import Post
from flask_restful import Resource, request
from config import db
from flask import session

class EditForumPost(Resource):
    def patch(self, id):
        post = Post.query.get(id)
        if not post:
            return {"error": "Post not found."}, 404

        user_id = session.get('user_id')
        if post.user_id != user_id:
            return {"error": "You are not authorized to edit this post."}, 403

        data = request.json
        content = data.get('content')
        if not content:
            return {"error": "Content is required."}, 400

        post.content = content
        db.session.commit()
        return post.to_dict(), 200
    
class DeleteForumPost(Resource):
    def delete(self, id):
        post = Post.query.get(id)
        if not post:
            return {"error": "Post not found."}, 404

        user_id = session.get('user_id')
        is_admin = session.get('is_admin', False)
        if post.user_id != user_id and not is_admin:
            return {"error": "You are not authorized to delete this post."}, 403

        db.session.delete(post)
        db.session.commit()
        return {"message": "Post deleted successfully."}, 200

