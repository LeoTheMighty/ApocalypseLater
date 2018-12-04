from random import randint
from .CSVHandler import parse_csv_file, parse_inline_csv
import os


class EventHandler:
    def __init__(self):
        self.events = []
        self.events_dict = {}
        events_dict = parse_csv_file(os.path.join("csv", "events.csv"))
        for event_id, event_dict in events_dict.items():
            event = Event(event_id, event_dict)
            self.events.append(event)
            self.events_dict[event_id] = event
        self.n = 5

    def get_random_event(self):
        if self.n == 0:
            self.n = 5
            num_events = len(self.events)
            event_index = randint(0, 3 * num_events)
            if event_index < num_events:
                return self.events[event_index]
            return None
        else:
            self.n -= 1


class Event:
    def __init__(self, event_id, event_dict):
        self.id = None
        self.title = None
        self.type = None
        self.message = None
        self.closeness = None
        self.trickle = None
        self.force = None
        self.money = None
        self.money_trickle = None
        self.decline_money = None
        self.decline_closeness = None
        self.decline_trickle = None
        self.decline_force = None
        self.decline_money_trickle = None

        if {"title", "type", "message", "closeness", "trickle", "force", "money", "money_trickle", "decline_money", "decline_money_trickle", "decline_closeness", "decline_trickle", "decline_force"} <= set(event_dict):
            self.id = event_id
            self.title = event_dict["title"]
            self.type = event_dict["type"] if event_dict["type"] in ["alert", "decision", "news"] else print("ERROR EVENT TYPE VALUE INCORRECT")
            self.message = event_dict["message"]
            self.money = float(event_dict["money"]) if event_dict["money"] != "" else 0
            self.money_trickle = float(event_dict["money_trickle"]) if event_dict["money_trickle"] != "" else 0
            self.closeness = parse_inline_csv(event_dict["closeness"], True)
            self.trickle = parse_inline_csv(event_dict["trickle"], True)
            self.force = parse_inline_csv(event_dict["force"], True)
            self.decline_money = float(event_dict["decline_money"]) if event_dict["decline_money"] != "" else 0
            self.decline_money_trickle = float(event_dict["decline_money_trickle"]) if event_dict["decline_money_trickle"] != "" else 0
            self.decline_closeness = parse_inline_csv(event_dict["decline_closeness"], True)
            self.decline_trickle = parse_inline_csv(event_dict["decline_trickle"], True)
            self.decline_force = parse_inline_csv(event_dict["decline_force"], True)
        else:
            print("Improperly formed event dict")

