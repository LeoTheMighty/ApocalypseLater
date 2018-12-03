import pygame
from ..UIConstants import *


def create_image(width, height, path):
    width = int(width)
    height = int(height)
    # print(width, height)
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (width, height))
    return image.convert_alpha()


def get_centered_rect(rect, screen_size):
    x, y, width, height = rect
    screen_width, screen_height = screen_size
    rect = pygame.Rect(
        int((x + ((screen_width - width) / 2))),
        int((y + ((screen_height - height) / 2))),
        int(width),
        int(height)
    )
    screen_rect = pygame.Rect(
        int(rect.x + (SCREEN_WIDTH / 2) - (screen_width / 2)),
        int(rect.y + (SCREEN_HEIGHT / 2) - (screen_height / 2)),
        int(width),
        int(height)
    )
    return rect, screen_rect
