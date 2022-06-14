#parent
#adoptive parent
#child annoying level of 2
#sibling annoying level of 5

class Parent:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def schoolDay(self):
        print("How was your day at school?")

class Child(Parent):
    def __init__(self, first_name, last_name, age, sibling_order):
        super().__init__(first_name, last_name, age)
        self.sibling_order = sibling_order
    def answerSchoolDay(self):
        answer = input("What is your answer?\n")
        print(answer)

Lisa = Parent("Lisa", "Samuels", "55")
Sheldon = Parent("Sheldon", "Samuels", "53")
Jason = Child("Jason", "Samuels", "32", 1)
Stacy = Child("Stacy", "Samuels", "30", 2)

Sheldon.schoolDay()
Stacy.answerSchoolDay()