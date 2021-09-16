import sys

import pygame


class EventController:
    def __init__(self, space_ship, pygame):
        self.space_ship = space_ship
        self.pygame = pygame

    def on_event(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                sys.exit()
            elif event.type == self.pygame.KEYDOWN:
                self.on_key_down(event)
            elif event.type == self.pygame.KEYUP:
                self.on_key_up(event)

    def on_key_down(self, event):
        if event.key == self.pygame.K_RIGHT:
            self.space_ship.right_direction()
        elif event.key == self.pygame.K_LEFT:
            self.space_ship.left_direction()
        elif event.key == self.pygame.K_SPACE:
            self.space_ship.fire_bullet()

    def on_key_up(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.space_ship.stop()
        elif event.key == pygame.K_SPACE:
            self.space_ship.hold_fire()
