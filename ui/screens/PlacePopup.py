from ..Popup import Popup
from ..aspects.TextBox import Textbox
from ..aspects.Label import Label
from ..aspects.LabeledButton import LabeledButton
from ..logic.GameHandler import get_money_text
import pygame
import os


class PlacePopup(Popup):
    def __init__(self, place, game_handler):
        super().__init__()
        # For the place pop up, we want to show the Name (Big)
        # We also want to show the description
        self.game_handler = game_handler
        self.place = place

        # Two buttons, one for funneling money, one for
        self.border_length = min(self.get_width() / 8, self.get_height() / 8)
        font = pygame.font.Font(os.path.join("fonts", "OpenSans-Regular.ttf"), 30)
        self.title = Label("title", place.name, (0, -self.get_height() / 2 + 2 * self.border_length, 3 * self.get_width() / 4, self.get_height() / 2), 30, screen_size=self.screen_size)
        self.description = Label("description", place.description, (0, 0, self.get_width() - (2 * self.border_length), self.get_height() / 2), 30, font=font, screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.title_group.add(self.description)
        self.add_sprite_group(self.title_group)
        money = get_money_text(place.cost)
        self.funnel_button = LabeledButton("funnel_button", "Funnel Money (" + money + ")", (0, self.get_height() / 2 - self.border_length, 3 * self.get_width() / 4, 50), screen_size=self.screen_size)
        # self.take_money_button = LabeledButton("take_money_button", "Take Money", (self.get_width() / 4, self.get_height() / 2 - self.border_length, 200, 40), screen_size=self.screen_size)
        self.action_button_group = pygame.sprite.Group()
        self.action_button_group.add(self.funnel_button)
        # self.action_button_group.add(self.take_money_button)
        self.add_sprite_group(self.action_button_group)

    # def receive_next_values(self, next_values):
        # This will basically tell you when it opens
        # self.game_handler = GameHandler()

    def action(self, identifier):
        # Make sure that the close icon will not work
        if identifier == self.funnel_button.identifier:
            # Do the funnel!
            self.game_handler.handle_place_funnel(self.place)
            return -1, None
        return super().action(identifier)
