import pygame
from ui.Screen import Screen
from ui.aspects.Button import Button
from ui.UIConstants import *
import os


class Popup(Screen):
    def __init__(self, background_image_path=os.path.join("img", "rounded_rectangle.png"), percent_width=75, percent_height=75):
        width = int(SCREEN_WIDTH * percent_width / 100)
        height = int(SCREEN_HEIGHT * percent_height / 100)
        self.width = width
        self.height = height
        self.screen_size = (width, height)
        super().__init__(background_image_path, width, height)
        popup_button_group = pygame.sprite.Group()
        side_length = min(width / 8, height / 8)
        close_button = Button("close", (3 * width / 8, -3 * height / 8, side_length, side_length),
                              os.path.join("img", "x_button.png"),
                              os.path.join("img", "x_button_highlighted.png"),
                              os.path.join("img", "x_button_pressed.png"),
                              (width, height))
        # print(close_button.rect)
        # print(close_button.screen_rect)
        popup_button_group.add(close_button)
        self.add_sprite_group(popup_button_group)

    def action(self, identifier):
        if identifier == "close":
            return -1, None
        return None, None

