import sys
import os
from random import uniform


def parse_csv_file(file_path):
    file_dict = {}
    names = []
    file = open(file_path, "r")
    is_first = True
    for line in file:
        values = [x.strip() for x in line.split(",")]
        if is_first:
            is_first = False
            names = values
        else:
            if_first = True
            item_id = None
            for i, value in enumerate(values):
                if if_first:
                    if_first = False
                    item_id = value
                    if item_id == "E011":
                        print("ay")
                    file_dict[item_id] = {}
                else:
                    if item_id:
                        if len(names) <= i and value == "":
                            # This is probably a dumb error
                            continue
                            # print(value, i, len(names))
                        else:
                            file_dict[item_id][names[i]] = value.replace(";", ",")
                    else:
                        print("DID NOT SET THE ITEM ID")
                        sys.exit(-2)
    return file_dict


def parse_inline_csv(string, if_values_float=False):
    # A001_0.0101;A002_1.9;
    inline_csv_dict = {}
    csv_values = [x.strip() for x in string.split(",")]
    for csv_value in csv_values:
        values = csv_value.split("_")
        if len(values) == 2:
            if if_values_float:
                inline_csv_dict[values[0]] = float(values[1])
            else:
                inline_csv_dict[values[0]] = values[1]
    return inline_csv_dict


def parse_inline_csv_list(string):
    return [x.strip() for x in string.split(",") if x != ""]


def get_random_value_from_range(string):
    values = string.split('-')
    if len(values) == 0 or values[0] == "":
        return 0
    if len(values) == 1:
        return float(values[0])
    elif len(values) == 2:
        return uniform(float(values[0]), float(values[1]))
    else:
        print("INCORRECTLY FORMATTED!!")


if __name__ == "__main__":
    filepath = os.path.join("..", "..", "csv", "places.csv")
    places = parse_csv_file(filepath)
    for place_id, place in places.items():
        print("ID = " + place_id)
        for name, value in place.items():
            print("    " + name + " = " + value)
