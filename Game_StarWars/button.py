import pygame.font

class Button():
    
    def __init__(self, ai_settings, screen, msg):
        """Атрибуты кнопок"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        "#10 строка" #назначение, размеры и свойства кнопок
        self.width, self.height = 200, 50
        self.button_color = (48, 213, 200)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #построение объекта rect кнопки и выравнивание по центру
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        "#20 строка" #сообщение кнопки, создается 1 раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        "Преобразует msg в прямоугольник, выравнивает текст по центру"
        self.msg_image = self.font.render(msg, True,self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

            
