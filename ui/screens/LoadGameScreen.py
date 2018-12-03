from ..Screen import Screen
from ..aspects.Label import Label
from ..aspects.LabeledButton import LabeledButton
import pygame
import os


class LoadGameScreen(Screen):
    def __init__(self, game_handler):
        super().__init__(os.path.join("img", "granite.jpg"))
        self.label_group = pygame.sprite.Group()
        self.label = Label("label", "Not implemented yet!", (0, 0, 400, 50))
        self.labeled_button = LabeledButton("back", "Back", (0, self.get_height() / 4, 200, 40))
        self.label_group.add(self.label, self.labeled_button)
        self.add_sprite_group(self.label_group)

    def action(self, identifier):
        if identifier == self.labeled_button.identifier:
            return -1, None
        return None, None
