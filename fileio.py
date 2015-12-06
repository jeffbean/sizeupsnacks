import json


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_json(filename, json_data):
    with open(filename, 'w') as f:
        json.dump(json_data, f)


def read_file_as_string(filename):
    with open (filename, "r") as f:
        return f.read().replace('\n', '')
