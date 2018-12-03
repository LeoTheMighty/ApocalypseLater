from ..Popup import Popup
from ..aspects.Label import Label
from ..aspects.LabeledButton import LabeledButton
import pygame
import os


class SettingsPopup(Popup):
    def __init__(self, game_handler):
        super().__init__()
        self.border_length = min(self.get_width() / 8, self.get_height() / 8)
        self.title = Label("title", "Settings", (0, -self.get_height() / 2 + self.border_length, 200, 50), 30, screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.add_sprite_group(self.title_group)
        self.exit_game_button = LabeledButton("exit_game", "Exit Game", (0, 0, 200, 50), screen_size=self.screen_size)
        self.exit_game_button_group = pygame.sprite.Group()
        self.exit_game_button_group.add(self.exit_game_button)
        self.add_sprite_group(self.exit_game_button_group)

    def action(self, identifier):
        if identifier == self.exit_game_button.identifier:
            return 0, None
        return super().action(identifier)
