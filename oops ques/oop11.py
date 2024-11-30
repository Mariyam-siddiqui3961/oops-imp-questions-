# Composition with Aggregation:
# Write python code to create classes for “Department” and
# “Employee.” Use aggregation to represent that an Employee
# belongs to a Department. Implement methods to add
# employees to a department and calculate the average salary
# of employees in a department.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def average_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees) if self.employees else 0

# Example usage
dept = Department("Engineering")

emp1 = Employee("John", 50000)
emp2 = Employee("Alice", 60000)
emp3 = Employee("Bob", 55000)

dept.add_employee(emp1)
dept.add_employee(emp2)
dept.add_employee(emp3)

print("Average salary in", dept.name, "department:", dept.average_salary())
