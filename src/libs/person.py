class Person:
    def __init__(self, first_name, last_name, enrollment_id):
        self.first_name = first_name
        self.last_name = last_name
        self.enrollment_id = enrollment_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.enrollment_id}"





def sort_by_enrollment_id(person_obj1, person_obj2):
    if(person_obj1.enrollment_id < person_obj2.enrollment_id):
        return -1
    elif (person_obj1.enrollment_id > person_obj2.enrollment_id):
        return 1
    else:
        return 0


def sort_by_first_name(person_obj1, person_obj2):
    # ord() function returns position of ascii value of a character
    if(person_obj1.first_name[0][0] < person_obj2.first_name[0][0]):
        return -1
    elif (person_obj1.first_name[0][0] > person_obj2.first_name[0][0]):
        return 1
    else:
        return 0

def sort_by_last_name(person_obj1, person_obj2):
    # ord() function returns position of ascii value of a character
    if(person_obj1.last_name[0][0] < person_obj2.last_name[0][0]):
        return -1
    elif (person_obj1.last_name[0][0] > person_obj2.last_name[0][0]):
        return 1
    else:
        return 0