import sys
import game_functions as gf
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button #10
from scoreboard import Scoreboard

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Created ***Vecnik88***")
    #создаем кнопку play
    play_button = Button(ai_settings, screen, "Play")#20
    #создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    #создание пришельца
    alien = Alien(ai_settings, screen)
    #создание группы для хранения пуль
    bullets = Group()
    aliens = Group()

    #30 строка #создание флота пришельцев

    gf.create_fleet(ai_settings, screen, ship, aliens)

    #основной цикл игры

    while True:
        gf.check_events(ai_settings, screen,stats,sb, play_button,
                        ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)#40
            #print(len(bullets)) - проверка ограничения на пули
            gf.update_aliens(ai_settings, screen,stats, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                             play_button)

run_game()
