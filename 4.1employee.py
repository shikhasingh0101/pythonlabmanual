class Employee:
    def __init__(self):
        self.name = ""
        self.employeeID = 0
        self.salary = 0.0

class Employee:
    def __init__(self):
        self.name = ""
        self.employeeID = 0
        self.salary = 0.0

    def set_details(self):
        self.name = input("Enter a name: ")
        self.employeeID = int(input("Enter an ID: "))
        self.salary = float(input("Enter a salary: "))

    def print_details(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Employee ID:", self.employeeID)
        print("Salary: $", self.salary)

emp = Employee()
emp.set_details()
emp.print_details()
