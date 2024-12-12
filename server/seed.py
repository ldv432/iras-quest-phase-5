#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from config import db
from models.monster import Monster
from models.npc import Npc
from models.player import Player


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
        Npc(dialogue="You are nearly there... The King is waiting.")
    ]
    db.session.add_all(npcs)
    db.session.commit()

def seed_player():
    player = [
        Player(health=100, power=20, score=0, time=0, user_id=0)
    ]
    db.session.add_all(player)
    db.session.commit()

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        seed_monsters()
        seed_npcs()
        seed_player()
        
