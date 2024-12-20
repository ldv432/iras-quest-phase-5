from settings import *
from os.path import join

class Npc(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("..", "graphics", "npc", "npc_1.png"))
        self.rect = self.image.get_rect(topleft=pos)
        self.collision_sprites = collision_sprites

    def interact(self):
        # Logic for NPC interaction
        print("Hello! I am an NPC.")
