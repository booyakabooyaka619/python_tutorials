class Employee:
    # def __init__(self,oldSalary,newSalary,increment):
    #     self.oldSalary = oldSalary
    #     self.newSalary = newSalary
    #     self.increment = increment

    # @property
    def salaryOld(self,newSalary,increment):
        return (newSalary - increment)
    
    # @property
    def salaryNew(self,oldSalary,increment):
        return (oldSalary + increment)
    
    # @property
    def newIncrement(self,newSalary,oldSalary):
        return(newSalary - oldSalary)
    
a = Employee()

# a.salaryNew(25,5)
print(a.salaryNew(25,5))

print(a.newIncrement(25,20))

