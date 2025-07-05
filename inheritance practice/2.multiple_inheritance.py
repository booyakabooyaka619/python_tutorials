class Employee:
    company = "Microsoft"
    def details(self):
        print(f"Hello I work for the company {self.company}")

class Teacher:
    def sub(self):
        print(f"I like to teach {self.subject}")

class Manager(Employee, Teacher):
    def intro(self):
        print(f"I love {self.language} the most")

a = Manager()
a.company = "Apple"
a.language = "java"
a.subject = "HTML"

a.details()
a.sub()
a.intro()


