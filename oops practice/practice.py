class Programmer:
    company= "Microsoft"
    
    def __init__(self,name,age,salary,designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation

anushree = Programmer("anushree", 22, 200000000000, "Engineer")
print(f"Hello I am {anushree.name}, my age is {anushree.age}, my salary is {anushree.salary} and I am an {anushree.designation} and i work for {anushree.company}")


