class Employee:
    def __init__(self, name, department, role):
        self.name = name
        self.department = department
        self.role = role
    def talkAboutWork(self):
        print("Man, Mondays, am I right?")
class SuperEmployee(Employee):
    def __init__(self,name,department,role):
        super().__init__(name,department,role) 
        self.securityLevel = "top level" #this overrides the inheritance of employee class
    def leadAStandup(self):
        print("Hey guys, lets start our standup")
    def accessClientData(self):
        print("Print out all the client data in a report")
stacy = SuperEmployee("stacy", "Engineering Group", "staff III")
rahmin = Employee("rahmin", "Engineering Group", "staff")
rayleigh = Employee("rayleigh", "Engineering Group", "staff")
amanda = Employee("amanda", "Engineering Group", "staff")

stacy.talkAboutWork()
stacy.leadAStandup()
print(stacy.securityLevel)


