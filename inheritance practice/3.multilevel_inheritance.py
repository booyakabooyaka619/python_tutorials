class Employee:
    a = 1
class Teacher(Employee):
    b = 2

class Manager(Teacher):
    c = 3

# o = Employee()
# print(o.a)
# print(o.a, o.b)  This will throw an error as employee doesnt have an attribute b

o = Teacher()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)


