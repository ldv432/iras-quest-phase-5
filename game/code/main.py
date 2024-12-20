from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join
import pygame.mixer
import sys


class Game:
    def __init__(self):
        pygame.init()

        # Attempt to initialize the mixer
        try:
            pygame.mixer.init()
            self.audio_enabled = True
        except pygame.error:
            print("Warning: Audio device not found. Audio will be disabled.")
            self.audio_enabled = False

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Ira's Quest")
        self.clock = pygame.time.Clock()

        # Load music if audio is enabled
        if self.audio_enabled:
            pygame.mixer.music.load(join("..", "audio", "Ira's Quest Main Theme.ogg"))
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

        self.tmx_maps = {0: load_pygame(join("..", "data", "levels", "1.tmx"))}
        self.current_stage = Level(self.tmx_maps[0])

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
