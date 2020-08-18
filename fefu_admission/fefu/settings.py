import os
import logging

from fefu_admission.university import Settings

import requests
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
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }

        response = requests.get(self.URL_TABLE, headers=headers, verify=True)
        logging.info("Status code: " + str(response.status_code))

        headers["cookie"] = '; '.join([x.name + '=' + x.value for x in response.cookies])
        headers["content-type"] = 'application/x-www-form-urlencoded'
        payload = {
            "PROPERTY_1647": "Прием на обучение на бакалавриат/специалитет",
            "PROPERTY_1677": "Бюджетная основа",
            "PROPERTY_1648": "Очная",
            "PROPERTY_1652": "Владивосток",
            "PROPERTY_1642": self.default_settings_content["list_of_departments"][0]
        }

        response = requests.post(self.URL_TABLE, data=payload, headers=headers,
                                 verify=True)

        return response.text

    def get_list_of_all_departments(self):
        page = html.fromstring(self.__get_html_with_departments_list())
        form = page.get_element_by_id("sel5")

        departments_list = []
        for item in form:
            item_str = item.text_content().replace("\t", "").replace("\n", "")
            if item_str != "":
                departments_list.append(item_str)
        return departments_list
