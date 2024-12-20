from settings import *
from sprites import Sprite
from player import Player
from groups import AllSprites
from npc import Npc


class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()
        self.map_width = tmx_map.width * TILE_SIZE
        self.map_height = tmx_map.height * TILE_SIZE
        # groups
        self.all_sprites = AllSprites()
        self.kill_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup(tmx_map)

    def setup(self, tmx_map):
        for layer in ["Backdrop", "Decoration"]:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for x, y, surf in tmx_map.get_layer_by_name("Killtiles").tiles():
            print(f"Loaded kill tile at ({x}, {y})")
            Sprite(
                (x * TILE_SIZE, y * TILE_SIZE),
                surf,
                (self.all_sprites, self.kill_sprites),  # Add to kill_sprites
            )

        for layer in ["Platforms"]:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                print(f"Loaded tile at ({x}, {y}) in layer {layer}")
                Sprite(
                    (x * TILE_SIZE, y * TILE_SIZE),
                    surf,
                    (self.all_sprites, self.collision_sprites),
                )

        for obj in tmx_map.get_layer_by_name("Objects"):
            print(f"Loaded object {obj.name} at ({obj.x}, {obj.y})")
            if obj.name == "player":
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites, self.kill_sprites)
            if obj.name == "npc1":
                self.npc = Npc((obj.x, obj.y), self.all_sprites, self.collision_sprites)

    def draw_death_counter(self):
        font = pygame.font.Font(None, 36)
        death_text = font.render(f"Deaths: {self.player.death_count}", True, (255, 255, 255))  # White text
        outline_color = (0, 0, 0)  # Black outline color

        text_rect = death_text.get_rect(topleft=(10, 10))  # Position at the top left

        # Render the outline by drawing slightly offset versions of the text
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Offsets for corners
            outline_text = font.render(f"Deaths: {self.player.death_count}", True, outline_color)
            self.display_surface.blit(outline_text, text_rect.move(dx, dy))

        # Render the main text on top of the outline
        self.display_surface.blit(death_text, text_rect)


    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill("black")
        self.all_sprites.draw(self.player.rect.center, self.map_width, self.map_height, ZOOM_FACTOR)
        self.draw_death_counter()
