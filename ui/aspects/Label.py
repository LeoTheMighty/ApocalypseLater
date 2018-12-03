import pygame
from ..Sprite import Sprite
from .TextBox import create_text_box
from .Image import get_centered_rect
from ..UIConstants import *
import os


class Label(Sprite):
    def __init__(self, identifier, text, rect, font_size=30, font=None, font_color=(0, 0, 0), screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        super().__init__()
        self.image = None
        self.identifier = identifier
        self.text = text
        self.rect, self.screen_rect = get_centered_rect(rect, screen_size)
        self.font_color = font_color
        if font is None:
            # self.font = pygame.font.SysFont("Times New Roman", 20, True)
            self.font = pygame.font.Font(os.path.join("fonts", "OpenSans-Bold.ttf"), font_size)
        else:
            self.font = font
        self.draw_label()

    def change_label(self, label):
        self.text = label
        self.draw_label()

    def change_color(self, color):
        self.font_color = color
        self.draw_label()

    def draw_label(self):
        self.image = create_text_box(self.text, 50, self.rect[2], self.rect[3], self.font_color, self.font, True, True, False)

    def refresh(self):
        return

    def highlight(self):
        return

    def push(self):
        return

    def release(self):
        return

    def click(self):
        return self.identifier
