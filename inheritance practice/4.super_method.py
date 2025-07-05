class Employee:
    def __init__(self):
        print("This is the constructor of Employee")
    a = 1
class Teacher(Employee):
    def __init__(self):
        # super().__init__()
        print("This is the constructor of Teacher")
    b = 2

class Manager(Teacher):
    def __init__(self):
        super().__init__()
        print("This is the constructor of Manager")
    c = 3


o = Manager()
print(o.a, o.b, o.c)

# super() method is used to print init constructor of the parent class


