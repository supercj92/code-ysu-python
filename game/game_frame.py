import pygame


class GameFrame:
    """画面帧"""
    def __init__(self, space_ship):
        self.space_ship = space_ship

    def draw(self, screen, game_config):
        # 更新屏幕上的图像，并切换到新屏幕
        screen.fill(game_config.bg_color)

        self.space_ship.draw()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
