#!/usr/bin/python
# -*- coding:utf8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    # 创建一艘飞船

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()