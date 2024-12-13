#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api

from models import monster, npc, player, post, postreaction, reaction, user

from routes.monster.monsters import Monster
from routes.npc.npcs import Npc
from routes.player.players import Player
from routes.post.posts import ForumPosts, AddForumPost
from routes.post.posts_by_id import EditForumPost, DeleteForumPost
# from routes.post.posts import Post
# from routes.reaction.reactions import Reaction
# from routes.postreaction.postreactions import PostReaction
# from routes.user.users import User

from routes.auth.signup import Signup
from routes.auth.login import Login
from routes.auth.current_user import CurrentUser
from routes.auth.logout import Logout

app.secret_key="JIMMY DEAN SAUSAGES?"

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CurrentUser, '/current-user')
api.add_resource(ForumPosts, '/forum/posts')
api.add_resource(AddForumPost, '/forum/posts')
api.add_resource(EditForumPost, '/forum/posts/<int:id>')
api.add_resource(DeleteForumPost, '/forum/posts/<int:id>')






@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

