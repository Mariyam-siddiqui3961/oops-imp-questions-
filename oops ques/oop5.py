# Multiple Inheritance:
# Create three classes, “Person,” “Employee,” and “Student.”
# Use multiple inheritance to create a class “PersonInfo” that
# inherits from both “Employee” and “Student.” Add
# attributes and methods specific to each class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee_info(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

class Student:
    def __init__(self, student_id, grade):
        self.student_id = student_id
        self.grade = grade

    def display_student_info(self):
        print("Student ID:", self.student_id)
        print("Grade:", self.grade)

class PersonInfo(Person, Employee, Student):
    def __init__(self, name, age, emp_id, salary, student_id, grade):
        # Call constructors of parent classes explicitly
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        Student.__init__(self, student_id, grade)

    def display_person_info(self):
        self.display_info()
        self.display_employee_info()
        self.display_student_info()

# Example usage
person_info = PersonInfo("John", 30, "E123", 50000, "S456", "A")
person_info.display_person_info()
