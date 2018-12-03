from ..Sprite import Sprite
import pygame
from ..UIConstants import *
from .Image import get_centered_rect


class ProgressBar(Sprite):
    def __init__(self, identifier, percent, color, border_color, rect, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        super().__init__()
        self.identifier = identifier
        self.percent = min(percent, 100)
        self.color = color
        _, _, self.width, self.height = rect

        self.rect, self.screen_rect = get_centered_rect(rect, screen_size)

        # Create the bar
        self.image = pygame.Surface((int(self.width), int(self.height)))
        self.image.fill((0, 0, 0))
        border_length = self.height / 8
        bar_width = self.width - (2 * border_length)
        bar_height = self.height - (2 * border_length)
        pygame.draw.rect(self.image, border_color, (int(border_length), int(border_length), int(bar_width), int(bar_height)))
        pygame.draw.rect(self.image, self.color, (int(border_length), int(border_length), int(self.percent * bar_width / 100), int(bar_height)))
        self.image = self.image.convert_alpha()

    def set_percent(self, percent):
        self.percent = min(100, percent)
        # Create the bar
        self.image = pygame.Surface((int(self.width), int(self.height)))
        self.image.fill((0, 0, 0))
        border_length = self.height / 8
        bar_width = self.width - (2 * border_length)
        bar_height = self.height - (2 * border_length)
        pygame.draw.rect(self.image, (255, 255, 255), (int(border_length), int(border_length), int(bar_width), int(bar_height)))
        pygame.draw.rect(self.image, self.color, (int(border_length), int(border_length), int(self.percent * bar_width / 100), int(bar_height)))
        self.image = self.image.convert_alpha()

    def refresh(self):
        return

    def push(self):
        return None

    def highlight(self):
        return None

    def release(self):
        return None

    def click(self):
        return self.identifier
