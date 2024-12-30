import pygame
from sys import exit
from random import randint, choice
import os

os.environ['SDL_AUDIODRIVER'] = 'alsa' 

# Initialize pygame and mixer
pygame.init()

# Try initializing the mixer
try:
    pygame.mixer.init()  # Initializes the mixer module for sound
except pygame.error as e:
    print(f"Error initializing pygame.mixer: {e}")
    exit()  # Exit the program if mixer fails to initialize

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/2.png').convert_alpha()
        player_walk_3 = pygame.image.load('graphics/Player/3.png').convert_alpha()
        player_walk_4 = pygame.image.load('graphics/Player/4.png').convert_alpha()

        # Scale images here (adjust the scale factor as needed)
        scale_factor = 3 # Example: scaling by a factor of 2
        player_walk_1 = pygame.transform.scale(player_walk_1, (player_walk_1.get_width() * scale_factor, player_walk_1.get_height() * scale_factor))
        player_walk_2 = pygame.transform.scale(player_walk_2, (player_walk_2.get_width() * scale_factor, player_walk_2.get_height() * scale_factor))
        player_walk_3 = pygame.transform.scale(player_walk_3, (player_walk_3.get_width() * scale_factor, player_walk_3.get_height() * scale_factor))
        player_walk_4 = pygame.transform.scale(player_walk_4, (player_walk_4.get_width() * scale_factor, player_walk_4.get_height() * scale_factor))

        self.player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        # Scale jump image
        self.player_jump = pygame.transform.scale(self.player_jump, (self.player_jump.get_width() * scale_factor, self.player_jump.get_height() * scale_factor))

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))  # You can adjust the position here if needed
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.ogg')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'Bat':
            # Load Bat images
            Bat_1 = pygame.image.load('graphics/Bat/Bat1.png').convert_alpha()
            Bat_2 = pygame.image.load('graphics/Bat/Bat2.png').convert_alpha()
            Bat_3 = pygame.image.load('graphics/Bat/Bat3.png').convert_alpha()

            # Scale Bat images here (adjust the scale factor as needed)
            scale_factor = 3  # Example: scaling by a factor of 2
            Bat_1 = pygame.transform.scale(Bat_1, (Bat_1.get_width() * scale_factor, Bat_1.get_height() * scale_factor))
            Bat_2 = pygame.transform.scale(Bat_2, (Bat_2.get_width() * scale_factor, Bat_2.get_height() * scale_factor))
            Bat_3 = pygame.transform.scale(Bat_3, (Bat_3.get_width() * scale_factor, Bat_3.get_height() * scale_factor))

            # Store the frames
            self.frames = [Bat_1, Bat_2, Bat_3]
            y_pos = 210
        else:
            Snake_1 = pygame.image.load('graphics/Snake/Snake1.png').convert_alpha()
            Snake_2 = pygame.image.load('graphics/Snake/Snake2.png').convert_alpha()
            Snake_3 = pygame.image.load('graphics/Snake/Snake3.png').convert_alpha()
            Snake_4 = pygame.image.load('graphics/Snake/Snake4.png').convert_alpha()
            
            # Scale Snake images here (adjust the scale factor as needed)
            scale_factor = 3  # Example: scaling by a factor of 3
            Snake_1 = pygame.transform.scale(Snake_1, (Snake_1.get_width() * scale_factor, Snake_1.get_height() * scale_factor))
            Snake_2 = pygame.transform.scale(Snake_2, (Snake_2.get_width() * scale_factor, Snake_2.get_height() * scale_factor))
            Snake_3 = pygame.transform.scale(Snake_3, (Snake_3.get_width() * scale_factor, Snake_3.get_height() * scale_factor))
            Snake_4 = pygame.transform.scale(Snake_4, (Snake_4.get_width() * scale_factor, Snake_4.get_height() * scale_factor))

            self.frames = [Snake_1, Snake_2, Snake_3, Snake_4]
            y_pos = 300  # Position of the Snake (you can adjust as needed)

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: 
        return True

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()  # This ensures that the mixer is initialized properly

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pre-Alpha: Ira\'s Quest')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# Initialize background music
bg_music = pygame.mixer.Sound('audio/IrasQuestMusic.ogg')
bg_music.play(loops=-1)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Load walking animation images
player_walk_1 = pygame.image.load('graphics/Player/1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/2.png').convert_alpha()
player_walk_3 = pygame.image.load('graphics/Player/3.png').convert_alpha()
player_walk_4 = pygame.image.load('graphics/Player/4.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
player_index = 0

# Scale the walking images
scale_factor = 3  # Adjust scale factor as needed
player_walk = [pygame.transform.scale(img, (img.get_width() * scale_factor, img.get_height() * scale_factor)) for img in player_walk]

# Game title and message
game_name = test_font.render('Ira\'s Quest', False, (255, 255, 255))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, (255, 255, 255))
game_message_rect = game_message.get_rect(center=(400, 330))

# Set initial position for the player (centered)
player_rect = player_walk[0].get_rect(center=(400, 200))  # Keep player centered
game_active = False
score = 0  # Initialize the score

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['Bat', 'Snake', 'Snake', 'Snake'])))
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)


    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()
        
    else:
        screen.fill((94, 129, 162))  # Background color

        # Loop through the walk images for animation (no horizontal movement)
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0

        # Set the current walking image
        player_image = player_walk[int(player_index)]

        # Draw the character running in place (no movement in x)
        screen.blit(player_image, player_rect)

        # Draw the game name and message
        screen.blit(game_name, game_name_rect)

        # If score is greater than 0, show the score message, otherwise show the "press space to run" message
        if score > 0: 
            score_message = test_font.render(f'Your score: {score}', False, (245, 245, 245))
            score_message_rect = score_message.get_rect(center=(400, 330))
            screen.blit(score_message, score_message_rect)
        else: 
            screen.blit(game_message, game_message_rect)

    pygame.display.update()
    clock.tick(60)
