from ..Screen import Screen
import pygame
from ..logic.GameHandler import GameHandler
# from ..UIConstants import SCREEN_WIDTH, SCREEN_HEIGHT
from ..aspects.Label import Label
from ..aspects.LabeledButton import LabeledButton
from ..aspects.Button import Button
from ..aspects.Circle import Circle
from ..aspects.ProgressBar import ProgressBar
from ..aspects.NewsPrompt import NewsPrompt
from ..aspects.SpeedButton import SpeedButton
import os
import colorsys
# from ..logic.CSVHandler import parse_csv_file


# def rgb_to_hsv(rgb):
# hsv = colorsys.rgb_to_hsv(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)


def hsv_to_rgb(hsv):
    rgb = colorsys.hsv_to_rgb(hsv[0] / 180, hsv[1] / 255, hsv[2] / 255)
    rgb = rgb[0] * 255, rgb[1] * 255, rgb[2] * 255
    print(rgb)
    return rgb


def color_2_gradient(start_color, end_color, percent):
    percent /= 100
    return (start_color[0] + (end_color[0] - start_color[0]) * percent), \
           (start_color[1] + (end_color[1] - start_color[1]) * percent), \
           (start_color[2] + (end_color[2] - start_color[2]) * percent)


def color_3_gradient(start_color, middle_color, end_color, percent):
    percent *= 2
    if percent < 100:
        end_color = middle_color
    else:
        start_color = middle_color
        percent -= 100
    percent /= 100
    return (start_color[0] + (end_color[0] - start_color[0]) * percent), \
           (start_color[1] + (end_color[1] - start_color[1]) * percent), \
           (start_color[2] + (end_color[2] - start_color[2]) * percent)


class GameScreen(Screen):
    def __init__(self, game_handler):
        super().__init__(os.path.join("img", "worldmap.png"))
        self.game_handler = game_handler
        self.if_first_entered = None
        self.place_button_size = min(self.get_width() / 16, self.get_height() / 16)
        self.initial_color = (0, 255, 0)
        green = (0, 255, 0)
        yellow = (255, 255, 0)
        red = (255, 0, 0)
        self.gradient = (green, yellow, red)
        self.initial_percent = 0
        # self.places = parse_csv_file(os.path.join("csv", "places.csv"))
        self.border_distance = min(1 * self.get_width() / 18, 1 * self.get_height() / 18)
        self.place_button_group = None
        self.place_buttons = None
        self.add_place_buttons()
        self.progress_bar_group = pygame.sprite.Group()
        self.percent = 0
        self.closeness_progress_bar = ProgressBar("closeness_progress_bar", self.percent, red, (255, 255, 255),
            (-self.get_width() / 2 + (4 * self.border_distance), -self.get_height() / 2 + (self.border_distance / 2), 200, 20))
        self.force_progress_bar = ProgressBar("force_progress_bar", self.percent, green, (255, 255, 255),
            (-self.get_width() / 2 + (4 * self.border_distance), -self.get_height() / 2 + (11 * self.border_distance / 8), 200, 20))
        self.progress_bar_group.add(self.closeness_progress_bar)
        self.progress_bar_group.add(self.force_progress_bar)
        self.add_sprite_group(self.progress_bar_group)
        self.news_prompt = NewsPrompt("news_prompt", (255, 255, 255), (0, self.get_height() / 2 - self.border_distance, 400, 40))
        self.news_prompt_group = pygame.sprite.Group()
        self.news_prompt_group.add(self.news_prompt)
        self.add_sprite_group(self.news_prompt_group)
        self.speed_button = SpeedButton("speed_button",
            (self.get_width() / 2 - 3.25 * self.border_distance, self.get_height() / 2 - 1.25 * self.border_distance,
             self.place_button_size * 1.4, self.place_button_size * 1.4))
        self.speed_button.set_speed_state("regular")
        self.speed_button_group = pygame.sprite.Group()
        self.speed_button_group.add(self.speed_button)
        self.add_sprite_group(self.speed_button_group)
        self.settings_button = Button("settings_button",
            (self.get_width() / 2 - 1.25 * self.border_distance, self.get_height() / 2 - 1.25 * self.border_distance,
            self.place_button_size * 1.5, self.place_button_size * 1.5), os.path.join("img", "settings.png"),
            os.path.join("img", "settings_highlighted.png"), os.path.join("img", "settings_pressed.png"))
        self.settings_button_group = pygame.sprite.Group()
        self.settings_button_group.add(self.settings_button)
        self.add_sprite_group(self.settings_button_group)
        self.info_button = Button("info_button",
            (-self.get_width() / 2 + 1.25 * self.border_distance, self.get_height() / 2 - 1.25 * self.border_distance,
            self.place_button_size * 1.5, self.place_button_size * 1.5), os.path.join("img", "info_button.png"),
            os.path.join("img", "info_button_highlighted.png"), os.path.join("img", "info_button_pressed.png"))
        self.info_button_group = pygame.sprite.Group()
        self.info_button_group.add(self.info_button)
        self.add_sprite_group(self.info_button_group)
        self.year_label = Label("year_label", str(int(self.game_handler.year)), (0, -self.get_height() / 2 + self.border_distance, 100, 50))
        self.money_label = Label("money_label", self.game_handler.get_money_text(),
            (4 * self.get_width() / 11, -self.get_height() / 2 + self.border_distance, 300, 50))
        self.apocalypse_label = Label("apocalypse_label", self.game_handler.shown_apocalypse_name,
            (-6 * self.get_width() / 13, -self.get_height() / 2 + self.border_distance - 2, 200, 50), font_size=15)
        # self.label_button = LabeledButton("label_button", "Label", (0, 0, 200, 40))
        self.label_group = pygame.sprite.Group()
        self.label_group.add(self.year_label)
        self.label_group.add(self.money_label)
        self.label_group.add(self.apocalypse_label)
        # self.label_group.add(self.label_button)
        self.add_sprite_group(self.label_group)

        # self.back_button = Button("back", (0, 0, side_length, side_length),
        #                      os.path.join("img", "place_button.png"),
        #                      os.path.join("img", "place_button_highlighted.png"),
        #                      os.path.join("img", "place_button_pressed.png"))
        # self.back_button_color_circle = Circle(hsv_to_rgb(self.color), (0, 0, side_length, side_length))
        # self.button_group = pygame.sprite.Group()
        # self.button_group.remove(self.back_button_color_circle)
        # self.button_group.add(self.back_button_color_circle)
        # self.button_group.add(self.back_button)
        # self.add_sprite_group(self.button_group)

    def refresh(self):
        # Time based stuff
        if self.if_first_entered is None:
            self.if_first_entered = True
        elif self.if_first_entered:
            self.if_first_entered = False
            return self.get_next_screen_values(self.info_button.identifier)

        # Handle the losing
        if self.game_handler.lose_message is not None:
            return self.get_next_screen_values("lose_game")

        # Handle alert messages
        if self.game_handler.alert_title_message is not None:
            return self.get_next_screen_values("alert")

        # Handle events
        if not self.news_prompt.is_showing_event():
            event = self.game_handler.get_next_event()
            if event is not None:
                if event.if_decision:
                    self.game_handler.set_deciding_event(event)
                    return self.get_next_screen_values("event_decision")
                else:
                    self.news_prompt.show_event(event)
                    self.game_handler.handle_event(event)

        # Handle the refreshing
        if self.game_handler.if_should_refresh():
            # self.game_handler = GameHandler()
            self.game_handler.refresh()
            self.reset_labels()
            # if win_status == "lose":
            #     return self.get_next_screen_values("lose_game")
            # elif win_status == "win":
            #     pass
        return None, None

    def reset_labels(self):
        self.money_label.change_label(self.game_handler.get_money_text())
        self.year_label.change_label(str(int(self.game_handler.year)))
        self.apocalypse_label.change_label(self.game_handler.shown_apocalypse_name)
        self.closeness_progress_bar.set_percent(self.game_handler.shown_closeness_percent)
        self.force_progress_bar.set_percent(self.game_handler.shown_force_percent)

    def add_place_buttons(self):
        self.place_button_group = pygame.sprite.Group()
        self.place_buttons = {}
        for i, place in enumerate(self.game_handler.place_handler.places):
            # These will be different for each button
            identifier = str(i) + "_" + place.id
            # print(place)
            x = float(place.x_location)
            y = float(place.y_location)
            x *= self.get_width()
            y *= self.get_height()

            # These will not be different
            color = self.initial_color
            percent = self.initial_percent
            place_button = Button(identifier, (x, y, self.place_button_size, self.place_button_size),
                                  os.path.join("img", "place_button.png"),
                                  os.path.join("img", "place_button_highlighted.png"),
                                  os.path.join("img", "place_button_pressed.png"))
            place_button_circle = Circle(color, (x, y, self.place_button_size, self.place_button_size))
            self.place_buttons[place.id] = (identifier, color, percent, place_button, place_button_circle)
            self.place_button_group.add(place_button_circle)
            self.place_button_group.add(place_button)
        self.add_sprite_group(self.place_button_group)

    def change_button_percent(self, identifier, percent):
        place_button_tuple = self.place_buttons[identifier]
        name = place_button_tuple[0]
        color = color_3_gradient(self.gradient[0], self.gradient[1], self.gradient[2], percent)
        place_button = place_button_tuple[3]
        place_button_circle = place_button_tuple[4]
        # new_color = int((color[0] + delta_hsv[0]) % 180), \
        #             int((color[1] + delta_hsv[1]) % 256), \
        #             int((color[2] + delta_hsv[2]) % 256)
        place_button_circle.change_color()
        self.place_buttons[identifier] = (name, color, percent, place_button, place_button_circle)

    def add_button_percent(self, identifier, delta_percent):
        place_button_tuple = self.place_buttons[identifier]
        name = place_button_tuple[0]
        percent = place_button_tuple[2]
        percent += delta_percent
        percent %= 101
        color = color_3_gradient(self.gradient[0], self.gradient[1], self.gradient[2], percent)
        place_button = place_button_tuple[3]
        place_button_circle = place_button_tuple[4]
        # new_color = int((color[0] + delta_hsv[0]) % 180), \
        #             int((color[1] + delta_hsv[1]) % 256), \
        #             int((color[2] + delta_hsv[2]) % 256)
        place_button_circle.change_color(color)
        self.place_buttons[identifier] = (name, color, percent, place_button, place_button_circle)

    def action(self, identifier):
        # self.percent += 2
        # self.percent %= 100

        # if identifier == self.closeness_progress_bar.identifier or identifier == self.force_progress_bar.identifier:
            # pass
            # self.percent += 5
            # self.closeness_progress_bar.set_percent(self.percent)
            # self.force_progress_bar.set_percent(self.percent)
            # self.game_handler.apocalypse_handler.apocalypses_dict["A001"].force += 10
            # return int(len(self.game_handler.place_handler.places)), None
        # elif identifier == self.news_prompt.identifier:
            # self.news_prompt.show_event(self.game_handler.event_handler.get_random_event())
            # pass
        if identifier == self.speed_button.identifier:
            self.speed_button.next_speed_state()
            self.game_handler.change_speed(self.speed_button.speed_state)
            self.news_prompt.change_speed(self.speed_button.speed_state)
        # elif identifier == self.label_button.identifier:
        #     self.label_button.change_text("Changed")
        # elif identifier == self.info_button.identifier:
            # pass
            # print("info")
        # elif identifier == self.money_label.identifier:
            # self.game_handler.money += 10
            # self.money_label.change_label(self.game_handler.get_money_text())
        # elif identifier == self.year_label.identifier:
            # self.game_handler.year += 1
            # self.year_label.change_label(str(int(self.game_handler.year)))
        # elif identifier == self.apocalypse_label.identifier:
            # pass
        # elif identifier == self.settings_button.identifier:
            # pass
        # else:
        # index = identifier[0]
        # identifier = identifier[1:]
        # self.add_button_percent(identifier, 5)
        return self.get_next_screen_values(identifier)

    def get_next_screen_values(self, identifier):
        if identifier is not None:
            num_places = len(self.game_handler.place_handler.places)
            if identifier == self.money_label.identifier:
                return num_places + 0, None
            elif identifier == self.closeness_progress_bar.identifier:
                return num_places + 1, None
            elif identifier == self.force_progress_bar.identifier:
                return num_places + 2, None
            elif identifier == self.news_prompt.identifier:
                return num_places + 3, None
            elif identifier == self.info_button.identifier:
                return num_places + 4, None
            elif identifier == self.settings_button.identifier:
                return num_places + 5, None
            elif identifier == "event_decision":
                return num_places + 6, None
            elif identifier == "lose_game":
                return num_places + 7, None
            elif identifier == "alert":
                title_message = self.game_handler.alert_title_message
                self.game_handler.alert_title_message = None
                return num_places + 8, title_message
            elif identifier == self.speed_button.identifier:
                return None, None
            elif identifier == self.year_label.identifier:
                return None, None
            elif identifier == self.apocalypse_label.identifier:
                return None, None
            # elif identifier == self.label_button.identifier:
            #     return None, None
            else:
                index, _ = identifier.split("_")
                return int(index), None


    #  self.change_button_color(((self.color[0] + 1) % 180, self.color[1], self.color[2]))
    def receive_next_values(self, next_values):
        self.game_handler.start()
        self.reset_labels()
