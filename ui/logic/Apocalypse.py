from random import randint
from .CSVHandler import parse_csv_file, get_random_value_from_range
import os


class ApocalypseHandler:
    def __init__(self):
        self.apocalypses = []
        self.apocalypses_dict = {}
        apocalypse_csv = parse_csv_file(os.path.join("csv", "apocalypses.csv"))
        for apocalypse_id, apocalypse_dict in apocalypse_csv.items():
            apocalypse = Apocalypse(apocalypse_id, apocalypse_dict)
            self.apocalypses.append(apocalypse)
            self.apocalypses_dict[apocalypse_id] = apocalypse


class Apocalypse:
    def __init__(self, apocalypse_id, apocalypse_dict):
        self.id = None
        self.name = None
        self.closeness = None
        self.trickle = None
        self.force = None
        self.lose_message = None

        if {"name", "initial_closeness", "initial_trickle", "initial_force", "lose_message"} <= set(apocalypse_dict):
            self.id = apocalypse_id
            self.name = apocalypse_dict["name"]
            self.closeness = get_random_value_from_range(apocalypse_dict["initial_closeness"])
            self.trickle = get_random_value_from_range(apocalypse_dict["initial_trickle"])
            self.force = get_random_value_from_range(apocalypse_dict["initial_force"])
            self.lose_message = apocalypse_dict["lose_message"]
        else:
            print("Improperly formed apocalypse dict")
