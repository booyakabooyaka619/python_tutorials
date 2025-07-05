# just like we had @staticmethod in python that runs without self arguement, for similar purpose we use @classmethod, 
# as we know the instance attribute is always prioritized before class attribute, 
# but by using @classmethod we prioritize class attribute before instance attribute,
# over here instead of self attribute we use cls to denote a class method

# Normal case that prioritizes Apple(instance attribute) over Microsoft(class attribute)
class Employee:
    company = "Microsoft"
    def details(cls):
        print(f"My company is {cls.company}")

a = Employee()
a.company = "Apple"
a.details()


# class method
class Employee:
    company = "Microsoft"
    @classmethod
    def details(cls):
        print(f"My company is {cls.company}")

a = Employee()
a.company = "Apple"
a.details()