from .Image import create_image, get_centered_rect
from ..Sprite import Sprite
from ..UIConstants import *


class Button(Sprite):
    def __init__(self, identifier, rect, button_image_path, highlighted_button_image_path, pushed_button_image_path, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        super().__init__()
        _, _, width, height = rect
        self.button_image = create_image(width, height, button_image_path)
        self.highlighted_button_image = create_image(width, height, highlighted_button_image_path)
        self.pushed_button_image = create_image(width, height, pushed_button_image_path)
        self.image = self.button_image
        self.identifier = identifier

        # TODO Option not to be centered?
        self.rect, self.screen_rect = get_centered_rect(rect, screen_size)

    def refresh(self):
        return

    def push(self):
        self.image = self.pushed_button_image
        return None

    def highlight(self):
        self.image = self.highlighted_button_image
        return None

    def release(self):
        self.image = self.button_image
        return None

    def click(self):
        return self.identifier
