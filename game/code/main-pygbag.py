from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join
import sys
import pygame.mixer
import asyncio  # Required for async handling in Pygbag

# Detect Pygbag environment
IS_WEB = hasattr(sys, "__EMSCRIPTEN__")


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

        # Display surface with resizable support for web
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Ira's Quest - Web Edition" if IS_WEB else "Ira's Quest")
        self.clock = pygame.time.Clock()

        # Load music if audio is enabled and not in web mode
        if self.audio_enabled:
            audio_path = join("audio", "Ira's Quest Main Theme.ogg")
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.set_volume(0.5)
            if not IS_WEB:
                pygame.mixer.music.play(-1)  # Infinite loop only for desktop

        # Adjust paths for levels
        self.tmx_maps = {0: load_pygame(join("data", "levels", "1.tmx"))}
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
    if IS_WEB:
        asyncio.run(game.run())  # Async execution for Pygbag
    else:
        game.run()  # Standard execution for desktop
