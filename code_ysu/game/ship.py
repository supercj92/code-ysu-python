import pygame
import bullet
from pygame.sprite import Group


class Ship:
    """玩家控制的飞船"""

    def __init__(self, screen, game_config):
        self.screen = screen
        self.ship_img = pygame.image.load('resources/ship.bmp')
        self.ship_rect = self.ship_img.get_rect()
        self.screen_rect = screen.get_rect()
        self.center_ship()
        self.game_config = game_config
        self.ship_move_direction = 0
        self.bullet_group = Group()
        self.firing_bullet = 0

    def center_ship(self):
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

    def fire_bullet(self):
        self.firing_bullet = 1
        self.do_fire_bullet()
        print('bullet len %d' % len(self.bullet_group))

    def do_fire_bullet(self):
        my_bullet = bullet.Bullet(self, self.screen)
        self.bullet_group.add(my_bullet)

    def hold_fire(self):
        self.firing_bullet = 2

    def update_bullets(self):

        # 持续发射字段模式
        if self.game_config.continue_fire and self.firing_bullet == 1:
            self.do_fire_bullet()

        for bullet_item in self.bullet_group.copy():
            if not bullet_item.is_alive():
                self.bullet_group.remove(bullet_item)

        self.bullet_group.update()

    def draw_bullets(self):
        # print('bullet group len %d ' % len(self.bullet_group))
        for bullet_item in self.bullet_group.sprites():
            bullet_item.draw_bullet()

    def draw(self):
        self.draw_bullets()
        self.draw_ship()

    # 在屏幕上绘制飞船
    def draw_ship(self):
        self.screen.blit(self.ship_img, self.ship_rect)

    def right_direction(self):
        self.ship_move_direction = 1

    def left_direction(self):
        self.ship_move_direction = 2

    def stop(self):
        self.ship_move_direction = 0

    def update(self):
        self.update_bullets()
        self.update_ship()

    def update_ship(self):
        if self.ship_move_direction == 1:
            self.move_right()

        if self.ship_move_direction == 2:
            self.move_left()

    def move_left(self):
        self.ship_rect.centerx -= self.game_config.space_ship_speed

    def move_right(self):
        self.ship_rect.centerx += self.game_config.space_ship_speed
