import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initializes the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

        # set start time.
        self.start_time = pygame.time.get_ticks()

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def simulate_movement(self):
        """Flips image horizontal after set amount of time"""
        # Get current time(ms) and set time interval(ms).
        current_time = pygame.time.get_ticks()
        interval = 1000

        if current_time > self.start_time + interval:
            # Flips image and resets the start time
            self.image = pygame.transform.flip(self.image, True, False)
            self.start_time = pygame.time.get_ticks()

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        self.simulate_movement()

