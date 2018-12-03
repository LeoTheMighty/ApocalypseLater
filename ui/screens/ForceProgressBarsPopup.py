from ..Popup import Popup
from ..aspects.Label import Label
from ..aspects.ProgressBar import ProgressBar
import pygame
import os


class ForceProgressBarsPopup(Popup):
    def __init__(self, game_handler):
        super().__init__()
        self.game_handler = game_handler
        self.border_length = min(self.get_width() / 8, self.get_height() / 8)
        self.title = Label("title", "Apocalyptic Forces", (0, -self.get_height() / 2 + self.border_length, 400, 50), 30,
                           screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.add_sprite_group(self.title_group)
        # Evenly spread the bars from
        self.apocalypse_bar_group = pygame.sprite.Group()
        start_y = -self.get_height() / 2 + 2 * self.border_length
        end_y = self.get_height() / 2
        num_apocalypses = len(self.game_handler.apocalypse_handler.apocalypses)
        self.apocalypse_bars = {}
        for i in range(0, num_apocalypses):
            apocalypse_id = self.game_handler.apocalypse_handler.apocalypses[i].id
            y = start_y + (end_y - start_y) * i / num_apocalypses
            self.apocalypse_bars[apocalypse_id] = ProgressBar(str(i), self.game_handler.apocalypse_handler.apocalypses[i].force,
                                                         (0, 0, 255), (0, 0, 0), (0, y, self.get_width() / 2, 0.5 * (end_y - start_y) / num_apocalypses),
                                                         screen_size=self.screen_size)
            apocalypse_label = Label(str(i) + "_label", self.game_handler.apocalypse_handler.apocalypses[i].name,
                                     (-2 * self.get_width() / 6, y, 200, 50), 25, screen_size=self.screen_size)
            self.apocalypse_bar_group.add(self.apocalypse_bars[apocalypse_id], apocalypse_label)
        self.add_sprite_group(self.apocalypse_bar_group)

    def receive_next_values(self, next_values):
        for apocalypse in self.game_handler.apocalypse_handler.apocalypses:
            self.apocalypse_bars[apocalypse.id].set_percent(apocalypse.force)
