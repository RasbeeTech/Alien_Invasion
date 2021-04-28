import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """A class to handle explosion effect."""

    def __init__(self, center):
        """Initialize explosion effect."""
        super().__init__()

        # Load explosion images.
        self.explosion_image_1 = pygame.image.load('images/alien_hit_1.bmp')
        self.explosion_image_2 = pygame.image.load('images/alien_hit_2.bmp')

        # Load image and set rect attribute.
        self.image = self.explosion_image_1
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Set the effect's start time.
        self.start_time = pygame.time.get_ticks()

    def update(self):
        """Allow the explosion effect to last for a period of time."""
        # Get the current time and set the effects time span.
        #   Time is in milliseconds (1000ms = 1s).
        current_time = pygame.time.get_ticks()
        time_span = 200
        lapsed_time = current_time - self.start_time

        # Switch explosion images during second half of effect.
        if self.image == self.explosion_image_1 and lapsed_time > time_span * 0.5:
            self.image = self.explosion_image_2
        # Destroy object after 2 seconds
        if current_time > self.start_time + time_span:
            self.kill()
