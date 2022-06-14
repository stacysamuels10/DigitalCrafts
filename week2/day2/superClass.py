class Employee:
    def __init__(self, name, department, role):
        self.name = name
        self.department = department
        self.role = role

    rahmin = Employee("rahmin", "Engineering Group", "staff")
    rayleigh = Employee("rayleigh", "Engineering Group", "staff")
    carlos = Employee("carlos", "Engineering", "Engineering Group", "staff")
    amanda = Employee("amanda", "Engineering", "Engineering Group", "staff")

class SuperEmployee(Employee):
    pass
stacy = SuperEmployee