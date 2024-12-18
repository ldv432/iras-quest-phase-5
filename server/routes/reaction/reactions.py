from flask_restful import Resource, request
from config import db
from flask import session
from models.postreaction import PostReaction
from sqlalchemy import func

from flask_restful import Resource
from flask import session
from config import db
from models.postreaction import PostReaction
from sqlalchemy import func

class GetReactions(Resource):
    def get(self):
        try:
            if "user_id" not in session:
                return {"error": "User must be logged in"}, 401

            user_id = session["user_id"]

            # Query for total reaction counts grouped by post and reaction type
            total_reactions = (
                db.session.query(
                    PostReaction.post_id,
                    PostReaction.reaction_id,
                    func.count(PostReaction.id).label("count")
                )
                .group_by(PostReaction.post_id, PostReaction.reaction_id)
                .all()
            )

            # Query for the user's specific reactions
            user_reactions = (
                db.session.query(
                    PostReaction.post_id,
                    PostReaction.reaction_id
                )
                .filter_by(user_id=user_id)
                .all()
            )

            # Build the response
            response = {}
            for post_id, reaction_id, count in total_reactions:
                if post_id not in response:
                    response[post_id] = {"counts": {}, "user": {}}
                response[post_id]["counts"][reaction_id] = count

            for post_id, reaction_id in user_reactions:
                response[post_id]["user"][reaction_id] = True

            return response, 200

        except Exception as e:
            return {"error": str(e)}, 500


class AddReaction(Resource):
    def post(self):
        try:
            if "user_id" not in session:
                return {'error': "You must login to react to this post"}, 400

            data = request.json
            user_id = session['user_id']
            post_id = data.get('post_id')
            reaction_id = data.get('reaction_id')

            # Check for existing reaction
            existing_reaction = PostReaction.query.filter_by(
                user_id=user_id, post_id=post_id, reaction_id=reaction_id
            ).first()

            if existing_reaction:
                # Remove reaction (toggle off)
                db.session.delete(existing_reaction)
                db.session.commit()
                # Fetch updated count for this reaction type
                updated_count = db.session.query(func.count(PostReaction.id)).filter_by(
                    post_id=post_id, reaction_id=reaction_id
                ).scalar()
                return {
                    "message": "Reaction removed",
                    "reaction_id": reaction_id,
                    "count": updated_count,
                    "status": "removed",
                }, 200
            else:
                # Add new reaction
                new_reaction = PostReaction(user_id=user_id, post_id=post_id, reaction_id=reaction_id)
                db.session.add(new_reaction)
                db.session.commit()
                # Fetch updated count for this reaction type
                updated_count = db.session.query(func.count(PostReaction.id)).filter_by(
                    post_id=post_id, reaction_id=reaction_id
                ).scalar()
                return {
                    "message": "Reaction added",
                    "reaction_id": reaction_id,
                    "count": updated_count,
                    "status": "added",
                }, 201

        except Exception as e:
            return {'error': str(e)}, 500
