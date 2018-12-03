from .Image import create_image, get_centered_rect
from .TextBox import create_text_box
from .Button import Button
from ..UIConstants import *
import pygame
import os


class LabeledButton(Button):
    def __init__(self, identifier, text, rect, font=None, font_size=30, button_image_path=os.path.join("img", "button.png"), highlighted_button_image_path=os.path.join("img", "button_highlighted.png"), pushed_button_image_path=os.path.join("img", "button_pressed.png"), screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        super().__init__(identifier, rect, button_image_path, highlighted_button_image_path, pushed_button_image_path, screen_size)
        _, _, self.width, self.height = rect
        self.font_size = font_size
        self.identifier = identifier
        if font is None:
            # self.font = pygame.font.Font(os.path.join("fonts", "OpenSans-Regular.ttf"), font_size)
            self.font = pygame.font.Font(os.path.join("fonts", "Caviar_Dreams_Bold.ttf"), font_size)
        else:
            self.font = font
        self.text_surface = create_text_box(text, font_size, self.width, self.height, (0, 0, 0), self.font, True, False, False)
        self.backup = pygame.Surface((self.width, self.height))
        self.backup_highlighted = pygame.Surface((self.width, self.height))
        self.backup_pressed = pygame.Surface((self.width, self.height))
        self.backup.blit(self.button_image, (0, 0))
        self.backup_highlighted.blit(self.highlighted_button_image, (0, 0))
        self.backup_pressed.blit(self.pushed_button_image, (0, 0))
        self.button_image.blit(self.text_surface, (0, 0))
        self.highlighted_button_image.blit(self.text_surface, (0, 0))
        self.pushed_button_image.blit(self.text_surface, (0, 0))
        self.image = self.button_image

        # TODO Option not to be centered?
        self.rect, self.screen_rect = get_centered_rect(rect, screen_size)

    def change_text(self, text):
        self.text_surface = create_text_box(text, self.font_size, self.width, self.height, (0, 0, 0), self.font, True, False, False)
        self.button_image = pygame.Surface((self.width, self.height))
        self.highlighted_button_image = pygame.Surface((self.width, self.height))
        self.pushed_button_image = pygame.Surface((self.width, self.height))
        self.button_image.blit(self.backup, (0, 0))
        self.highlighted_button_image.blit(self.backup_highlighted, (0, 0))
        self.pushed_button_image.blit(self.backup_pressed, (0, 0))
        self.button_image.blit(self.text_surface, (0, 0))
        self.highlighted_button_image.blit(self.text_surface, (0, 0))
        self.pushed_button_image.blit(self.text_surface, (0, 0))

