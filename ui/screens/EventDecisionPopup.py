from ..Popup import Popup
from ..aspects.Label import Label
from ..aspects.LabeledButton import LabeledButton
from ..logic.GameHandler import GameHandler
import pygame
import os


class EventDecisionPopup(Popup):
    def __init__(self, game_handler):
        super().__init__()
        self.game_handler = game_handler
        self.border_length = min(self.get_width() / 8, self.get_height() / 8)
        font = pygame.font.Font(os.path.join("fonts", "OpenSans-Regular.ttf"), 30)
        self.title = Label("title", "", (0, -self.get_height() / 2 + 2 * self.border_length, 3 * self.get_width() / 4, self.get_height() / 2), 30, screen_size=self.screen_size)
        self.description = Label("description", "", (0, 0, self.get_width() - (2 * self.border_length), self.get_height() / 2), 30, font=font, screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.title_group.add(self.description)
        self.add_sprite_group(self.title_group)
        self.accept_button = LabeledButton("accept_button", "Accept", (- self.get_width() / 4, self.get_height() / 2 - self.border_length, 200, 40), screen_size=self.screen_size)
        self.decline_button = LabeledButton("decline_button", "Decline", (self.get_width() / 4, self.get_height() / 2 - self.border_length, 200, 40), screen_size=self.screen_size)
        self.action_button_group = pygame.sprite.Group()
        self.action_button_group.add(self.accept_button)
        self.action_button_group.add(self.decline_button)
        self.add_sprite_group(self.action_button_group)

    def receive_next_values(self, next_values):
        # This will basically tell you when it opens
        # self.game_handler = GameHandler()
        event = self.game_handler.deciding_event
        self.title.change_label(event.title)
        self.description.change_label(event.message)

    def action(self, identifier):
        # Make sure that the close icon will not work
        if identifier == self.accept_button.identifier:
            # TODO Accept the event
            self.game_handler.handle_event(self.game_handler.deciding_event)
            self.game_handler.unset_deciding_event()
            return -1, None
        elif identifier == self.decline_button.identifier:
            # TODO Decline the event
            self.game_handler.unset_deciding_event()
            return -1, None
        return None, None
