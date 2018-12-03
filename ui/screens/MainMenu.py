from ..Screen import Screen
from ..aspects.Button import Button
from ..aspects.LabeledButton import LabeledButton
# from ..aspects.TextBox import create_text_box
from ..aspects.TextBox import Textbox
import pygame
import os


class MainMenu(Screen):
    def __init__(self, game_handler):
        super().__init__(os.path.join("img", "granite.jpg"))
        self.buttons_group = None
        self.game_handler = game_handler
        self.add_buttons()
        # text = "one two three four five six seven eight nine ten"
        font = pygame.font.Font(os.path.join("fonts", "OpenSans-Bold.ttf"), 45)
        self.title_box = Textbox("Apocalypse Later", (0, -1 * self.get_width() / 10, 3 * self.get_width() / 4, self.get_height() / 2), 30, font=font, bold=True, centered=True)
        self.title_sprite_group = pygame.sprite.Group(self.title_box)
        self.add_sprite_group(self.title_sprite_group)

    def add_buttons(self):
        button_width = self.get_width() / 6
        button_height = self.get_height() / 12
        play_game_button = LabeledButton("play_game", "Play Game", (0, (-self.get_height() / 5), button_width, button_height), font_size=25)
        load_game_button = LabeledButton("load_game", "Load Game", (0, 0, button_width, button_height), font_size=25)
        credits_button = LabeledButton("credits", "Credits", (0, (self.get_height() / 5), button_width, button_height), font_size=25)
        exit_game_button = LabeledButton("exit_game", "Exit Game", (0, (2 * self.get_height() / 5), button_width, button_height), font_size=25)
        self.buttons_group = pygame.sprite.Group(play_game_button, load_game_button, credits_button, exit_game_button)
        self.add_sprite_group(self.buttons_group)

    def action(self, identifier):
        print("Received identifier: " + identifier)
        if identifier == "play_game":
            self.game_handler.initialize_game("Leo")
            return 0, self.game_handler
        elif identifier == "load_game":
            return 1, None
        elif identifier == "credits":
            return 2, None
        elif identifier == "exit_game":
            return 42069, None

