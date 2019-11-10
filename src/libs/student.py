from src.libs.person import Person

class Student(Person):
    def __init__(self, first_name, last_name, enrollment_id):
        Person.__init__(self, first_name, last_name, enrollment_id)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.enrollment_id}"
