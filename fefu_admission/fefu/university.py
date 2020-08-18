from fefu_admission.university.university.university import University

from .department import FefuDepartment


class FefuUniversity(University):

    def __init__(self, settings):
        super().__init__(settings=settings)
        self.name = "ДВФУ"
        self.departments = []
        self.settings = settings(self)
        for department in self.settings.list_of_departments:
            self.departments.append(FefuDepartment(department, self))
