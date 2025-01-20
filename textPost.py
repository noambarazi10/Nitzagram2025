import pygame
from constants import *
from classes import Post



class TextPost:
    def __init__(self, text, text_color, background_color):
        self.text = text
        self.text_color = text_color
        self.background_color = background_color



    def display(self):
        pygame.init()
        surface = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        surface.fill(self.background_color)
        font = pygame.font.Font(None, TEXT_POST_FONT_SIZE)
        text_surface = font.render(self.text, True, self.text_color)
        surface.blit(text_surface, (POST_X_POS, POST_Y_POS))
        Post.Post.display()


