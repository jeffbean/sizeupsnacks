import json


class FileIO:
    @staticmethod
    def read():
        with open('data.json', 'r') as f:
            return json.load(f)

    @staticmethod
    def write(json_data):
        with open('data.json', 'w') as f:
            json.dump(json_data, f)

