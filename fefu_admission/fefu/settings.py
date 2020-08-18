import os

from fefu_admission.university import Settings


class FefuSettings(Settings):

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
