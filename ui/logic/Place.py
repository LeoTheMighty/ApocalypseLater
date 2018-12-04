from .CSVHandler import parse_csv_file, parse_inline_csv, parse_inline_csv_list, get_random_value_from_range
import os


class PlaceHandler:
    def __init__(self):
        self.places = []
        self.places_dict = {}
        places_dict = parse_csv_file(os.path.join("csv", "places.csv"))
        for place_id, place_dict in places_dict.items():
            place = Place(place_id, place_dict)
            self.places.append(place)
            self.places_dict[place_id] = place


class Place:
    def __init__(self, place_id, place_dict):
        self.id = None
        self.name = None
        self.x_location = None
        self.y_location = None
        self.description = None
        self.cost = None
        self.money_trickle = None
        self.closeness = None
        self.trickle = None
        self.force = None
        self.apocalypse_indicators = None

        self.percent_indicated = 0

        if {"name", "x_location", "y_location", "description", "cost", "money_trickle", "closeness", "trickle", "force", "apocalypse_indicators"} <= set(place_dict):
            self.id = place_id
            self.name = place_dict["name"]
            self.x_location = float(place_dict["x_location"])
            self.y_location = float(place_dict["y_location"])
            self.description = place_dict["description"]
            self.cost = float(place_dict["cost"]) if place_dict["cost"] != "" else 0
            self.money_trickle = float(place_dict["money_trickle"]) if place_dict["money_trickle"] != "" else 0
            self.closeness = parse_inline_csv(place_dict["closeness"], True)
            self.trickle = parse_inline_csv(place_dict["trickle"], True)
            self.force = parse_inline_csv(place_dict["force"], True)
            self.apocalypse_indicators = parse_inline_csv_list(place_dict["apocalypse_indicators"])
        else:
            print("Improperly formed place dict = " + str(place_dict))
