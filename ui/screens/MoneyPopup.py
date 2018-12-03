from ..Popup import Popup
from ..aspects.Label import Label
import pygame
import os


class MoneyPopup(Popup):
    def __init__(self, game_handler):
        self.game_handler = game_handler
        super().__init__()
        self.border_length = min(self.get_width() / 8, self.get_height() / 8)
        self.title = Label("title", "Money", (0, -self.get_height() / 2 + self.border_length, 200, 50), 30, screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.add_sprite_group(self.title_group)
        self.label_group = pygame.sprite.Group()
        self.money_label = Label("money", game_handler.get_money_text(), (0, 0, self.get_width(), self.get_height() / 2), 45, screen_size=self.screen_size)
        self.money_trickle_label = Label("money_trickle", "", (0, self.get_height() / 4, self.get_width(), self.get_height() / 4), 25, screen_size=self.screen_size)
        self.label_group.add(self.money_label)
        self.label_group.add(self.money_trickle_label)
        self.add_sprite_group(self.label_group)
        # Display money plus the trickle

    def receive_next_values(self, next_values):
        self.money_label.change_label(self.game_handler.get_money_text())
        money_trickle = self.game_handler.money_trickle
        color = (0, 0, 0)
        addition = ""
        if money_trickle > 0:
            addition = "+"
            color = (0, 255, 0)
        elif money_trickle < 0:
            color = (255, 0, 0)
        self.money_trickle_label.change_color(color)
        self.money_trickle_label.change_label(addition + str(money_trickle))
