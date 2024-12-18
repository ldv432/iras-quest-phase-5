from models.post import Post
from flask_restful import Resource, request
from config import db
from flask import session


class EditForumPost(Resource):
    def patch(self, id):
        try:
            if "user_id" not in session:
                return {"error": "You must be logged in to edit a post."}, 401

            post = Post.query.get(id)
            if not post:
                return {"error": "Post not found."}, 404

            if post.user_id != session["user_id"]:
                return {"error": "You are not authorized to edit this post."}, 403

            data = request.json
            content = data.get("content")
            if not content:
                return {"error": "Content is required."}, 400

            post.content = content
            db.session.commit()
            return post.to_dict(), 200

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500


class DeleteForumPost(Resource):
    def delete(self, id):
        try:
            post = Post.query.get(id)
            if not post:
                return {"error": "Post not found."}, 404

            if post.user_id != session["user_id"]:
                return {"error": "You are not authorized to delete this post."}, 403

            db.session.delete(post)
            db.session.commit()
            return {"message": "Post deleted successfully."}, 200

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
