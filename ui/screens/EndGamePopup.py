from ..Popup import Popup
from ..aspects.Label import Label
from ..aspects.LabeledButton import LabeledButton
from ..logic.GameHandler import GameHandler
import pygame
import os


class EndGamePopup(Popup):
    def __init__(self, game_handler):
        super().__init__()
        self.game_handler = game_handler
        self.border_length = min(self.get_width() / 8, self.get_height() / 8)
        font = pygame.font.Font(os.path.join("fonts", "OpenSans-Regular.ttf"), 30)
        self.title = Label("title", "You Lose!", (0, -self.get_height() / 2 + 2 * self.border_length, 3 * self.get_width() / 4, self.get_height() / 2), 30, screen_size=self.screen_size)
        self.description = Label("description", "", (0, 0, self.get_width() - (2 * self.border_length), self.get_height() / 2), 30, font=font, screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.title_group.add(self.description)
        self.add_sprite_group(self.title_group)
        self.ok_button = LabeledButton("ok_button", "ok...", (0, self.get_height() / 2 - self.border_length, 200, 40), screen_size=self.screen_size)
        self.action_button_group = pygame.sprite.Group()
        self.action_button_group.add(self.ok_button)
        self.add_sprite_group(self.action_button_group)

    def receive_next_values(self, next_values):
        # This will basically tell you when it opens
        # self.game_handler = GameHandler()
        lose_message = self.game_handler.lose_message
        self.description.change_label(lose_message)

    def action(self, identifier):
        # Make sure that the close icon will not work
        if identifier == self.ok_button.identifier:
            # Okay, return back to main menu
            return 0, None
        return None, None
