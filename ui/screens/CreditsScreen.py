from ui.Screen import Screen
from ..aspects.Label import Label
from ..aspects.LabeledButton import LabeledButton
import pygame
import os


class CreditsScreen(Screen):
    def __init__(self):
        super().__init__(os.path.join("img", "granite.jpg"))
        self.label_group = pygame.sprite.Group()
        self.link = Label("link", "Go to https://github.com/LeoTheMighty/ApocalypseLater to try it for yourself!", \
                          (0, -self.get_height() / 4, self.get_width(), 100))
        self.credit = Label("credit", "Thanks to Professor Winborne from Northeastern University for inspiring the Apocalyptic themes!", \
                          (0, 0 * self.get_height() / 4, self.get_width(), 100), font_size=20)
        self.back_button = LabeledButton("back_button", "Back", (0, self.get_height() / 4, 200, 50))
        self.label_group.add(self.link, self.credit, self.back_button)
        self.add_sprite_group(self.label_group)

    def action(self, identifier):
        if identifier == self.back_button.identifier:
            return -1, None
        return None, None
