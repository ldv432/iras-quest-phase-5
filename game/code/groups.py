from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()
    def update_camera(self, target_pos):
        """Update the camera offset to center on the new target position."""
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH // 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT // 2)

    def draw(self, target_pos, map_width, map_height, zoom_factor=1):
        """Draw all sprites with the camera's offset applied."""
        self.update_camera(target_pos)  # Ensure camera is centered on the target
        zoomed_width = WINDOW_WIDTH / zoom_factor
        zoomed_height = WINDOW_HEIGHT / zoom_factor
        temp_surface = pygame.Surface((zoomed_width, zoomed_height))

        # Calculate the offset for centering the camera on the target
        self.offset.x = -(target_pos[0] - zoomed_width / 2)
        self.offset.y = -(target_pos[1] - zoomed_height / 2)

        # Clamp the offset to prevent black space
        self.offset.x = max(-(map_width - zoomed_width), min(0, self.offset.x))
        self.offset.y = max(-(map_height - zoomed_height), min(0, self.offset.y))

        # Draw all sprites with the clamped offset to the temporary surface
        for sprite in self:
            offset_pos = sprite.rect.topleft + self.offset
            temp_surface.blit(sprite.image, offset_pos)

        # Scale the temporary surface to the main display
        scaled_surface = pygame.transform.scale(temp_surface, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface.blit(scaled_surface, (0, 0))

