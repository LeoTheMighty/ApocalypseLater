from .Timer import Timer
from .CSVHandler import parse_csv_file
from .Event import EventHandler
from .Place import PlaceHandler
from .Apocalypse import ApocalypseHandler
from .LogicConstants import *
import os


class GameHandler:
    def __init__(self):
        self.name = None
        self.year = 2018.0
        self.speed = REGULAR_STEP_TIMER
        self.is_paused = True
        self.money = 1000000000.0
        self.money_trickle = 0
        # self.apocalypses = []
        # self.apocalypse_closeness = {}
        # self.apocalypse_closeness_trickle = {}
        # self.apocalypse_forces = {}
        self.shown_apocalypse_name = ""
        self.shown_closeness_percent = None
        self.shown_force_percent = None
        # The percentages of how close each apocalypse is
        # The amount each apocalypse increases each step
        # How strong our defenses against the apocalypses are
        self.apocalypse_handler = ApocalypseHandler()
        # Our event manager to handle getting the events
        self.event_handler = EventHandler()
        # Our event handler for handling all the global locations
        self.place_handler = PlaceHandler()
        self.news_events = []
        self.events_to_show = []
        self.step_timer = None
        self.deciding_event = None
        self.lose_message = None
        self.alert_title_message = None

    def initialize_game(self, name, save_file_name=None):
        self.name = name

        # The event feed that has occurred (limited at 5)
        self.events_to_show = []
        # self.events = []

        if save_file_name is None:
            # Init it from scratch
            # The current year
            self.year = 2018.0

            # The seconds between each step
            self.speed = REGULAR_STEP_TIMER

            # If we are paused
            self.is_paused = True

            # You start with a billion dollars
            self.money = 1000000000.0

            # How much you earn per step
            self.money_trickle = 500

            self.news_events = []
            self.events_to_show = []

            # How strong our defenses against the apocalypses are
            self.apocalypse_handler = ApocalypseHandler()
            # Our event manager to handle getting the events
            self.event_handler = EventHandler()
            # Our event handler for handling all the global locations
            self.place_handler = PlaceHandler()

            self.shown_apocalypse_name, self.shown_closeness_percent, self.shown_force_percent = self.get_closeness_force_percent()

            self.lose_message = None
            self.alert_title_message = None
        else:
            open(save_file_name, "r")

        self.step_timer = None

    def if_should_refresh(self):
        return not self.is_paused and self.step_timer.has_finished()

    def refresh(self):
        # Then we go another step
        # win_status = None
        self.year += 1

        # Update the trickle / speed stats
        self.money += self.money_trickle
        for apocalypse in self.apocalypse_handler.apocalypses:
            apocalypse.closeness += apocalypse.trickle
            if apocalypse.closeness >= 100:
                if apocalypse.force >= 50:
                    apocalypse.closeness = 50
                    apocalypse.force = 0
                    self.alert_title_message = (apocalypse.name + " almost ended us!", "Fortunately, our forces were strong enough to defend against it. However, they were completely eliminated in the process...")
                else:
                    self.lose_message = apocalypse.lose_message
            # TODO Check to see if the apocalypses have overflowed!
        for place in self.place_handler.places:
            max_apocalypse_percent = 0
            for apocalypse_id in place.apocalypse_indicators:
                percent = self.apocalypse_handler.apocalypses_dict[apocalypse_id].closeness
                max_apocalypse_percent = max(percent, max_apocalypse_percent)
            place.percent_indicated = max_apocalypse_percent
        self.shown_apocalypse_name, self.shown_closeness_percent, self.shown_force_percent = self.get_closeness_force_percent()
        event = self.event_handler.get_random_event()
        if event is not None:
            self.events_to_show.append(event)

        # Reset the step timer
        self.set_step_timer()
        # return win_status

    def start(self):
        self.is_paused = False
        self.set_step_timer()

    def pause(self):
        self.is_paused = True
        self.step_timer = None

    def get_closeness_force_percent(self):
        # Get the highest closeness and display that, then display the force corresponding to that one
        closest_apocalypse_name = ""
        closest_apocalypse_percent = 0
        closest_apocalypse_force_percent = 0
        for apocalypse in self.apocalypse_handler.apocalypses:
            if apocalypse.closeness > closest_apocalypse_percent:
                closest_apocalypse_name = apocalypse.name
                closest_apocalypse_percent = apocalypse.closeness
                closest_apocalypse_force_percent = apocalypse.force
        return closest_apocalypse_name, closest_apocalypse_percent, closest_apocalypse_force_percent

    def handle_event(self, event, if_accept=True):
        if if_accept:
            self.money += event.money
            self.money_trickle += event.money_trickle
            for apocalypse_id, value in event.closeness.items():
                self.apocalypse_handler.apocalypses_dict[apocalypse_id].closeness += value
            for apocalypse_id, value in event.trickle.items():
                self.apocalypse_handler.apocalypses_dict[apocalypse_id].trickle += value
            for apocalypse_id, value in event.force.items():
                self.apocalypse_handler.apocalypses_dict[apocalypse_id].force += value
        else:
            self.money += event.decline_money
            self.money_trickle += event.decline_money_trickle
            for apocalypse_id, value in event.decline_closeness.items():
                self.apocalypse_handler.apocalypses_dict[apocalypse_id].closeness += value
            for apocalypse_id, value in event.decline_trickle.items():
                self.apocalypse_handler.apocalypses_dict[apocalypse_id].trickle += value
            for apocalypse_id, value in event.decline_force.items():
                self.apocalypse_handler.apocalypses_dict[apocalypse_id].force += value

    def handle_place_funnel(self, place):
        self.money -= place.cost
        self.money_trickle += place.money_trickle
        for apocalypse_id, value in place.closeness.items():
            self.apocalypse_handler.apocalypses_dict[apocalypse_id].closeness += value
        for apocalypse_id, value in place.trickle.items():
            self.apocalypse_handler.apocalypses_dict[apocalypse_id].trickle += value
        for apocalypse_id, value in place.force.items():
            self.apocalypse_handler.apocalypses_dict[apocalypse_id].force += value

    def get_next_event(self):
        if len(self.events_to_show) > 0:
            event = self.events_to_show.pop(0)
            self.add_news_event(event)
            return event
        return None

    def add_news_event(self, event):
        self.news_events.insert(0, event)
        if len(self.news_events) > MAX_NEWS_EVENTS:
            del self.news_events[-1]

    def change_speed(self, speed):
        if speed == "slow":
            self.speed = SLOW_STEP_TIMER
            self.set_step_timer()
        elif speed == "regular":
            self.speed = REGULAR_STEP_TIMER
            self.set_step_timer()
        elif speed == "fast":
            self.speed = FAST_STEP_TIMER
            self.set_step_timer()
        elif speed == "fastest":
            self.speed = FASTEST_STEP_TIMER
            self.set_step_timer()
        else:
            print("Unrecognized speed: " + speed)

    def set_deciding_event(self, event):
        self.deciding_event = event

    def unset_deciding_event(self):
        self.deciding_event = None

    def set_step_timer(self):
        self.step_timer = Timer(self.speed)

    def get_money_text(self):
        return get_money_text(self.money)


def get_money_text(money):
    text = "$"
    money_text = str(float(money))
    parts = money_text.split(".")
    dollars = ""
    for i, c in enumerate(parts[0]):
        if (len(parts[0]) - i) % 3 == 0 and i != 0:
            dollars += ","
        dollars += c
    text += (dollars + ".")
    cents = parts[1]
    if len(cents) == 1:
        cents += "0"
    else:
        cents = cents[0] + cents[1]
    text += cents
    # text += str(round(self.money, 2))
    return text
