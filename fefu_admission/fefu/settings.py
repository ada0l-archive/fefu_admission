import os

from fefu_admission.university import Settings
from fefu_admission.utils import Utils

from lxml import html


class FefuSettings(Settings):
    URL_TABLE = "https://www.dvfu.ru/admission/spd/"

    def __init__(self, university):
        super().__init__(university,
                         data_path=os.path.join(os.path.expanduser('~'), ".fefu_admission"),
                         default_settings_content={
                             "me": None,
                             "list_of_departments": [
                                 "01.03.02 Прикладная математика и информатика",
                                 "02.03.01 Математика и компьютерные науки",
                                 "09.03.03 Прикладная информатика",
                                 "09.03.04 Программная инженерия"
                             ]
                         })

    def __get_html_with_departments_list(self):
        return Utils.get_response(
            method="get",
            url=self.URL_TABLE,
            data={
                "PROPERTY_1647": "Прием на обучение на бакалавриат/специалитет",
                "PROPERTY_1677": "Бюджетная основа",
                "PROPERTY_1648": "Очная",
                "PROPERTY_1652": "Владивосток",
                "PROPERTY_1642": self.default_settings_content["list_of_departments"][0]
            }).text

    def get_list_of_all_departments(self):
        page = html.fromstring(self.__get_html_with_departments_list())
        form = page.get_element_by_id("sel5")

        departments_list = []
        for item in form:
            item_str = item.text_content().replace("\t", "").replace("\n", "")
            if item_str != "":
                departments_list.append(item_str)
        return departments_list
