class Employee:
    def __init__(self, name, department, role):
        self.name = name
        self.department = department
        self.role = role
    def talkAboutWork(self):
        print("Man, Mondays, am I right?")

    rahmin = Employee("rahmin", "Engineering Group", "staff")
    rayleigh = Employee("rayleigh", "Engineering Group", "staff")
    carlos = Employee("carlos", "Engineering", "Engineering Group", "staff")
    amanda = Employee("amanda", "Engineering", "Engineering Group", "staff")

class SuperEmployee(Employee):
    def leadAStandup(self):
        print("Hey guys, lets start our standup")
    pass
stacy = SuperEmployee("stacy", "Engineering Group", "staff III")
stacy.talkAboutWork()
carlos.talkAboutWork()
stacy.leadAStandup()
carlos.leadAStandup()