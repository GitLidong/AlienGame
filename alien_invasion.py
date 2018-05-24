#!/usr/bin/python
# -*- coding:utf8 -*-
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一群外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新子弹状态
        gf.update_bullets(bullets)
        # 更新屏幕上的图像
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
