#!/usr/bin/env python3

from random import randint
from faker import Faker
from app import app
from config import db
from models.monster import Monster
from models.npc import Npc
from models.player import Player
from models.user import User
from models.post import Post
from models.reaction import Reaction
from models.postreaction import PostReaction

def reset_database():
    db.drop_all()
    db.create_all()
    print("Database reset complete.")

def seed_users():
    users = [
        User(email="user1@example.com", username="user1", _password_hash="password123"),
        User(email="user2@example.com", username="user2", _password_hash="password123"),
        User(email="user3@example.com", username="user3", _password_hash="password123"),
    ]
    db.session.add_all(users)
    db.session.commit()

def seed_monsters():
    monsters = [
        Monster(type="Goblin", health=150, power=40),
        Monster(type="Alien", health=100, power=30),
        Monster(type="Archer", health=60, power=20),
    ]
    db.session.add_all(monsters)
    db.session.commit()

def seed_npcs():
    npcs = [
        Npc(dialogue="Hello. We are surprised you made it this far. You must keep going..."),
        Npc(dialogue="This is the first time we've seen someone make it here... impressive."),
        Npc(dialogue="You are nearly there... The King is waiting."),
    ]
    db.session.add_all(npcs)
    db.session.commit()

def seed_player():
    players = [
        Player(health=100, power=20, score=0, time=0, user_id=1),
    ]
    db.session.add_all(players)
    db.session.commit()

def seed_posts():
    posts = [
        Post(user_id=1, content="This is my first post!", created_at=fake.date_time()),
        Post(user_id=2, content="Hello, world!", created_at=fake.date_time()),
        Post(user_id=3, content="Loving this game so far.", created_at=fake.date_time()),
    ]
    db.session.add_all(posts)
    db.session.commit()

def seed_reactions():
    reactions = [
        Reaction(reaction_type="Like"),
        Reaction(reaction_type="Dislike"),
        Reaction(reaction_type="Love"),
    ]
    db.session.add_all(reactions)
    db.session.commit()

def seed_post_reactions():
    post_reactions = [
        PostReaction(post_id=1, user_id=2, reaction_id=1),
        PostReaction(post_id=2, user_id=3, reaction_id=2),
        PostReaction(post_id=3, user_id=1, reaction_id=3),
    ]
    db.session.add_all(post_reactions)
    db.session.commit()

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Resetting database...")
        # reset_database()
        print("Starting seed...")
        seed_users()
        seed_monsters()
        seed_npcs()
        seed_player()
        seed_posts()
        seed_reactions()
        seed_post_reactions()
        print("Seeding complete!")
