class Employee:
    company = "Microsoft"
    def details(self):
        print(f"Hello I work for the company {self.company}")

class Manager(Employee):
    language = "python"
    def intro(self):
        print(f"I love {self.language} the most")

a = Manager()
a.company = "Apple"
a.language = "java"

a.details()
a.intro()


