import json
import os

from fefu_admission.university.enrollee import Enrollee


class Settings:

    def __init__(self, university, data_path="", default_settings_content=None):
        self.data_path = data_path
        if default_settings_content is not None:
            self.default_settings_content = default_settings_content
        else:
            self.default_settings_content = {
                "me": None,
                "list_of_departments": []
            }
        self.university = university
        self.settings_file = os.path.join(self.data_path, "settings.json")

        data = self.get()
        self.me: Enrollee = Enrollee.get_from_json(data["me"])
        self.list_of_departments = data["list_of_departments"]

    def get(self):
        try:
            read_file = open(self.settings_file, "r")
            data = json.load(read_file)
            read_file.close()
            return data
        except FileNotFoundError:
            self.create_default_settings()
            self.get()

    def get_data_path(self):
        return self.data_path

    def create_default_settings(self):
        if not os.path.exists(self.university.data_path):
            os.makedirs(self.university.data_path)
        with open(self.settings_file, 'w') as settings_file:
            json.dump(self.default_settings_content, settings_file)
