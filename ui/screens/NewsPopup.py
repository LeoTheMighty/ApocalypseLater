from ..Popup import Popup
from ..aspects.Label import Label
from ..logic.GameHandler import GameHandler
from ..logic.LogicConstants import *
import pygame
import os


class NewsPopup(Popup):
    def __init__(self, game_handler):
        super().__init__()
        self.game_handler = game_handler
        self.border_length = min(self.get_width() / 8, self.get_height() / 8)
        self.title = Label("title", "News", (0, -self.get_height() / 2 + self.border_length, 200, 50), 30, screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.add_sprite_group(self.title_group)
        self.news_events_group = pygame.sprite.Group()
        self.add_sprite_group(self.news_events_group)

    def receive_next_values(self, next_values):
        # self.game_handler = GameHandler()
        self.news_events_group.empty()
        # num_events = len(self.game_handler.news_events)
        for i, event in enumerate(self.game_handler.news_events):
            start_y = -self.get_height() / 2 + 2 * self.border_length
            end_y = self.get_height() / 2
            y = start_y + (end_y - start_y) * i / MAX_NEWS_EVENTS
            news_label = Label(str(i), event.title, (0, y, 4 * self.get_width() / 5, (end_y - start_y) / MAX_NEWS_EVENTS), font_size=20, screen_size=self.screen_size)
            self.news_events_group.add(news_label)


