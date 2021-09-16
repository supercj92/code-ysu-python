#!/usr/bin env python
# coding=utf-8
import pygame
import ship
import game_frame
import event_controller
import game_config
import character_controller
import time


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    my_game_config = game_config.GameConfig()
    screen = create_screen(pygame, my_game_config)
    # 创建飞船
    my_space_ship = ship.Ship(screen, my_game_config)
    # 创建屏幕刷新器
    my_game_frame = game_frame.GameFrame(my_space_ship)
    # 处理用户控制指令
    my_event_controller = event_controller.EventController(my_space_ship, pygame)
    # 控制游戏元素状态
    my_character_controller = character_controller.CharacterController(my_space_ship)

    # 开始游戏的主循环
    while True:
        start_time = time.time()
        time.sleep(0.01)
        # 监视键盘和鼠标事件
        my_event_controller.on_event()

        # 更新角色状态
        my_character_controller.update_character()

        # 刷新画面
        my_game_frame.draw(screen, my_game_config)
        end_time = time.time()
        print('one loop cost %d' % (start_time - end_time))


def create_screen(pygame, game_config):
    screen = pygame.display.set_mode(game_config.window_size)
    pygame.display.set_caption(game_config.game_name)
    return screen


if __name__ == '__main__':
    run_game()
