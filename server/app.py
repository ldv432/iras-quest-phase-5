#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from better_profanity import profanity

from models import monster, npc, player, post, postreaction, reaction, user

# Import Route Classes
from routes.monster.monsters import Monster
from routes.npc.npcs import Npc
from routes.player.players import Player
from routes.post.posts import ForumPosts 
from routes.post.posts_by_id import EditForumPost, DeleteForumPost
from routes.reaction.reactions import AddReaction
from routes.reaction.reactions_by_id import DeleteReaction
from routes.user.users import CreateUser
from routes.user.users_by_id import DeleteUser
from routes.reaction.reactions import GetReactions

from routes.auth.signup import Signup
from routes.auth.login import Login
from routes.auth.current_user import CurrentUser
from routes.auth.logout import Logout



# Route Registration
api.add_resource(Signup, '/signup')  # POST: User Signup
api.add_resource(Login, '/login')  # POST: User Login
api.add_resource(Logout, '/logout')  # POST: User Logout
api.add_resource(CurrentUser, '/current-user')  # GET: Fetch Logged-in User

# Forum Routes
api.add_resource(ForumPosts, '/forum/posts')  # GET: List Posts | POST: Add Post
api.add_resource(EditForumPost, '/forum/posts/<int:id>')  # PATCH: Edit Post
api.add_resource(DeleteForumPost, '/forum/posts/<int:id>')  # DELETE: Delete Post

# Reaction Routes
api.add_resource(AddReaction, '/post-reactions')  # POST: Add/Toggle Reaction
api.add_resource(DeleteReaction, '/post-reactions/<int:id>')  # DELETE: Remove Reaction
api.add_resource(GetReactions, "/forum/reactions")

# User Routes
api.add_resource(CreateUser, '/user')  # POST: Create User
api.add_resource(DeleteUser, '/user/<int:id>')  # DELETE: Delete User

# Index Route
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# Server Start
if __name__ == '__main__':
    app.run(port=5555, debug=True)
