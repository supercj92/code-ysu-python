import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ship, screen):
        super(Bullet, self).__init__()
        self.screen = screen
        self.color = (60, 60, 60)
        self.bullet_width = ship.game_config.bullet_width
        self.bullet_height = ship.game_config.bullet_height
        self.bullet_speed = ship.game_config.bullet_speed
        self.bullet_rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.bullet_rect.centerx = ship.ship_rect.centerx
        self.bullet_rect.bottom = ship.ship_rect.top

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)

    def update(self):
        self.bullet_rect.bottom -= self.bullet_speed

    def is_alive(self):
        return self.bullet_rect.bottom > 0
