from ..Popup import Popup
from ..aspects.Button import Button
from ..aspects.Label import Label
import pygame
import os


class InfoPopup(Popup):
    def __init__(self):
        super().__init__()
        # self.width, self.height = self.screen_size
        self.border_length = min(self.width / 10, self.height / 10)
        self.title = Label("title", "Info", (0, -self.get_height() / 2 + self.border_length, 400, 50), 30, screen_size=self.screen_size)
        self.title_group = pygame.sprite.Group()
        self.title_group.add(self.title)
        self.add_sprite_group(self.title_group)
        self.next_button = Button("next_button", (self.get_width() / 2 - 2.25 * self.border_length, self.get_height() / 2 - 1.5 * self.border_length,
            50, 50), os.path.join("img", "next_button.png"), os.path.join("img", "next_button_highlighted.png"),
                                  os.path.join("img", "next_button_pressed.png"), screen_size=self.screen_size)
        self.next_button_group = pygame.sprite.Group()
        self.next_button_group.add(self.next_button)
        self.add_sprite_group(self.next_button_group)
        self.page_index = 0
        self.num_pages = 7
        self.page_group = pygame.sprite.Group()
        self.description = Label("description", "", (0, self.get_height() / 16, self.get_width() - 2 * self.border_length, self.get_height() / 1.5), 20, screen_size=self.screen_size)
        self.page_group.add(self.description)
        self.add_sprite_group(self.page_group)

    def receive_next_values(self, next_values):
        self.draw_page(0)

    def draw_page(self, index):
        description = ""
        if index == 0:
            # TODO Tell information about the game as a whole
            description = "Hello! This game is about defending the world from the apocalypse! You are now a billionaire who got a billion " + \
                          "dollars from their father who passed away and with recent news concerning you, you decide to make a difference! " + \
                          "Using your wealth and strategic planning, you must find a way to funnel your funds into the right places so you " + \
                          "can avoid the destruction of the planet and bankruptcy (otherwise, you won't be able to help others!)"
            pass
        elif index == 1:
            # TODO Point to the money and say these are our current funds and say we can see how much money we get per year by clicking it
            # TODO Also point to the year
            description = "If you look above and to the right, you'll find the year and your current funds. This will be crucial " + \
                          "to managing your economy. By clicking on the money label, you can also view your \"trickle\", aka how much " + \
                          "money you're making per year."
            pass
        elif index == 2:
            # TODO Point to the apocalypse bars and say these are your indicators for how close each apocalypse is
            # TODO Also point out that you can also see your force for the closest apocalypse.
            # TODO Mention that each apocalypse has a trickle to it that increases it by an amount each year, but your force doesn't
            description = "To the left of that, you'll find the Apocalypse bars, which indicate how close the closest apocalypse is " + \
                          "to occuring and how strong your force against it is. By clicking on the bars, you can also view the closeness " + \
                          "and your force of each individual apocalypse happening."
            pass
        elif index == 3:
            # TODO Point to a place icon and say these are the places that we either control or have influence over.
            # TODO The places we control we can fund to increase our forces, the places we don't we can funnel money into and help prevent the apocalypses or get a better money trickle
            description = "If we look on the map, we'll find buttons for each place that we have influence over. We either control them " + \
                          "and we can fund them to increase our forces, or they are owned by someone else and we can funnel funds into " + \
                          "them to both lower apocalypse rates and/or closeness and potentially increase our revenue stream!"
            pass
        elif index == 4:
            # TODO Point to the news reel and say that this shows the recent events that have happened which have direct impact on the apocalypses
            description = "If we look below at the bottom, we'll find the news reel, where we can find events that are " + \
                          "happening. These events have profound consequences on what we do, and some of them will even ask us to make decisions. " + \
                          "If we click on it, we can view the most recent events from the past."
            pass
        elif index == 5:
            # TODO Point at the speed and settings and say that this controls how fast time moves and can save or exit your game
            description = "If we look to the bottom right, we'll find the settings and the speed, which can exit/save your game and change the speed"
            pass
        elif index == 6:
            # TODO point at the info button and say to view this info at any time, click on this button
            description = "Finally, you can click on the button to the bottom left to view this screen again at any time! Have fun playing Apocalypse Later!"
            pass
        self.description.change_label(description)

    def next_page(self):
        self.page_index += 1
        self.page_index %= self.num_pages
        self.draw_page(self.page_index)

    def action(self, identifier):
        if identifier == self.next_button.identifier:
            self.next_page()
        return super().action(identifier)
