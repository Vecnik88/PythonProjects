class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0,0,0)
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #параметры пули
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,0
        self.bullets_allowed = 3 #ограничение по пулям, не более 3-х пуль на экране
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #темп ускорения игры
        self.speedup_scale = 1.1
        #темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

        #fleet_direction = 1 - движение вправо, -1 влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
