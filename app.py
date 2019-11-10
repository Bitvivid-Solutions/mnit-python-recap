from src.libs.student import Student
from src.libs.employee import Employee
from src.libs.attendance_book import AttendanceBook
from src.libs.input_validators import get_non_negative_int, get_string_value

number_of_person_per_role = 3
# Create a new attendance sheet
my_attendance_sheet = AttendanceBook()

# Insert details of 5 students
for i in range(number_of_person_per_role):
    first_name = get_string_value("Enter first name of the student: ")
    last_name = get_string_value("Enter last name of the student: ")
    enrollment_id = get_non_negative_int("Enter enrollment-id of the student: ")
    print("---------------------------------------------\n")
    student = Student(first_name, last_name, enrollment_id)
    my_attendance_sheet.insert_person(student)
    # create student object

    #insert in attendance object


# Insert details of 5 employees
for i in range(number_of_person_per_role):
    first_name = get_string_value("Enter first name of the employee: ")
    last_name = get_string_value("Enter last name of the employee: ")
    enrollment_id = get_non_negative_int("Enter enrollment-id of the employee: ")
    print("--------------------------------------------\n")
    employee = Employee(first_name, last_name, enrollment_id)
    my_attendance_sheet.insert_person(employee)



# Display list of total students in attendance sheet
print("list of all the students: ", my_attendance_sheet.get_all_students().__len__())


# Display list of total employees in attendance sheet
print("list of all the employees: ", my_attendance_sheet.get_all_employees().__len__())

print("------------------------------------------------------------------------------------- \n")

# Display list of students in alphabetical order of their last name

# Display list of students in increasing order of their enrollment-id
for std in my_attendance_sheet.sort_by_enrollment_id(my_attendance_sheet.get_all_students()):
    print(std)

print("------------------------------------------------------------------------------------- \n")
# Display list of students in decreasing order of their enrollment-id
for std in my_attendance_sheet.sort_by_enrollment_id(my_attendance_sheet.get_all_students(), False):
    print(std)

print("------------------------------------------------------------------------------------- \n")

# Display list of students sorted in by their first name
for std in my_attendance_sheet.sort_by_fisrt_name(my_attendance_sheet.get_all_students()):
    print(std)

print("------------------------------------------------------------------------------------- \n")

# Display list of students sorted in by their last name
for std in my_attendance_sheet.sort_by_fisrt_name(my_attendance_sheet.get_all_students()):
    print(std)

print("------------------------------------------------------------------------------------- \n")

# Display total number of students and employees

