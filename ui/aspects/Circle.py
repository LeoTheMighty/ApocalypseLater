from .Image import create_image, get_centered_rect
from ..Sprite import Sprite
from ..UIConstants import *
import pygame


class Circle(Sprite):
    def __init__(self, color, rect, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        super().__init__()
        _, _, width, height = rect
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.radius = min(int(width / 2), int(height / 2))
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.image = self.image.convert_alpha()

        # TODO Option not to be centered?
        self.rect, self.screen_rect = get_centered_rect(rect, screen_size)

    def change_color(self, color):
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.image = self.image.convert_alpha()

    def refresh(self):
        return

    def release(self):
        return None

    def highlight(self):
        return None

    def push(self):
        return None

    def click(self):
        return None
