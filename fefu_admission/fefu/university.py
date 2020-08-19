from fefu_admission.university.university.university import University

from .department import FefuDepartment


class FefuUniversity(University):

    def __init__(self, settings):
        self.name = "ДВФУ"
        self.departments = []
        self.departmentClass = FefuDepartment
        super().__init__(settings=settings)
