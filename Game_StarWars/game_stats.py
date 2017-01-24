class GameStats():
    ####отслеживаем статистику
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0 #рекорд

    def reset_stats(self):
        #Инициализируем статистику
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
