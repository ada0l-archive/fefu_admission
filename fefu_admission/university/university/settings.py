import json
import os

from fefu_admission.university.enrollee import Enrollee
from fefu_admission.prompt import Prompt


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
        if data is not None:
            self.me: Enrollee = Enrollee.get_from_json(data.get("me", None))
            self.list_of_departments = data["list_of_departments"]
        else:
            self.me = None
            self.list_of_departments = []

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

    def __create_settings(self, settings_content):
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        with open(self.settings_file, 'w') as settings_file:
            json.dump(settings_content, settings_file)

    def create_default_settings(self):
        self.__create_settings(self.default_settings_content)

    def get_list_of_all_departments(self):
        return []

    def get_generated_settings(self):
        selected_departments_str = []
        print("Do you want to add this direction?")
        for department_str in self.get_list_of_all_departments():
            answer = Prompt.get_confirm(department_str)
            if answer == Prompt.YES:
                selected_departments_str.append(department_str)
            else:
                pass
        me = None
        if Prompt.get_confirm("do you want to know your place on the list?") == Prompt.YES:
            name = Prompt.get_str("Enter name")
            points = [int(x) for x in Prompt.get_str("Enter your points").split(" ")]
            me = Enrollee(name, points, True)
        settings = {
            "list_of_departments": selected_departments_str
        }
        if me is not None:
            settings["me"] = {
                "name": me.name,
                "points": me.points,
                "agreement": me.agreement
            }
        else:
            settings["me"] = None
        return settings

    def generate_and_save_settings(self):
        self.__create_settings(self.get_generated_settings())
