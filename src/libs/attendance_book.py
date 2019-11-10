from src.libs.student import Student
from src.libs.employee import Employee
from src.libs.person import sort_by_first_name, sort_by_enrollment_id, sort_by_last_name
from functools import cmp_to_key


class AttendanceBook:
    def __init__(self):
        self.attendance_sheet = []

    def sort_by_fisrt_name(self, person_list, incr=True):
        return sorted(person_list, key=cmp_to_key(sort_by_first_name), reverse = not incr)

    def sort_by_last_name(self, person_list, incr=True):
        return sorted(person_list, key=cmp_to_key(sort_by_last_name), reverse = not incr)

    def sort_by_last_name(self):
        pass

    def sort_by_enrollment_id(self, person_list, incr=True):
        return sorted(person_list, key=cmp_to_key(sort_by_enrollment_id), reverse = not incr)

    def get_all_students(self):
        students = []
        for i in range(self.attendance_sheet.__len__()):
            curr_person = self.attendance_sheet[i]
            if(type(curr_person) == Student):
                students.append(curr_person)

        return students

    def get_all_employees(self):
        employee = []
        for i in range(self.attendance_sheet.__len__()):
            curr_person = self.attendance_sheet[i]
            if (type(curr_person) == Employee):
                employee.append(curr_person)

        return employee


    def insert_person(self, person):
        self.attendance_sheet.append(person)