import json


class Importer:

    def __init__(self):
        self.taski = None

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        try:
            with open('taski.json', encoding="utf-8") as json_file:
                data = json.load(json_file)
                self.taski = data
        except FileNotFoundError:
            self.taski = []

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        if self.taski is None:
            self.read_tasks()
        
        return self.taski